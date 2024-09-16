"""
The Souffle reasoner.
"""

import os
import psutil
from typing import Optional
from timeout_decorator import timeout, TimeoutError  # type: ignore
from bench_executor.container import Container
from bench_executor.logger import Logger

VERSION = '1.0.0'
TIMEOUT = 1 * 3600  # 6 hours


class Souffle(Container):
    """Souffle container for executing R2RML and RML mappings."""

    def __init__(self, data_path: str, config_path: str, directory: str,
                 verbose: bool):
        """Creates an instance of the Souffle class.

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
        
        os.makedirs(os.path.join(self._data_path, 'souffle'), exist_ok=True)
        super().__init__(f'alloka/souffle:v{VERSION}', 'Souffle',
                         self._logger,
                         volumes=[f'{self._data_path}/souffle:/data',
                                  f'{self._data_path}/shared:/data/shared'])
        print('INIT')

    @property
    def root_mount_directory(self) -> str:
        """Subdirectory in the root directory of the case for Souffle.

        Returns
        -------
        subdirectory : str
            Subdirectory of the root directory for Souffle.

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
        self._logger.info(f'Executing Souffle with arguments '
                          f'{" ".join(arguments)}')

        # Execute command
        cmd = f'./bin/souffle -c -j 12 ' + \
              f'{"".join(arguments)}'
        return self.run_and_wait_for_exit(cmd)

    def execute(self, arguments: list) -> bool:
        """Execute Souffle with given arguments.

        Parameters
        ----------
        arguments : list
            Arguments to supply to Souffle.

        Returns
        -------
        success : bool
            Whether the execution succeeded or not.
        """
        try:
            return self._execute_with_timeout(arguments)
        except TimeoutError:
            msg = f'Timeout ({TIMEOUT}s) reached for Souffle'
            self._logger.warning(msg)

        return False

    def execute_mapping(self, mapping_file: str, output_file: str) -> bool:
        """Execute a First Order Logic mapping file with Souffle.

        Parameters
        ----------
        mapping_file : str
            Path to the mapping file to convert.
        output_file : str
            Name of the output file to store generated triples in.

        Returns
        -------
        success : bool
            Whether the execution was successfull or not.
        """
        arguments = ['', os.path.join('/data/shared/', mapping_file),
                     ' -D', '/data/shared/']  # Output directory

        print(arguments)

        return self.execute(arguments)
