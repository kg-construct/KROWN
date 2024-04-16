#!/usr/bin/env python3

"""
The RMLMapper executes RML rules to generate high quality Linked Data
from multiple originally (semi-)structured data sources.

**Website**: https://rml.io<br>
**Repository**: https://github.com/RMLio/rmlmapper-java
"""

import os
import psutil
from typing import Optional
from timeout_decorator import timeout, TimeoutError  # type: ignore
from bench_executor.container import Container
from bench_executor.logger import Logger

VERSION = '6.0.0'
TIMEOUT = 6 * 3600  # 6 hours


class RMLMapperDocker(Container):
    """RMLMapper container for executing R2RML and RML mappings."""

    def __init__(self, data_path: str, config_path: str, directory: str,
                 verbose: bool):
        """Creates an instance of the RMLMapper class.

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
        self._verbose = verbose

        os.makedirs(os.path.join(self._data_path, 'rmlmapper'), exist_ok=True)
        super().__init__(f'blindreviewing/rmlmapper:v{VERSION}', 'RMLMapper',
                         self._logger,
                         volumes=[f'{self._data_path}/rmlmapper:/data',
                                  f'{self._data_path}/shared:/data/shared'])

    @property
    def root_mount_directory(self) -> str:
        """Subdirectory in the root directory of the case for RMLMapper.

        Returns
        -------
        subdirectory : str
            Subdirectory of the root directory for RMLMapper.

        """
        return __name__.lower()

    @timeout(TIMEOUT)
    def _execute_with_timeout(self, arguments: list) -> bool:
        """Execute a mapping with a provided timeout.

        Returns
        -------
        success : bool
            Whether the execution was successfull or not.
        """
        # Set Java heap to 1/2 of available memory instead of the default 1/4
        max_heap = int(psutil.virtual_memory().total * (1/2))

        # Execute command
        cmd = f'java -Xmx{max_heap} -Xms{max_heap}' + \
              ' -jar /rmlmapper/rmlmapper.jar'
        if self._verbose:
            cmd += ' -vvvvvvvvvvvvv'
        cmd += f' {" ".join(arguments)}'

        self._logger.debug(f'Executing RMLMapper with arguments '
                           f'{" ".join(arguments)}')

        return self.run_and_wait_for_exit(cmd)

    def execute(self, arguments: list) -> bool:
        """Execute RMLMapper with given arguments.

        Parameters
        ----------
        arguments : list
            Arguments to supply to RMLMapper.

        Returns
        -------
        success : bool
            Whether the execution succeeded or not.
        """
        try:
            return self._execute_with_timeout(arguments)
        except TimeoutError:
            msg = f'Timeout ({TIMEOUT}s) reached for RMLMapper'
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
                        rdb_type: Optional[str] = None) -> bool:
        """Execute a mapping file with RMLMapper.

        N-Quads and N-Triples are currently supported as serialization
        format for RMLMapper.

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

        Returns
        -------
        success : bool
            Whether the execution was successfull or not.
        """
        arguments = ['-m', os.path.join('/data/shared/', mapping_file),
                     '-s', serialization,
                     '-o', os.path.join('/data/shared/', output_file),
                     '-d']  # Enable duplicate removal

        if rdb_username is not None and rdb_password is not None \
                and rdb_host is not None and rdb_port is not None \
                and rdb_name is not None and rdb_type is not None:

            arguments.append('-u')
            arguments.append(rdb_username)
            arguments.append('-p')
            arguments.append(rdb_password)

            parameters = ''
            if rdb_type == 'MySQL':
                protocol = 'jdbc:mysql'
                parameters = '?allowPublicKeyRetrieval=true&useSSL=false'
            elif rdb_type == 'PostgreSQL':
                protocol = 'jdbc:postgresql'
            else:
                raise ValueError(f'Unknown RDB type: "{rdb_type}"')
            rdb_dsn = f'\'{protocol}://{rdb_host}:{rdb_port}/' + \
                      f'{rdb_name}{parameters}\''
            arguments.append('-dsn')
            arguments.append(rdb_dsn)

        return self.execute(arguments)
