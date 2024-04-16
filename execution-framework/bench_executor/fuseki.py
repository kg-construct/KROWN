#!/usr/bin/env python3

"""
Apache Jena Fuseki is a SPARQL server. It can run as an operating system
service, as a Java web application (WAR file), and as a standalone server.

**Website**: https://jena.apache.org/documentation/fuseki2/
"""

import os
import requests
import psutil
from typing import Dict
from bench_executor.container import Container
from bench_executor.logger import Logger

VERSION = '4.6.1'
CMD_ARGS = '--tdb2 --update --loc /fuseki/databases/DB /ds'


class Fuseki(Container):
    """Fuseki container for executing SPARQL queries."""
    def __init__(self, data_path: str, config_path: str, directory: str,
                 verbose: bool):
        """Creates an instance of the Fuseki class.

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
        os.makedirs(os.path.join(self._data_path, 'fuseki'), exist_ok=True)

        # Set Java heap to 1/2 of available memory instead of the default 1/4
        max_heap = int(psutil.virtual_memory().total * (1/2))

        super().__init__(f'blindreviewing/fuseki:v{VERSION}', 'Fuseki',
                         self._logger,
                         ports={'3030': '3030'},
                         environment={
                             'JAVA_OPTIONS': f'-Xmx{max_heap} -Xms{max_heap}'
                         },
                         volumes=[f'{self._config_path}/fuseki/'
                                  f'log4j2.properties:/fuseki/'
                                  f'log4j2.properties',
                                  f'{self._data_path}/shared:/data',
                                  f'{self._data_path}/fuseki:'
                                  '/fuseki/databases/DB'])
        self._endpoint = 'http://localhost:3030/ds/sparql'

    def initialization(self) -> bool:
        """Initialize Fuseki's database.

        Returns
        -------
        success : bool
            Whether the initialization was successfull or not.
        """
        # Fuseki should start with a initialized database, start Fuseki
        # if not initialized to avoid the pre-run start during benchmark
        # execution
        success = self.wait_until_ready()
        if not success:
            return False
        success = self.stop()

        return success

    @property
    def root_mount_directory(self) -> str:
        """Subdirectory in the root directory of the case for Fuseki.

        Returns
        -------
        subdirectory : str
            Subdirectory of the root directory for Fuseki.
        """
        return __name__.lower()

    @property
    def headers(self) -> Dict[str, Dict[str, str]]:
        """HTTP headers of SPARQL queries for serialization formats.

        Only supported serialization formats are included in the dictionary.
        Currently, the following formats are supported:
        - N-Triples
        - Turtle
        - CSV
        - RDF/JSON
        - RDF/XML
        - JSON-LD

        Returns
        -------
        headers : dict
            Dictionary of headers to use for each serialization format.
        """
        headers = {}
        headers['ntriples'] = {'Accept': 'text/plain'}
        headers['turtle'] = {'Accept': 'text/turtle'}
        headers['csv'] = {'Accept': 'text/csv'}
        headers['rdfjson'] = {'Accept': 'application/rdf+json'}
        headers['rdfxml'] = {'Accept': 'application/rdf+xml'}
        headers['jsonld'] = {'Accept': 'application/ld+json'}
        return headers

    def wait_until_ready(self, command: str = '') -> bool:
        """Wait until Fuseki is ready to execute SPARQL queries.

        Parameters
        ----------
        command : str
            Command to execute in the Fuseki container, optionally, defaults to
            no command.

        Returns
        -------
        success : bool
            Whether the Fuseki was initialized successfull or not.
        """
        command = f'{command} {CMD_ARGS}'
        return self.run_and_wait_for_log(':: Start Fuseki ', command=command)

    def load(self, rdf_file: str) -> bool:
        """Load an RDF file into Fuseki.

        Currently, only N-Triples files are supported.

        Parameters
        ----------
        rdf_file : str
            Name of the RDF file to load.

        Returns
        -------
        success : bool
            Whether the loading was successfull or not.
        """
        path = os.path.join(self._data_path, 'shared', rdf_file)

        if not os.path.exists(path):
            self._logger.error(f'RDF file "{rdf_file}" does not exist')
            return False

        # Load directory with data with HTTP post
        try:
            h = {'Content-Type': 'application/n-triples'}
            r = requests.post('http://localhost:3030/ds',
                              data=open(path, 'rb'),
                              headers=h)
            self._logger.debug(f'Loaded triples: {r.text}')
            r.raise_for_status()
        except Exception as e:
            self._logger.error(f'Failed to load RDF: "{e}" into Fuseki')
            return False

        return True

    def stop(self) -> bool:
        """Stop Fuseki.

        Drops all triples in Fuseki before stopping its container.

        Returns
        -------
        success : bool
            Whether stopping Fuseki was successfull or not.
        """
        # Drop triples on exit
        try:
            headers = {'Content-Type': 'application/sparql-update'}
            data = 'DELETE { ?s ?p ?o . } WHERE { ?s ?p ?o . }'
            r = requests.post('http://localhost:3030/ds/update',
                              headers=headers, data=data)
            self._logger.debug(f'Dropped triples: {r.text}')
            r.raise_for_status()
        except Exception as e:
            self._logger.error(f'Failed to drop RDF: "{e}" from Fuseki')
            return False

        return super().stop()

    @property
    def endpoint(self):
        """SPARQL endpoint URL"""
        return self._endpoint


if __name__ == '__main__':
    print(f'ℹ️  Starting up Fuseki v{VERSION}...')
    f = Fuseki('data', 'config', 'log', True)
    f.wait_until_ready()
    input('ℹ️  Press any key to stop')
    f.stop()
    print('ℹ️  Stopped')
