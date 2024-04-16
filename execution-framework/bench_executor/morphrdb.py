#!/usr/bin/env python3

"""
Morph-RDB (formerly called ODEMapster) is an RDB2RDF engine developed by
the Ontology Engineering Group, which follows the R2RML specification.

**Website**: https://oeg.fi.upm.es/index.php/en/technologies/315-morph-rdb/index.html <br>
**Repository**: https://github.com/oeg-upm/morph-rdb
"""  # noqa: E501

import os
import psutil
import configparser
from timeout_decorator import timeout, TimeoutError  # type: ignore
from bench_executor.container import Container
from bench_executor.logger import Logger

VERSION = '3.12.5'
TIMEOUT = 6 * 3600  # 6 hours


class MorphRDB(Container):
    """Morph-RDB container for executing R2RML mappings."""
    def __init__(self, data_path: str, config_path: str, directory: str,
                 verbose: bool):
        """Creates an instance of the MorphRDB class.

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

        os.umask(0)
        os.makedirs(os.path.join(self._data_path, 'morphrdb'), exist_ok=True)
        super().__init__(f'blindreviewing/morph-rdb:v{VERSION}', 'Morph-RDB',
                         self._logger,
                         volumes=[f'{self._data_path}/shared:/data/shared',
                                  f'{self._data_path}/morphrdb:/data'])

    @property
    def root_mount_directory(self) -> str:
        """Subdirectory in the root directory of the case for Morph-RDB.

        Returns
        -------
        subdirectory : str
            Subdirectory of the root directory for Morph-RDB.

        """
        return __name__.lower()

    @timeout(TIMEOUT)
    def _execute_with_timeout(self, arguments) -> bool:
        """Execute a mapping with a provided timeout.

        Returns
        -------
        success : bool
            Whether the execution was successfull or not.
        """
        # Set Java heap to 1/2 of available memory instead of the default 1/4
        max_heap = int(psutil.virtual_memory().total * (1/2))

        # Execute command
        cmd = f'java -Xmx{max_heap} -Xms{max_heap} ' + \
              '-cp .:morph-rdb-dist-3.12.6.jar:dependency/* ' + \
              'es.upm.fi.dia.oeg.morph.r2rml.rdb.engine.MorphRDBRunner ' + \
              '/data config.properties'
        success = self.run_and_wait_for_exit(cmd)

        return success

    def execute(self, arguments: list) -> bool:
        """Execute Morph-KGC with the given arguments.

        Parameters
        ----------
        arguments : list
            Additional arguments to supply to Morph-KGC.

        Returns
        -------
        success : bool
            Whether the execution succeeded or not.
        """
        try:
            return self._execute_with_timeout(arguments)
        except TimeoutError:
            msg = f'Timeout ({TIMEOUT}s) reached for Morph-RDB'
            self._logger.warning(msg)

        return False

    def execute_mapping(self, mapping_file: str, output_file: str,
                        serialization: str, rdb_username: str,
                        rdb_password: str, rdb_host: str,
                        rdb_port: int, rdb_name: str,
                        rdb_type: str) -> bool:
        """Execute a mapping file with Morph-RDB.

        N-Quads and N-Triples are currently supported as serialization
        format for Morph-RDB. Only relational databases are supported by
        Morph-RDB, thus the relational database parameters are mandantory.

        Parameters
        ----------
        mapping_file : str
            Path to the mapping file to execute.
        output_file : str
            Name of the output file to store the triples in.
        serialization : str
            Serialization format to use.
        rdb_username : str
            Username for the database.
        rdb_password : str
            Password for the database.
        rdb_host : str
            Hostname for the database.
        rdb_port : int
            Port for the database.
        rdb_name : str
            Database name for the database.
        rdb_type : str
            Database type.

        Returns
        -------
        success : bool
            Whether the execution was successfull or not.
        """

        if serialization == 'nquads':
            serialization = 'N-QUADS'
        elif serialization == 'ntriples':
            serialization = 'N-TRIPLE'
        else:
            raise NotImplementedError('Unsupported serialization: '
                                      f'"{serialization}"')

        # Generate INI configuration file since no CLI is available
        config = configparser.ConfigParser()
        mapping_file = os.path.join('shared', os.path.basename(mapping_file))
        output_file = os.path.join('shared', os.path.basename(output_file))
        config['root'] = {
            'mappingdocument.file.path': mapping_file,
            'output.file.path': output_file,
            'output.rdflanguage': serialization,
        }

        config['root']['database.name[0]'] = rdb_name
        if rdb_type == 'MySQL':
            config['root']['database.driver[0]'] = 'com.mysql.jdbc.Driver'
            config['root']['database.type[0]'] = 'mysql'
            dsn = f'jdbc:mysql://{rdb_host}:{rdb_port}/{rdb_name}' + \
                  '?allowPublicKeyRetrieval=true&useSSL=false'
            config['root']['database.url[0]'] = dsn
        elif rdb_type == 'PostgreSQL':
            config['root']['database.driver[0]'] = 'org.postgresql.Driver'
            config['root']['database.type[0]'] = 'postgresql'
            dsn = f'jdbc:postgresql://{rdb_host}:{rdb_port}/{rdb_name}'
            config['root']['database.url[0]'] = dsn
        else:
            raise ValueError(f'Unknown RDB type: "{rdb_type}"')
        config['root']['database.user[0]'] = rdb_username
        config['root']['database.pwd[0]'] = rdb_password
        config['root']['no_of_database'] = '1'

        path = os.path.join(self._data_path, 'morphrdb')
        os.umask(0)
        os.makedirs(path, exist_ok=True)
        with open(os.path.join(path, 'config.properties'), 'w') as f:
            config.write(f, space_around_delimiters=False)

        # .properties files are like .ini files but without a [HEADER]
        # Use a [root] header and remove it after writing
        with open(os.path.join(path, 'config.properties'), 'r') as f:
            data = f.read()

        with open(os.path.join(path, 'config.properties'), 'w') as f:
            f.write(data.replace('[root]\n', ''))

        return self.execute([])
