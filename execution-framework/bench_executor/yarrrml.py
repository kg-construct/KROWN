#!/usr/bin/env python3

"""
YARRRML is a human readable text-based representation for declarative
Linked Data generation rules.

**Website**: https://rml.io/yarrrml/<br>
**Repository**: https://github.com/RMLio/yarrrml-parser
"""

import os
from bench_executor.container import Container
from bench_executor.logger import Logger

VERSION = '1.3.6'


class YARRRML(Container):
    """YARRRML container to transform YARRRML mappings into RML mappings."""

    def __init__(self, data_path: str, config_path: str, directory: str,
                 verbose: bool):
        """Creates an instance of the YARRRML class.

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

        os.makedirs(os.path.join(self._data_path, 'yarrrml'), exist_ok=True)
        super().__init__(f'blindreviewing/yarrrml:v{VERSION}', 'YARRRML',
                         self._logger,
                         volumes=[f'{self._data_path}/yarrrml:/data',
                                  f'{self._data_path}/shared:/data/shared'])

    @property
    def root_mount_directory(self) -> str:
        """Subdirectory in the root directory of the case for YARRRML.

        Returns
        -------
        subdirectory : str
            Subdirectory of the root directory for YARRRML.
        """
        return __name__.lower()

    def transform_mapping(self, yarrrml_file: str, mapping_file: str,
                          r2rml: bool = False, pretty: bool = True) -> bool:
        """Transform a YARRRML mapping into a RML mapping.

        Parameters
        ----------
        yarrrml_file : str
            Name of the YARRRML mapping file.
        mapping_file : str
            Name of the RML mapping file.
        r2rml : bool
            Whether the RML mapping file must be R2RML compatible.
        pretty : bool
            Whether the generated mapping file must be pretty or not.

        Returns
        -------
        success : bool
            Whether the YARRRML was initialized successfull or not.
        """
        arguments = ['-i', os.path.join('/data/shared/', yarrrml_file),
                     '-o', os.path.join('/data/shared/', mapping_file)]

        if r2rml:
            arguments.append('-c')
            arguments.append('-f R2RML')

        if pretty:
            arguments.append('-p')

        self._logger.debug(f'Executing YARRRML with arguments '
                           f'"{" ".join(arguments)}"\n')

        cmd = f'{" ".join(arguments)}'
        success = self.run_and_wait_for_exit(cmd)
        return success
