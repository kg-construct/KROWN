#!/usr/bin/env python3

"""
MySQL is an open-source relational database management system developed by
Oracle Corporation.

**Website**: https://www.mysql.com/<br>
**Repository**: https://github.com/mysql/mysql-server
"""

import os
import pymysql
import tempfile
from csv import reader
from typing import List, Tuple
from timeout_decorator import timeout, TimeoutError  # type: ignore
from bench_executor.container import Container
from bench_executor.logger import Logger

VERSION = '8.0'
HOST = 'localhost'
USER = 'root'
PASSWORD = 'root'
DB = 'db'
PORT = '3306'
CLEAR_TABLES_TIMEOUT = 5 * 60  # 5 minutes


class MySQL(Container):
    """MySQL container for executing SQL queries."""
    def __init__(self, data_path: str, config_path: str, directory: str,
                 verbose: bool):
        """Creates an instance of the MySQL class.

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
        self._tables: List[str] = []
        tmp_dir = os.path.join(tempfile.gettempdir(), 'mysql')
        os.umask(0)
        os.makedirs(tmp_dir, exist_ok=True)
        os.makedirs(os.path.join(self._data_path, 'mysql'), exist_ok=True)

        super().__init__(f'blindreviewing/mysql:v{VERSION}', 'MySQL',
                         self._logger,
                         ports={PORT: PORT},
                         environment={'MYSQL_ROOT_PASSWORD': 'root',
                                      'MYSQL_DATABASE': 'db'},
                         volumes=[f'{self._data_path}/shared/:/data/shared',
                                  f'{self._config_path}/mysql/'
                                  f'mysql-secure-file-prive.cnf:'
                                  f'/etc/mysql/conf.d/'
                                  f'mysql-secure-file-prive.cnf',
                                  f'{tmp_dir}:/var/lib/mysql'])

    def initialization(self) -> bool:
        """Initialize MySQL's database.

        Returns
        -------
        success : bool
            Whether the initialization was successfull or not.
        """
        # MySQL should start with a initialized database, start MySQL
        # if not initialized to avoid the pre-run start during benchmark
        # execution
        success = self.wait_until_ready()
        if not success:
            return False
        success = self.stop()

        return success

    @property
    def root_mount_directory(self) -> str:
        """Subdirectory in the root directory of the case for MySQL.

        Returns
        -------
        subdirectory : str
            Subdirectory of the root directory for MySQL.
        """
        return __name__.lower()

    def wait_until_ready(self, command: str = '') -> bool:
        """Wait until MySQL is ready to execute SQL queries.

        Parameters
        ----------
        command : str
            Command to execute in the MySQL container, optionally, defaults to
            no command.

        Returns
        -------
        success : bool
            Whether the MySQL was initialized successfull or not.
        """
        log_line = f'port: {PORT}  MySQL Community Server - GPL.'
        return self.run_and_wait_for_log(log_line, command=command)

    def load(self, csv_file: str, table: str) -> bool:
        """Load a single CSV file into MySQL.

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
        """Load multiple CSV files into MySQL.

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

    def load_sql_schema(self, schema_file: str,
                        csv_files: List[Tuple[str, str]]) -> bool:
        """Execute SQL schema with MySQL.

        Executes a .sql file with MySQL.
        If the data is not loaded by the .sql file but only the schema is
        provided through the .sql file, a list of CSV files can be provided to
        load them as well.

        Parameters
        ----------
        schema_file : str
            Name of the .sql file.
        csv_files : List[Tuple[str, str]]
            List of CSV file names to load in the tables created with the .sql
            file, may also be an empty list. Each entry contains a Tuple with
            the name of the CSV file and the table name.

        Returns
        -------
        success : bool
            Whether the execution was successfull or not.
        """
        success = True

        # Load SQL schema
        cmd = f'/bin/sh -c \'mysql --host={HOST} --port={PORT} ' + \
              f'--user={USER} --password={PASSWORD} --database={DB} ' + \
              f'< /data/shared/{schema_file}\''
        success, output = self.exec(cmd)

        # Load CSVs
        if success:
            for csv_file, table in csv_files:
                success = self._load_csv(csv_file, table, False)
                if not success:
                    break

        return success

    def _load_csv(self, csv_file: str, table: str, create: bool) -> bool:
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
        path2 = os.path.join(self._data_path, 'shared', f'tmp_{csv_file}')

        self._tables.append(table)

        # Analyze CSV for loading
        if not os.path.exists(path):
            self._logger.error(f'CSV file "{path}" does not exist')
            return False

        with open(path, 'r') as f:
            csv_reader = reader(f)
            columns = next(csv_reader)
            columns = [x.lower() for x in columns]

        # MySQL cannot set NULL as NULL keyword, use their own specific syntax
        # for this: \N
        with open(path, 'r') as f:
            data = f.read()
            data = data.replace('NULL', '\\N')

            with open(path2, 'w') as f2:
                f2.write(data)

        # Load CSV
        connection = pymysql.connect(host=HOST, user=USER, password=PASSWORD,
                                     db=DB)
        try:
            cursor = connection.cursor()

            if create:
                cursor.execute(f'DROP TABLE IF EXISTS {table};')
                c = ' TEXT , '.join(columns) + ' TEXT'
                cursor.execute(f'CREATE TABLE {table} (k INT ZEROFILL '
                               f'NOT NULL AUTO_INCREMENT, {c}, '
                               f'PRIMARY KEY(k));')
            c = ','.join(columns)
            cursor.execute(f'LOAD DATA INFILE \'/data/shared/tmp_{csv_file}\' '
                           f'INTO TABLE {table} FIELDS TERMINATED BY \',\' '
                           f'ENCLOSED BY \'\\"\' LINES TERMINATED BY \'\\n\' '
                           f'IGNORE 1 ROWS ({c});')
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
        connection = pymysql.connect(host=HOST, database=DB,
                                     user=PASSWORD, password=PASSWORD)
        cursor = connection.cursor()
        for table in self._tables:
            cursor.execute(f'DROP TABLE IF EXISTS {table};')
            cursor.execute('COMMIT;')
        self._tables = []
        connection.close()

    def stop(self) -> bool:
        """Stop MySQL
        Clears all tables and stops the MySQL container.

        Returns
        -------
        success : bool
            Whether the execution was successfull or not.
        """
        try:
            self._clear_tables()
        except TimeoutError:
            self._logger.warning('Clearing MySQL tables timed out after '
                                 f'{CLEAR_TABLES_TIMEOUT}s!')

        return super().stop()


if __name__ == '__main__':
    print(f'ℹ️  Starting up MySQL v{VERSION}...')
    m = MySQL('data', 'config', 'log', True)
    m.wait_until_ready()
    input('ℹ️  Press any key to stop')
    m.stop()
    print('ℹ️  Stopped')
