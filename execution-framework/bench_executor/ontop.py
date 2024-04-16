#!/usr/bin/env python3

"""
Ontop is a Virtual Knowledge Graph system. It exposes the content of
arbitrary relational databases as knowledge graphs. These graphs are virtual,
which means that data remains in the data sources instead of being moved
to another database.

**Website**: https://ontop-vkg.org<br>
**Repository**: https://github.com/ontop/ontop
"""

import os
import psutil
import configparser
from rdflib import Graph, Namespace, RDF, URIRef
from timeout_decorator import timeout, TimeoutError  # type: ignore
from typing import Dict, Optional, cast
from bench_executor.container import Container
from bench_executor.logger import Logger

VERSION = '5.0.0'
TIMEOUT = 6 * 3600  # 6 hours
R2RML = Namespace('http://www.w3.org/ns/r2rml#')


class Ontop(Container):
    """Ontop container super class for OntopMaterialize and OntopVirtualize."""
    def __init__(self, name: str, data_path: str, logger: Logger, mode: str):
        """Creates an instance of the Ontop class.

        Parameters
        ----------
        name : str
            Pretty name of the container.
        data_path: str
            Path to the data directory of the case.
        logger : Logger
            Logger to use for log messages.
        mode : str
            Ontop mode: `materialize` or `endpoint`
        """
        self._mode = mode
        self._headers: Dict[str, Dict[str, str]] = {}
        self._logger = logger
        self._data_path = data_path

        if self._mode == 'endpoint':
            subdir = 'ontopvirtualize'
        elif self._mode == 'materialize':
            subdir = 'ontopmaterialize'
        else:
            raise ValueError(f'Unknown Ontop mode: "{self._mode}"')
        os.makedirs(os.path.join(self._data_path, subdir), exist_ok=True)

        # Set Java heap to 1/2 of available memory instead of the default 1/4
        max_heap = int(psutil.virtual_memory().total * (1/2))

        # Configure logging
        log_level = 'info'
        if self._logger.verbose:
            log_level = 'debug'
        self._logger.info(f'Initialized Ontop logger at "{log_level}" level')

        environment = {'ONTOP_JAVA_ARGS': f'-Xmx{max_heap} -Xms{max_heap}',
                       'ONTOP_LOG_LEVEL': log_level}
        super().__init__(f'blindreviewing/ontop:v{VERSION}', name,
                         self._logger,
                         ports={'8888': '8888'},
                         environment=environment,
                         volumes=[f'{self._data_path}/'
                                  f'{self.root_mount_directory}:/data',
                                  f'{self._data_path}/shared:/data/shared'])

    @property
    def root_mount_directory(self) -> str:
        """Subdirectory in the root directory of the case for Ontop.

        Returns
        -------
        subdirectory : str
            Subdirectory of the root directory for Ontop.

        """
        if self._mode == 'endpoint':
            return 'ontopvirtualize'
        elif self._mode == 'materialize':
            return 'ontopmaterialize'
        else:
            raise ValueError(f'Unknown Ontop mode: "{self._mode}"')

    @property
    def endpoint(self) -> str:
        """SPARQL endpoint URL for Ontop.

        Returns
        -------
        url : str
            SPARQL endpoint URL.
        """
        return 'http://localhost:8888/sparql'

    @property
    def headers(self) -> dict:
        """HTTP headers of SPARQL queries for serialization formats.

        Only supported serialization formats are included in the dictionary.
        Currently, the following formats are supported:
        - N-Triples
        - N-Quads
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
        return self._headers

    def _execute(self, arguments: list) -> bool:
        """Execute Ontop with given arguments.

        Parameters
        ----------
        arguments : list
            Arguments to supply to Ontop.

        Returns
        -------
        success : bool
            Whether the execution succeeded or not.
        """

        cmd = f'/ontop/ontop {self._mode} {" ".join(arguments)}'
        self._logger.info(f'Executing Ontop with command: {cmd}')
        if self._mode == 'endpoint':
            log_line = 'OntopEndpointApplication - Started ' + \
                       'OntopEndpointApplication'
            success = self.run_and_wait_for_log(log_line, cmd)
        elif self._mode == 'materialize':
            success = self.run_and_wait_for_exit(cmd)
        else:
            self._logger.error(f'Unknown Ontop mode "{self._mode}"')
            success = False

        return success

    def _execute_mapping(self,
                         config_file: str,
                         arguments: list,
                         mapping_file: str,
                         output_file: Optional[str],
                         rdb_username: str,
                         rdb_password: str,
                         rdb_host: str,
                         rdb_port: int,
                         rdb_name: str,
                         rdb_type: str) -> bool:
        """Execute a mapping file with Ontop.

        Only relational databases are supported by
        Ontop, thus the relational database parameters are mandantory.

        Parameters
        ----------
        config_file : str
            Name of the generated config file for Ontop.
        arguments : list
            List of arguments to pass to Ontop.
        mapping_file : str
            Name of the mapping file to use.
        output_file : Optional[str]
            Name of the output file to use. Only applicable for
            materialization.
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
        # Generate INI configuration file since no CLI is available
        config = configparser.ConfigParser()
        config['root'] = {}
        if rdb_type == 'MySQL':
            dsn = f'jdbc:mysql://{rdb_host}:{rdb_port}/{rdb_name}'
            config['root']['jdbc.url'] = dsn
            config['root']['jdbc.driver'] = 'com.mysql.cj.jdbc.Driver'
        elif rdb_type == 'PostgreSQL':
            dsn = f'jdbc:postgresql://{rdb_host}:{rdb_port}/{rdb_name}'
            config['root']['jdbc.url'] = dsn
            config['root']['jdbc.driver'] = 'org.postgresql.Driver'
        else:
            msg = f'Unknown RDB type: "{rdb_type}"'
            self._logger.error(msg)
            raise ValueError(msg)
        config['root']['jdbc.user'] = rdb_username
        config['root']['jdbc.password'] = rdb_password

        path = os.path.join(self._data_path, self.root_mount_directory)
        os.makedirs(path, exist_ok=True)
        with open(os.path.join(path, 'config.properties'), 'w') as f:
            config.write(f, space_around_delimiters=False)

        # .properties files are like .ini files but without a [HEADER]
        # Use a [root] header and remove it after writing
        with open(os.path.join(path, 'config.properties'), 'r') as f:
            data = f.read()

        with open(os.path.join(path, 'config.properties'), 'w') as f:
            f.write(data.replace('[root]\n', ''))

        # Compatibility with Ontop requiring rr:class
        # Replace any rdf:type construction with rr:class
        # Without this, a strange error is raised: 'The definition of the
        # predicate is not always a ground term triple(s,p,o)'
        g = Graph()
        g.bind('r2rml', R2RML)
        g.bind('rdf', RDF)
        g.parse(os.path.join(self._data_path, 'shared',
                             os.path.basename(mapping_file)))

        for triples_map_iri, p, o in g.triples((None, RDF.type,
                                                R2RML.TriplesMap)):
            subject_map_iri = g.value(triples_map_iri, R2RML.subjectMap)

            if subject_map_iri is None:
                self._logger.warning("Subject Map not present in Triples Map")
                break

            iter_pom = g.triples((triples_map_iri,
                                  R2RML.predicateObjectMap,
                                  None))
            for s, p, predicate_object_map_iri in iter_pom:
                predicate_map_iri = g.value(predicate_object_map_iri,
                                            R2RML.predicateMap)
                object_map_iri = g.value(predicate_object_map_iri,
                                         R2RML.objectMap)

                if predicate_map_iri is None or object_map_iri is None:
                    continue

                # Check if PredicateObjectMap is pointing to a PredicateMap
                # specifying rdf:type. Skip this PredicateObjectMap if not
                if g.value(predicate_map_iri, R2RML.constant) != RDF.type:
                    continue

                # Retrieve the ObjectMap rr:constant value and add it as
                # rr:class to the Subject Map is present
                rdf_type_value = cast(URIRef,
                                      g.value(object_map_iri, R2RML.constant))
                if rdf_type_value is not None:
                    iri = URIRef(rdf_type_value.toPython())
                    g.add((subject_map_iri, R2RML['class'], iri))
                else:
                    msg = 'Cannot extract rr:class value, rdf:type value ' + \
                          'is not a constant value!'
                    self._logger.error(msg)
                    return False

                # Remove all triples associated with the rdf:type PredicateMap
                for s, p, o in g.triples((predicate_map_iri, None, None)):
                    g.remove((s, p, o))

                # Remove all triples associated with the rdf:type ObjectMap
                for s, p, o in g.triples((object_map_iri, None, None)):
                    g.remove((s, p, o))

                # Remove all triples associated with the
                # rdf:type PredicateObjectMap
                for s, p, o in g.triples((object_map_iri, None, None)):
                    g.remove((s, p, o))

                # Remove PredicateObjectMap from Triples Map
                g.remove((triples_map_iri, R2RML.predicateObjectMap,
                          predicate_object_map_iri))

            destination = os.path.join(self._data_path,
                                       self.root_mount_directory,
                                       'mapping_converted.r2rml.ttl')
            g.serialize(destination=destination, format='turtle')

        arguments.append('-m')
        arguments.append('/data/mapping_converted.r2rml.ttl')
        if output_file is not None:
            arguments.append('-o')
            arguments.append(os.path.join('/data/shared/', output_file))
        arguments.append('-p')
        arguments.append('/data/config.properties')

        return self._execute(arguments)


class OntopVirtualize(Ontop):
    """OntopVirtualize container for setting up an Ontop SPARQL endpoint."""
    def __init__(self, data_path: str, config_path: str, directory: str,
                 verbose: bool):
        """Creates an instance of the OntopVirtualize class.

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
        super().__init__('Ontop-Virtualize', self._data_path, self._logger,
                         'endpoint')

    def execute_mapping(self,
                        mapping_file: str,
                        serialization: str,
                        rdb_username: str,
                        rdb_password: str,
                        rdb_host: str,
                        rdb_port: int,
                        rdb_name: str,
                        rdb_type: str) -> bool:
        """Start an Ontop SPARQL endpoint with a mapping.

        Only relational databases are supported by
        Ontop, thus the relational database parameters are mandantory.
        Ontop SPARQL endpoint supports the following serialization formats:
        - N-Triples (Ontop v5+)
        - N-Quads (Ontop v5+)
        - Turtle
        - RDF/JSON
        - JSON-LD
        - CSV

        Parameters
        ----------
        mapping_file : str
            Path to the mapping file to execute.
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
        config_file = f'{self._data_path}/{self.root_mount_directory}' + \
                      '/config.properties'
        arguments = ['--cors-allowed-origins=*', '--port=8888']
        self._headers['ntriples'] = {'Accept': 'application/n-triples'}
        self._headers['nquads'] = {'Accept': 'application/n-quads'}
        self._headers['turtle'] = {'Accept': 'text/turtle'}
        self._headers['rdfjson'] = {'Accept': 'application/rdf+json'}
        self._headers['rdfxml'] = {'Accept': 'application/rdf+xml'}
        self._headers['jsonld'] = {'Accept': 'application/ld+json'}
        self._headers['csv'] = {'Accept': 'text/csv'}
        if serialization not in self._headers.keys():
            msg = 'Unsupported serialization format ' + \
                  f'"{serialization}" for Ontop'
            self._logger.error(msg)
            raise ValueError(msg)
        return super()._execute_mapping(config_file, arguments,
                                        mapping_file, None, rdb_username,
                                        rdb_password, rdb_host, rdb_port,
                                        rdb_name, rdb_type)


class OntopMaterialize(Ontop):
    """OntopMaterialize container to execute a R2RML mapping."""
    def __init__(self, data_path: str, config_path: str, directory: str,
                 verbose: bool):
        """Creates an instance of the OntopMaterialize class.

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
        os.makedirs(os.path.join(self._data_path, 'ontopmaterialize'),
                    exist_ok=True)
        super().__init__('Ontop-Materialize', self._data_path, self._logger,
                         'materialize')

    @timeout(TIMEOUT)
    def _execute_mapping_with_timeout(self, mapping_file: str,
                                      output_file: str,
                                      serialization: str,
                                      rdb_username: str,
                                      rdb_password: str,
                                      rdb_host: str,
                                      rdb_port: int,
                                      rdb_name: str,
                                      rdb_type: str) -> bool:
        """Execute a mapping with a provided timeout.

        Returns
        -------
        success : bool
            Whether the execution was successfull or not.
        """
        config_file = f'{self._data_path}/{self.root_mount_directory}' + \
                      '/config.properties'
        arguments = ['-f', serialization]
        self._headers = {}
        return super()._execute_mapping(config_file, arguments,
                                        mapping_file, output_file,
                                        rdb_username, rdb_password,
                                        rdb_host, rdb_port, rdb_name, rdb_type)

    def execute_mapping(self,
                        mapping_file: str,
                        output_file: str,
                        serialization: str,
                        rdb_username: str,
                        rdb_password: str,
                        rdb_host: str,
                        rdb_port: int,
                        rdb_name: str,
                        rdb_type: str) -> bool:
        """Execute a R2RML mapping with Ontop

        N-Quads and N-Triples are currently supported as serialization
        for Ontop materialize. Only relational databases are supported by
        Ontop, thus the relational database parameters are mandantory.

        Parameters
        ----------
        mapping_file : str
            Path to the mapping file to execute.
        output_file : str
            Name of the output file to store the triples in. This is not used
            for OntopVirtualize.
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
        try:
            return self._execute_mapping_with_timeout(mapping_file,
                                                      output_file,
                                                      serialization,
                                                      rdb_username,
                                                      rdb_password,
                                                      rdb_host,
                                                      rdb_port,
                                                      rdb_name,
                                                      rdb_type)
        except TimeoutError:
            msg = f'Timeout ({TIMEOUT}s) reached for Ontop Materialize'
            self._logger.warning(msg)

        return False
