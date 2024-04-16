#!/usr/bin/env python3

"""
The RMLStreamer executes RML rules to generate high quality Linked Data
from multiple originally (semi-)structured data sources in a streaming way.

**Website**: https://rml.io<br>
**Repository**: https://github.com/RMLio/RMLStreamer
"""

import os
import errno
import shutil
import psutil
from glob import glob
from typing import Optional
from timeout_decorator import timeout, TimeoutError  # type: ignore
from rdflib import Graph, BNode, Namespace, Literal, RDF
from bench_executor.container import Container
from bench_executor.logger import Logger
R2RML = Namespace('http://www.w3.org/ns/r2rml#')
RML = Namespace('http://semweb.mmlab.be/ns/rml#')
D2RQ = Namespace('http://www.wiwiss.fu-berlin.de/suhl/bizer/D2RQ/0.1#')

VERSION = '2.5.0'  # standalone mode with RDB support
TIMEOUT = 6 * 3600  # 6 hours
IMAGE = f'blindreviewing/rmlstreamer:v{VERSION}'


class RMLStreamer(Container):
    """RMLStreamer container for executing RML mappings."""

    def __init__(self, data_path: str, config_path: str, directory: str,
                 verbose: bool):
        """Creates an instance of the RMLStreamer class.

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
        super().__init__(IMAGE, 'RMLStreamer', self._logger,
                         volumes=[f'{self._data_path}/rmlstreamer:/data',
                                  f'{self._data_path}/shared:/data/shared'])

    @property
    def root_mount_directory(self) -> str:
        """Subdirectory in the root directory of the case for RMLStreamer.

        Returns
        -------
        subdirectory : str
            Subdirectory of the root directory for RMLStreamer.

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
        # Set Java heap to 50% of available memory instead of the default 1/4
        max_heap = int(psutil.virtual_memory().total * 0.5)

        # Execute command
        cmd = f'java -Xmx{max_heap} -Xms{max_heap}' + \
              ' -jar /rmlstreamer/rmlstreamer.jar'
        cmd += f' {" ".join(arguments)}'

        self._logger.debug(f'Executing RMLStreamer with arguments '
                           f'{" ".join(arguments)}')

        return self.run_and_wait_for_exit(cmd)

    def execute(self, arguments: list) -> bool:
        """Execute RMLStreamer with given arguments.

        Parameters
        ----------
        arguments : list
            Arguments to supply to RMLStreamer.

        Returns
        -------
        success : bool
            Whether the execution succeeded or not.
        """
        try:
            return self._execute_with_timeout(arguments)
        except TimeoutError:
            msg = f'Timeout ({TIMEOUT}s) reached for RMLStreamer'
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
        """Execute a mapping file with RMLStreamer.

        N-Quads/N-Triples is the only currently supported as serialization
        format for RMLStreamer.

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
        arguments = ['toFile', ' ',
                     '-o', '/data/output']
        mapping_file = os.path.join('/data/shared/', mapping_file)

        if rdb_username is not None and rdb_password is not None \
                and rdb_host is not None and rdb_port is not None \
                and rdb_name is not None and rdb_type is not None:
            if rdb_type == 'MySQL':
                driver = 'jdbc:mysql'
            elif rdb_type == 'PostgreSQL':
                driver = 'jdbc:postgresql'
            else:
                raise NotImplementedError('RMLStreamer does not support RDB '
                                          f'"{rdb_type}"')
            dsn = f'{driver}://{rdb_host}:{rdb_port}/{rdb_name}'

            # Compatibility with R2RML mapping files
            # Replace rr:logicalTable with rml:logicalSource + D2RQ description
            # and rr:column with rml:reference
            g = Graph()
            g.bind('rr', R2RML)
            g.bind('rml', RML)
            g.bind('d2rq', D2RQ)
            g.bind('rdf', RDF)
            g.parse(os.path.join(self._data_path, 'shared',
                                 os.path.basename(mapping_file)))

            # rr:logicalTable --> rml:logicalSource
            for triples_map_iri, p, o in g.triples((None, RDF.type,
                                                    R2RML.TriplesMap)):
                logical_source_iri = BNode()
                d2rq_rdb_iri = BNode()
                logical_table_iri = g.value(triples_map_iri,
                                            R2RML.logicalTable)
                if logical_table_iri is None:
                    break

                table_name_literal = g.value(logical_table_iri,
                                             R2RML.tableName)
                if table_name_literal is None:
                    break

                g.add((d2rq_rdb_iri, D2RQ.jdbcDSN, Literal(dsn)))
                g.add((d2rq_rdb_iri, D2RQ.jdbcDriver, Literal(driver)))
                g.add((d2rq_rdb_iri, D2RQ.username, Literal(rdb_username)))
                g.add((d2rq_rdb_iri, D2RQ.password, Literal(rdb_password)))
                g.add((d2rq_rdb_iri, RDF.type, D2RQ.Database))
                g.add((logical_source_iri, R2RML.sqlVersion, R2RML.SQL2008))
                g.add((logical_source_iri, R2RML.tableName,
                       table_name_literal))
                g.add((logical_source_iri, RML.source, d2rq_rdb_iri))
                g.add((logical_source_iri, RDF.type, RML.LogicalSource))
                g.add((triples_map_iri, RML.logicalSource, logical_source_iri))
                g.remove((triples_map_iri, R2RML.logicalTable,
                          logical_table_iri))
                g.remove((logical_table_iri, R2RML.tableName,
                          table_name_literal))
                g.remove((logical_table_iri, RDF.type, R2RML.LogicalTable))
                g.remove((logical_table_iri, R2RML.sqlVersion, R2RML.SQL2008))

            # rr:column --> rml:reference
            for s, p, o in g.triples((None, R2RML.column, None)):
                g.add((s, RML.reference, o))
                g.remove((s, p, o))

            mapping_file = os.path.join('/', 'data',
                                        'mapping_converted.rml.ttl')
            destination = os.path.join(self._data_path, 'rmlstreamer',
                                       'mapping_converted.rml.ttl')
            g.serialize(destination=destination, format='turtle')

        arguments.append('-m')
        arguments.append(mapping_file)

        os.makedirs(os.path.join(self._data_path, 'rmlstreamer', 'output'),
                    exist_ok=True)
        status_code = self.execute(arguments)

        # Combine all output into a single file.
        # Duplicates may exist because RMLStreamer does not support duplicate
        # removal
        output_path = os.path.join(self._data_path, 'shared', output_file)
        try:
            os.remove(output_path)
        except OSError as e:
            if e.errno != errno.ENOENT:
                raise

        with open(output_path, 'a') as out_file:
            files = list(glob(os.path.join(self._data_path, 'rmlstreamer',
                                           'output', '.*')))
            files += list(glob(os.path.join(self._data_path, 'rmlstreamer',
                                            'output', '*')))
            for gen_file in files:
                with open(gen_file, 'r') as f:
                    out_file.write(f.read())

        shutil.rmtree(os.path.join(self._data_path, 'rmlstreamer', 'output'),
                      ignore_errors=True)

        return status_code
