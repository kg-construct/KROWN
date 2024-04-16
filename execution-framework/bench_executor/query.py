#!/usr/bin/env python3

"""
Query executes SPARQL queries on endpoints by posting the SPARQL query over
HTTP onto the endpoint. It applies timeouts to these queries automatically and
checks if the results are empty or not.
"""

import os
import requests
from typing import Optional
from timeout_decorator import timeout, TimeoutError  # type: ignore
from bench_executor.logger import Logger

TIMEOUT = 1 * 3600  # 1 hour


class Query():
    """Execute a query on a SPARQL endpoint."""
    def __init__(self, data_path: str, config_path: str, directory: str,
                 verbose: bool):
        """Creates an instance of the Query class.

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
        os.makedirs(os.path.join(self._data_path, 'query'), exist_ok=True)

    @property
    def name(self):
        """Name of the class: Query"""
        return __name__

    @property
    def root_mount_directory(self) -> str:
        """Subdirectory in the root directory of the case for Query.

        Returns
        -------
        subdirectory : str
            Subdirectory of the root directory for Query.

        """
        return __name__.lower()

    @timeout(TIMEOUT)
    def _execute_with_timeout(self, query: str, sparql_endpoint: str,
                              headers: dict = {}) -> str:
        """Execute a query with a provided timeout.

        Parameters
        ----------
        query : str
            The query to execute.
        sparql_endpoint : str
            The URL of the SPARQL endpoint.
        headers : dict
            HTTP headers to supply when posting the query.

        Returns
        -------
        success : bool
            Whether the execution was successfull or not.
        """
        self._logger.info(f'Executing query "{query}" on endpoint '
                          f'"{sparql_endpoint}"')
        data = {
            'query': query,
            'maxrows': '3000000'  # Overwrite Virtuoso SPARQL limit
        }
        # Hardcoded to N-Triples
        r = requests.post(sparql_endpoint, data=data, headers=headers)
        if r.status_code != 200:
            msg = f'Query failed: {r.text} (HTTP {r.status_code})'
            self._logger.error(msg)
        r.raise_for_status()
        return r.text

    def _execute(self, query: str, sparql_endpoint: str, expect_empty: bool,
                 headers: dict = {}) -> Optional[str]:
        """Execute a query on a SPARQL endpoint

        Parameters
        ----------
        query : str
            The query to execute.
        sparql_endpoint : str
            The URL of the SPARQL endpoint.
        expect_empty : bool
            Whether the expected results are empty or not.
        headers : dict
            HTTP headers to supply when posting the query.

        Returns
        -------
        results : str
            The HTTP response as string of the SPARQL endpoint, unless it has
            no results.
        """
        results = None
        try:
            results = self._execute_with_timeout(query,
                                                 sparql_endpoint,
                                                 headers)
        except TimeoutError:
            msg = f'Timeout ({TIMEOUT}s) reached for Query: "{query}"'
            self._logger.warning(msg)

        # Check results output
        if results is None or not results or 'Empty' in results:
            if expect_empty:
                self._logger.info('No results found, but was expected!')
                return None

            self._logger.error('No results found!')
            return None

        return results

    def execute_and_save(self, query: str, sparql_endpoint: str,
                         results_file: str, expect_empty: bool = False,
                         headers: dict = {}) -> bool:
        """Executes a SPARQL query and save the results.

        The results are saved to the `results_file` path.

        Parameters
        ----------
        query : str
            The query to execute.
        sparql_endpoint : str
            The URL of the SPARQL endpoint.
        results_file : str
            Path to the file where the results may be stored.
        expect_empty : bool
            Whether the expected results are empty or not.
        headers : dict
            HTTP headers to supply when posting the query.

        Returns
        -------
        success : bool
            Whether the execution succeeded or not.
        """
        try:
            results = self._execute(query, sparql_endpoint, expect_empty,
                                    headers)
        except Exception as e:
            msg = f'Failed to execute query "{query}" on endpoint ' + \
                  f'"{sparql_endpoint}": {e}'
            self._logger.error(msg)
            return False

        path = os.path.join(self._data_path, 'shared')
        os.umask(0)
        os.makedirs(path, exist_ok=True)

        if results is not None:
            results_file = os.path.join(path, results_file)
            with open(results_file, 'w') as f:
                f.write(results)

            self._logger.debug(f'Wrote query results to "{results_file}"')
            self._logger.debug('Query results:')
            self._logger.debug(results)
            return True

        return False

    def _read_query_file(self, query_file: str) -> str:
        """Read the query file

        Returns
        -------
        content : str
            The content of the query file.

        Raises
        ------
        FileNotFoundError : Exception
            If the query file cannot be found.
        """
        path = os.path.join(self._data_path, 'shared', query_file)
        if not os.path.exists(path):
            msg = f'Query file "{path}" does not exist'
            self._logger.error(msg)
            raise FileNotFoundError(msg)

        with open(path, 'r') as f:
            query = f.read()

        return query

    def execute_from_file(self, query_file: str, sparql_endpoint: str,
                          expect_empty: bool = False,
                          headers: dict = {}) -> str:
        """Executes a SPARQL query from file.

        The results are saved to the `results_file` path.

        Parameters
        ----------
        query_file : str
            Path to the file containing the query.
        sparql_endpoint : str
            The URL of the SPARQL endpoint.
        expect_empty : bool
            Whether the expected results are empty or not.
        headers : dict
            HTTP headers to supply when posting the query.

        Returns
        -------
        results : str
            The HTTP response as string of the SPARQL endpoint, unless it has
            no results.

        Raises
        ------
        Exception : Exception
            Pass through the exception from the Python's request module
            regarding HTTP status codes.
        """
        query = self._read_query_file(query_file)
        try:
            results = self._execute(query, sparql_endpoint, expect_empty,
                                    headers)
        except Exception as e:
            msg = f'Failed to execute query "{query}" on endpoint ' + \
                  f'"{sparql_endpoint}": {e}'
            self._logger.error(msg)
            raise e

        if results is not None:
            return results

        return ''

    def execute_from_file_and_save(self, query_file: str,
                                   sparql_endpoint: str,
                                   results_file: str,
                                   expect_empty: bool = False,
                                   headers: dict = {}) -> bool:
        """Executes a SPARQL query from file and save the results.

        The results are saved to the `results_file` path.

        Parameters
        ----------
        query_file : str
            Path to the file containing the query.
        sparql_endpoint : str
            The URL of the SPARQL endpoint.
        results_file : str
            Path to the file where the results may be stored.
        expect_empty : bool
            Whether the expected results are empty or not.
        headers : dict
            HTTP headers to supply when posting the query.

        Returns
        -------
        success : bool
            Whether the execution succeeded or not.

        Raises
        ------
        FileNotFoundError : Exception
            If the query file cannot be found.
        """
        query = self._read_query_file(query_file)
        results = self.execute_and_save(query, sparql_endpoint, results_file,
                                        expect_empty, headers)
        if results is not None:
            return True

        return False
