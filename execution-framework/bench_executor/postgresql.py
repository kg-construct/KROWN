#!/usr/bin/env python3

"""
PostgreSQL is an open-source relational database developed by The PostgreSQL
Global Development Group.

**Website**: https://www.postgresql.org/<br>
**Repository**: https://git.postgresql.org/gitweb/?p=postgresql.git
"""

import os
import psycopg2
import tempfile
from csv import reader
from time import sleep
from typing import List, Tuple
from timeout_decorator import timeout, TimeoutError  # type: ignore
from bench_executor.container import Container
from bench_executor.logger import Logger

VERSION = '14.5'
HOST = 'localhost'
USER = 'root'
PASSWORD = 'root'
DB = 'db'
PORT = '5432'
WAIT_TIME = 3
CLEAR_TABLES_TIMEOUT = 5 * 60  # 5 minutes


class PostgreSQL(Container):
    """PostgreSQL container for executing SQL queries"""
    def __init__(self, data_path: str, config_path: str, directory: str,
                 verbose: bool):
        """Creates an instance of the PostgreSQL class.

        Parameters
        ----------
        data_path : str
            Path to the data directory of the case.
        config_path : str
            Path to the config directory of the case.
        directory : str
            Path to the directory to store logs.
        verbose : bool
            Enable verbose logs.
        """
        self._data_path = os.path.abspath(data_path)
        self._config_path = os.path.abspath(config_path)
        self._logger = Logger(__name__, directory, verbose)

        tmp_dir = os.path.join(tempfile.gettempdir(), 'postgresql')
        os.umask(0)
        os.makedirs(tmp_dir, exist_ok=True)
        os.makedirs(os.path.join(self._data_path, 'postgresql'), exist_ok=True)
        self._tables: List[str] = []

        super().__init__(f'blindreviewing/postgresql:v{VERSION}', 'PostgreSQL',
                         self._logger,
                         ports={PORT: PORT},
                         environment={'POSTGRES_PASSWORD': PASSWORD,
                                      'POSTGRES_USER': USER,
                                      'POSTGRES_DB': DB,
                                      'PGPASSWORD': PASSWORD,
                                      'POSTGRES_HOST_AUTH_METHOD': 'trust'},
                         volumes=[f'{self._data_path}/shared:/data/shared',
                                  f'{tmp_dir}:/var/lib/postgresql/data'])

    def initialization(self) -> bool:
        """Initialize PostgreSQL's database.

        Returns
        -------
        success : bool
            Whether the initialization was successfull or not.
        """
        # PostgreSQL should start with a initialized database, start PostgreSQL
        # if not initialized to avoid the pre-run start during benchmark
        # execution
        success = self.wait_until_ready()
        if not success:
            self._logger.error(f'Failed to initialize {__name__}')
            return False
        success = self.stop()

        return success

    @property
    def root_mount_directory(self) -> str:
        """Subdirectory in the root directory of the case for PostgreSQL.

        Returns
        -------
        subdirectory : str
            Subdirectory of the root directory for PostgreSQL.
        """
        return __name__.lower()

    def wait_until_ready(self, command: str = '') -> bool:
        """Wait until PostgreSQL is ready to execute SQL queries.

        Parameters
        ----------
        command : str
            Command to execute in the PostgreSQL container, optionally,
            defaults to no command.

        Returns
        -------
        success : bool
            Whether the PostgreSQL was initialized successfull or not.
        """
        success = self.run_and_wait_for_log(f'port {PORT}', command=command)
        if success:
            sleep(WAIT_TIME)
        else:
            msg = f'Failed to wait for {__name__} to become ready'
            self._logger.error(msg)

        return success

    def load(self, csv_file: str, table: str) -> bool:
        """Load a single CSV file into PostgreSQL.

        Parameters
        ----------
        csv_file : str
            Name of the CSV file.
        table : str
            Name of the table.

        Returns
        -------
        success : bool
            Whether the execution was successfull or not.
        """
        return self._load_csv(csv_file, table, True)

    def load_multiple(self, csv_files: List[dict]) -> bool:
        """Load multiple CSV files into PostgreSQL.

        Parameters
        ----------
        csv_files : list
            List of CSV files to load. Each entry consist of a `file` and
            `table` key.

        Returns
        -------
        success : bool
            Whether the execution was successfull or not.
        """
        for entry in csv_files:
            if not self._load_csv(entry['file'], entry['table'], True):
                return False
        return True
        for entry in csv_files:
            if not self._load_csv(entry['file'], entry['table'], True):
                return False
        return True

    def load_sql_schema(self, schema_file: str,
                        csv_files: List[Tuple[str, str]]) -> bool:
        """Execute SQL schema with PostgreSQL.

        Executes a .sql file with PostgreSQL.
        If the data is not loaded by the .sql file but only the schema is
        provided through the .sql file, a list of CSV files can be provided to
        load them as well.

        Parameters
        ----------
        schema_file : str
            Name of the .sql file.
        csv_files : List[Tuple[str, str]]]
            List of CSV file names to load in the tables created with the .sql
            file, may also be an empty list. Each entry contains a Tuple of the
            CSV file name and the table name.

        Returns
        -------
        success : bool
            Whether the execution was successfull or not.
        """
        success = True

        # Load SQL schema
        success, output = self.exec(f'psql -h {HOST} -p {PORT} -U {USER} '
                                    f'-d {DB} -f /data/shared/{schema_file}')
        if not success:
            self._logger.error(f'Failed to load SQL schema "{schema_file}"')
            return success

        # Load CSVs
        for csv_file, table in csv_files:
            success = self._load_csv(csv_file, table, False)
            if not success:
                self._logger.error(f'Failed to load CSV "{csv_file}" in '
                                   f'table "{table}"')
                break

        return success

    def _load_csv(self, csv_file: str, table: str, create: bool):
        """Load a single CSV file into MySQL.

        Parameters
        ----------
        csv_file : str
            Name of the CSV file.
        table : str
            Name of the table to store the data in.
        create : bool
            Whether to drop and create the table or re-use it

        Returns
        -------
        success : bool
            Whether the execution was successfull or not.
        """
        success = True
        columns = None
        table = table.lower()
        path = os.path.join(self._data_path, 'shared', csv_file)

        self._tables.append(table)

        # Analyze and move CSV for loading
        if not os.path.exists(path):
            self._logger.error(f'CSV file "{path}" does not exist')
            return False

        with open(path, 'r') as f:
            csv_reader = reader(f)
            columns = next(csv_reader)
            columns = [x.lower() for x in columns]

        # Load CSV
        connection = psycopg2.connect(host=HOST, database=DB,
                                      user=PASSWORD, password=PASSWORD)
        try:
            cursor = connection.cursor()

            if create:
                cursor.execute(f'DROP TABLE IF EXISTS {table};')
                c = ' VARCHAR , '.join(columns) + ' VARCHAR'
                cursor.execute(f'CREATE TABLE {table} (KEY SERIAL, {c}, '
                               'PRIMARY KEY(KEY))')

            c = ','.join(columns)
            cursor.execute(f'COPY {table} ({c}) FROM '
                           f'\'/data/shared/{csv_file}\' '
                           'DELIMITER \',\' NULL \'NULL\' CSV HEADER;')
            cursor.execute('COMMIT;')

            header = '| ID | ' + ' | '.join(columns) + ' |'
            self._logger.debug(header)
            self._logger.debug('-' * len(header))

            cursor.execute(f'SELECT * FROM {table};')
            number_of_records = 0
            for record in cursor:
                number_of_records += 1
                self._logger.debug(record)
            if number_of_records == 0:
                self._logger.error('No records loaded after loading CSV')
                success = False
        except Exception as e:
            self._logger.error(f'Failed to load CSV: "{e}"')
            success = False
        finally:
            connection.close()

        return success

    @timeout(CLEAR_TABLES_TIMEOUT)
    def _clear_tables(self):
        """Clears all tables with a provided timeout."""
        connection = psycopg2.connect(host=HOST, database=DB,
                                      user=PASSWORD, password=PASSWORD)
        cursor = connection.cursor()
        for table in self._tables:
            cursor.execute(f'DROP TABLE IF EXISTS {table};')
            cursor.execute('COMMIT;')
        self._tables = []
        connection.close()

    def stop(self) -> bool:
        """Stop PostgreSQL
        Clears all tables and stops the PostgreSQL container.

        Returns
        -------
        success : bool
            Whether the execution was successfull or not.
        """
        try:
            self._clear_tables()
        except TimeoutError:
            self._logger.warning(f'Clearing {__name__} tables timed out after '
                                 f'{CLEAR_TABLES_TIMEOUT}s!')
        except Exception as e:
            self._logger.error(f'Clearing{__name__} tables failed: "{e}"')

        return super().stop()


if __name__ == '__main__':
    print('Use "postgresql" CLI tool to run PostgreSQL standalone.')
