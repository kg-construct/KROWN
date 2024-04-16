#!/usr/bin/env python3

"""
Virtuoso is a secure and high-performance platform for modern data access,
integration, virtualization, and multi-model data management (tables & graphs)
based on innovative support of existing open standards
(e.g., SQL, SPARQL, and GraphQL).

**Website**: https://virtuoso.openlinksw.com/<br>
**Repository**: https://github.com/openlink/virtuoso-opensource
"""

import os
import tempfile
import psutil
from typing import Dict
from threading import Thread
from bench_executor.container import Container
from bench_executor.logger import Logger

VERSION = '7.2.7'
MAX_ROWS = '10000000'
QUERY_TIMEOUT = '0'  # no limit
MAX_VECTOR_SIZE = '3000000'  # max value is 'around' 3,500,000 from docs
PASSWORD = 'root'
NUMBER_OF_BUFFERS_PER_GB = 85000
MAX_DIRTY_BUFFERS_PER_GB = 65000


def _spawn_loader(container):
    """Thread function to parallel load RDF.

    Parameters
    ----------
    container : Container
        The Virtuoso container on which the RDF loader should run.
    """
    success, logs = container.exec('\'isql\' -U dba -P root '
                                   'exec="rdf_loader_run();"')


class Virtuoso(Container):
    """Virtuoso container to execute SPARQL queries"""

    def __init__(self, data_path: str, config_path: str, directory: str,
                 verbose: bool):
        """Creates an instance of the Virtuoso class.

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

        tmp_dir = os.path.join(tempfile.gettempdir(), 'virtuoso')
        os.umask(0)
        os.makedirs(tmp_dir, exist_ok=True)
        os.makedirs(os.path.join(self._data_path, 'virtuoso'), exist_ok=True)
        number_of_buffers = int(psutil.virtual_memory().total / (10**9)
                                * NUMBER_OF_BUFFERS_PER_GB)
        max_dirty_buffers = int(psutil.virtual_memory().total / (10**9)
                                * MAX_DIRTY_BUFFERS_PER_GB)
        environment = {'DBA_PASSWORD': PASSWORD,
                       'VIRT_SPARQL_ResultSetMaxRows': MAX_ROWS,
                       'VIRT_SPARQL_MaxQueryExecutionTime': QUERY_TIMEOUT,
                       'VIRT_SPARQL_ExecutionTimeout': QUERY_TIMEOUT,
                       'VIRT_SPARQL_MaxQueryCostEstimationTime': QUERY_TIMEOUT,
                       'VIRT_Parameters_MaxVectorSize': MAX_VECTOR_SIZE,
                       'VIRT_Parameters_NumberOfBuffers': number_of_buffers,
                       'VIRT_Parameters_MaxDirtyBuffers': max_dirty_buffers}
        super().__init__(f'blindreviewing/virtuoso:v{VERSION}',
                         'Virtuoso', self._logger,
                         ports={'8890': '8890', '1111': '1111'},
                         environment=environment,
                         volumes=[f'{self._data_path}/shared:/usr/share/proj',
                                  f'{tmp_dir}:/database'])
        self._endpoint = 'http://localhost:8890/sparql'

    def initialization(self) -> bool:
        """Initialize Virtuoso's database.

        Returns
        -------
        success : bool
            Whether the initialization was successfull or not.
        """
        # Virtuoso should start with a initialized database, start Virtuoso
        # if not initialized to avoid the pre-run start during benchmark
        # execution
        success = self.wait_until_ready()
        if not success:
            return False
        success = self.stop()

        return success

    @property
    def root_mount_directory(self) -> str:
        """Subdirectory in the root directory of the case for Virtuoso.

        Returns
        -------
        subdirectory : str
            Subdirectory of the root directory for Virtuoso.
        """
        return __name__.lower()

    def wait_until_ready(self, command: str = '') -> bool:
        """Wait until Virtuoso is ready to execute SPARQL queries.

        Parameters
        ----------
        command : str
            Command to execute in the Virtuoso container, optionally, defaults
            to no command.

        Returns
        -------
        success : bool
            Whether the Virtuoso was initialized successfull or not.
        """
        return self.run_and_wait_for_log('Server online at', command=command)

    def load(self, rdf_file: str, rdf_dir: str = '') -> bool:
        """Load an RDF file into Virtuoso.

        Currently, only N-Triples files are supported.

        Parameters
        ----------
        rdf_file : str
            Name of the RDF file to load.
        rdf_dir : str
            Name of the directory where RDF file(s) are stored.
            Default root of the data directory.

        Returns
        -------
        success : bool
            Whether the loading was successfull or not.
        """
        return self.load_parallel(rdf_file, 1, rdf_dir)

    def load_parallel(self, rdf_file: str, cores: int,
                      rdf_dir: str = '') -> bool:
        """Load an RDF file into Virtuoso in parallel.

        Currently, only N-Triples files are supported.

        Parameters
        ----------
        rdf_file : str
            Name of the RDF file to load.
        cores : int
            Number of CPU cores for loading.
        rdf_dir : str
            Name of the directory where RDF file(s) are stored.
            Default root of the data directory.

        Returns
        -------
        success : bool
            Whether the loading was successfull or not.
        """
        success = True

        success, logs = self.exec(f'sh -c "ls /usr/share/proj/{rdf_file}"')
        for line in logs:
            self._logger.debug(line)
        if not success:
            self._logger.error('RDF files do not exist for loading')
            return False

        # Load directory with data
        directory = f'/usr/share/proj/{rdf_dir}'
        success, logs = self.exec('\'isql\' -U dba -P root '
                                  f'exec="ld_dir(\'{directory}\','
                                  f'\'{rdf_file}\', '
                                  '\'http://example.com/graph\');"')
        for line in logs:
            self._logger.debug(line)
        if not success:
            self._logger.error('ISQL loader query failure')
            return False

        loader_threads = []
        self._logger.debug(f'Spawning {cores} loader threads')
        for i in range(cores):
            t = Thread(target=_spawn_loader, args=(self,), daemon=True)
            t.start()
            loader_threads.append(t)

        for t in loader_threads:
            t.join()
        self._logger.debug(f'Loading finished with {cores} threads')

        # Re-enable checkpoints and scheduler which are disabled automatically
        # after loading RDF with rdf_loader_run()
        success, logs = self.exec('\'isql\' -U dba -P root exec="checkpoint;"')
        for line in logs:
            self._logger.debug(line)
        if not success:
            self._logger.error('ISQL re-enable checkpoints query failure')
            return False

        success, logs = self.exec('\'isql\' -U dba -P root '
                                  'exec="checkpoint_interval(60);"')
        for line in logs:
            self._logger.debug(line)
        if not success:
            self._logger.error('ISQL checkpoint interval query failure')
            return False

        success, logs = self.exec('\'isql\' -U dba -P root '
                                  'exec="scheduler_interval(10);"')
        for line in logs:
            self._logger.debug(line)
        if not success:
            self._logger.error('ISQL scheduler interval query failure')
            return False

        return success

    def stop(self) -> bool:
        """Stop Virtuoso.

        Drops all triples in Virtuoso before stopping its container.

        Returns
        -------
        success : bool
            Whether stopping Virtuoso was successfull or not.
        """
        # Drop loaded triples
        success, logs = self.exec('\'isql\' -U dba -P root '
                                  'exec="delete from DB.DBA.load_list;"')
        for line in logs:
            self._logger.debug(line)
        if not success:
            self._logger.error('ISQL delete load list query failure')
            return False

        success, logs = self.exec('\'isql\' -U dba -P root '
                                  'exec="rdf_global_reset();"')
        for line in logs:
            self._logger.debug(line)
        if not success:
            self._logger.error('ISQL RDF global reset query failure')
            return False
        return super().stop()

    @property
    def endpoint(self) -> str:
        """SPARQL endpoint URL"""
        return self._endpoint

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
        headers['ntriples'] = {'Accept': 'text/ntriples'}
        headers['turtle'] = {'Accept': 'text/turtle'}
        headers['rdfxml'] = {'Accept': 'application/rdf+xml'}
        headers['rdfjson'] = {'Accept': 'application/rdf+json'}
        headers['csv'] = {'Accept': 'text/csv'}
        headers['jsonld'] = {'Accept': 'application/ld+json'}
        return headers


if __name__ == '__main__':
    print(f'ℹ️  Starting up Virtuoso v{VERSION}...')
    v = Virtuoso('data', 'config', 'log', True)
    v.wait_until_ready()
    input('ℹ️  Press any key to stop')
    v.stop()
    print('ℹ️  Stopped')
