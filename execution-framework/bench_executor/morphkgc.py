#!/usr/bin/env python3

"""
Morph-KGC is an engine that constructs RDF and RDF-star knowledge graphs
from heterogeneous data sources with the R2RML, RML and RML-star mapping
languages.

**Website**: https://morph-kgc.readthedocs.io/<br>
**Repository**: https://github.com/oeg-upm/morph-kgc
"""

import os
import configparser
from timeout_decorator import timeout, TimeoutError  # type: ignore
from typing import Optional
from bench_executor.container import Container
from bench_executor.logger import Logger

VERSION = '2.2.0'
TIMEOUT = 6 * 3600  # 6 hours


class MorphKGC(Container):
    """Morph-KGC container for executing R2RML, RML, and RML-star mappings."""
    def __init__(self, data_path: str, config_path: str, directory: str,
                 verbose: bool):
        """Creates an instance of the MorphKGC class.

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
        os.makedirs(os.path.join(self._data_path, 'morphkgc'), exist_ok=True)
        super().__init__(f'blindreviewing/morph-kgc:v{VERSION}', 'Morph-KGC',
                         self._logger,
                         volumes=[f'{self._data_path}/morphkgc:/data',
                                  f'{self._data_path}/shared:/data/shared'])

    @property
    def root_mount_directory(self) -> str:
        """Subdirectory in the root directory of the case for Morph-KGC.

        Returns
        -------
        subdirectory : str
            Subdirectory of the root directory for Morph-KGC.

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
        cmd = 'python3 -m morph_kgc /data/config_morphkgc.ini'
        success = self.run_and_wait_for_exit(cmd)

        return success

    def execute(self, arguments: list) -> bool:
        """Execute Morph-KGC with given arguments.

        Parameters
        ----------
        arguments : list
            Arguments to supply to Morph-KGC.

        Returns
        -------
        success : bool
            Whether the execution succeeded or not.
        """
        try:
            return self._execute_with_timeout(arguments)
        except TimeoutError:
            msg = f'Timeout ({TIMEOUT}s) reached for Morph-KGC'
            self._logger.warning(msg)

        return False

    def execute_mapping(self,
                        mapping_file: str,
                        output_file: str,
                        serialization: str,
                        rdb_username: Optional[str] = None,
                        rdb_password: Optional[str] = None,
                        rdb_host: Optional[str] = None,
                        rdb_port: Optional[int] = None,
                        rdb_name: Optional[str] = None,
                        rdb_type: Optional[str] = None,
                        multiple_files: bool = False) -> bool:
        """Execute a mapping file with Morph-KGC.

        Morph-KGC can transform SQL relational databases (MySQL, PostgreSQL,
        Oracle, Microsoft SQL Server, MariaDB, SQLite), tabular (CSV, TSV,
        Excel, Parquet, Feather, ORC, Stata, SAS, SPSS, ODS) and
        hierarchical files (JSON, XML).

        Morph-KGC currently only supports N-Quads and N-Triples in RDF and
        RDF-Star. RDF and RDF-Star output is done automatically, you can use
        the same serialization format (`ntriples`, `nquads`) for both RDF
        and RDF-Star output.

        Morph-KGC can generate all triples in a single file or spread it
        among multiple files.

        Parameters
        ----------
        mapping_file : str
            Path to the mapping file to execute.
        output_file : str
            Name of the output file to store the triples in.
        serialization : str
            Serialization format to use.
        rdb_username : Optional[str]
            Username for the database, required when a database is used as
            source.
        rdb_password : Optional[str]
            Password for the database, required when a database is used as
            source.
        rdb_host : Optional[str]
            Hostname for the database, required when a database is used as
            source.
        rdb_port : Optional[int]
            Port for the database, required when a database is used as source.
        rdb_name : Optional[str]
            Database name for the database, required when a database is used as
            source.
        rdb_type : Optional[str]
            Database type, required when a database is used as source.
        multiple_files : bool
            If the generated triples must be stored in multiple files, default
            a single file.

        Returns
        -------
        success : bool
            Whether the execution was successfull or not.
        """

        if serialization == 'nquads':
            serialization = 'N-QUADS'
        elif serialization == 'ntriples':
            serialization = 'N-TRIPLES'
        else:
            raise NotImplementedError('Unsupported serialization:'
                                      f'"{serialization}"')

        # Generate INI configuration file since no CLI is available
        config = configparser.ConfigParser()
        config['CONFIGURATION'] = {
            'output_format': serialization
        }
        config['DataSource0'] = {
            'mappings': f'/data/shared/{mapping_file}'
        }

        # Morph-KGC can keep the mapping partition results separate, provide
        # this option, default OFF
        if multiple_files:
            config['CONFIGURATION']['output_dir'] = '/data/shared/'
        else:
            config['CONFIGURATION']['output_file'] = \
                    f'/data/shared/{output_file}'

        if rdb_username is not None and rdb_password is not None \
                and rdb_host is not None and rdb_port is not None \
                and rdb_name is not None and rdb_type is not None:
            if rdb_type == 'MySQL':
                protocol = 'mysql+pymysql'
            elif rdb_type == 'PostgreSQL':
                protocol = 'postgresql+psycopg2'
            else:
                raise ValueError(f'Unknown RDB type: "{rdb_type}"')
            rdb_dsn = f'{protocol}://{rdb_username}:{rdb_password}' + \
                      f'@{rdb_host}:{rdb_port}/{rdb_name}'
            config['DataSource0']['db_url'] = rdb_dsn

        os.umask(0)
        os.makedirs(os.path.join(self._data_path, 'morphkgc'), exist_ok=True)
        path = os.path.join(self._data_path, 'morphkgc', 'config_morphkgc.ini')
        with open(path, 'w') as f:
            config.write(f)

        return self.execute([])
