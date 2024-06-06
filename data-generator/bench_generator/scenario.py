#!/usr/bin/env python3

"""
This module holds the abstract Scenario class which implements all the main
interfaces for a benchmark scenario. This class should never be used as a
scenario on its own but subclassed to implement a specific scenario.
"""

import os
import json
from rdflib.namespace import RDF
from rdflib import Graph, URIRef, BNode, Literal, Namespace
from abc import ABC, abstractmethod

METADATA_FILE = 'metadata.json'
METADATA_INDENT = 4
R2RML = Namespace('http://www.w3.org/ns/r2rml#')
RML = Namespace('http://semweb.mmlab.be/ns/rml#')
QL = Namespace('http://semweb.mmlab.be/ns/ql#')
EX = Namespace('http://example.com/')


class Scenario(ABC):
    def __init__(self, data_format: str, engine: str, main_directory: str,
                 verbose: bool):
        """Initializes the Scenario class.

        Parameters
        ----------
        data_format : str
            Data format to use for generating the data set, for example:
            "csv", "json", "xml", "postgresql", "mysql"
        engine : str
            Engine to use for execution of the generated scenario's instance,
            for example: "RMLMapper", "RMLStreamer", "SDMRDFizer", "MorphKGC",
            or "OntopMaterialize"
        main_directory : str
            Root directory to use for generating instances of scenario.
        verbose : bool
            If verbose logging is enabled.
        """
        self._data_format: str = data_format
        self._engine: str = engine
        self._main_directory: str = main_directory
        self._verbose: bool = verbose

    @abstractmethod
    def generate(self) -> bool:
        """Generate the scenario.

        Generate the scenario input to execute the scenario such as input
        data files, mappings, and other metadata.

        Returns
        -------
        success : bool
            True if success, otherwise false.
        """
        pass

    @abstractmethod
    def path(self) -> str:
        """Builds the file path for the instance of a scenario.

        Returns
        -------
        path : str
            File path for the scenario's instance
        """
        pass

    def _build_metadata(self, iri: str, name: str, description: str) -> dict:
        """Build a metadata structure.
        """
        return {
            '@id': iri,
            'name': name,
            'description': description,
            'steps': []
        }

    def _build_step(self, iri: str, name: str, resource: str, command: str,
                    parameters: dict, expect_failure: bool = False):
        """Build a step of the execution pipeline inside a metadata structure.
        """
        return {
            '@id': iri,
            'name': name,
            'resource': resource,
            'command': command,
            'parameters': parameters,
            'expect_failure': expect_failure
        }

    def _generate_metadata(self, iri: str, name: str, description: str,
                           mapping_file: str, serialization: str = 'ntriples',
                           joins: bool = False):
        """Generate the metadata for this scenario.

        Configures the execution pipeline automatically.

        Parameters
        ----------
        iri : str
            IRI to use for the scenario's metadata.
        name : str
            Name of the scenario.
        description : str
            Longer description of the scenario.
        mapping_file : str
            Name of the mapping file to use.
        serialization : str
            Serialization format to use. Default 'ntriples'.
        joins : bool
            If metadata is needed for joins. Default 'False'.

        Returns
        -------
        success : bool
            True if successfull, false otherwise
        """
        parameters: dict

        if self._data_format == 'postgresql':
            metadata = self._build_metadata(iri, name, description)

            # RDB setup
            if joins:
                parameters = {
                    'csv_files': [
                        {'file': 'data1.csv', 'table': 'data1'},
                        {'file': 'data2.csv', 'table': 'data2'}
                    ]
                }
                metadata['steps'].append(self._build_step(f'{iri}#step1',
                                                          'Load RDB',
                                                          'PostgreSQL',
                                                          'load_multiple',
                                                          parameters))
            else:
                parameters = {
                    'csv_file': 'data.csv',
                    'table': 'data'
                }
                metadata['steps'].append(self._build_step(f'{iri}#step1',
                                                          'Load RDB',
                                                          'PostgreSQL',
                                                          'load',
                                                          parameters))

            # Engine execution
            parameters = {
                'mapping_file': mapping_file,
                'output_file': 'out.nt',
                'serialization': serialization,
                'rdb_host': 'PostgreSQL',
                'rdb_port': 5432,
                'rdb_username': 'root',
                'rdb_password': 'root',
                'rdb_type': 'PostgreSQL',
                'rdb_name': 'db'
            }
            metadata['steps'].append(self._build_step(f'{iri}#step2',
                                                      'Execute RML mapping',
                                                      self._engine,
                                                      'execute_mapping',
                                                      parameters))
            self._write_metadata(self.path(), metadata)
        elif self._data_format == 'csv':
            metadata = self._build_metadata(iri, name, description)

            # Engine execution
            parameters = {
                'mapping_file': mapping_file,
                'output_file': 'out.nt',
                'serialization': serialization
            }
            metadata['steps'].append(self._build_step(f'{iri}#step1',
                                                      'Execute RML mapping',
                                                      self._engine,
                                                      'execute_mapping',
                                                      parameters))
            self._write_metadata(self.path(), metadata)
        else:
            raise NotImplementedError(f'{self._data_format} not implemented')

        return True

    def _write_metadata(self, path: str, metadata: dict):
        os.makedirs(os.path.join(path, 'data', 'shared'), exist_ok=True)
        with open(os.path.join(path, METADATA_FILE), 'w') as f:
            json.dump(metadata, f, indent=METADATA_INDENT)

    def _add_predicate_object_map(self, mapping: Graph, triplesmap_iri: URIRef,
                                  predicate_value: URIRef,
                                  object_value: Literal) -> BNode:
        """Insert a PredicateObjectMap into a [R2]RML mapping

        Parameters
        ----------
        mapping : Graph
            [R2]RML mapping as an RDFLib Graph.
        triples_map_iri : URIRef
            IRI of the Triples Map to insert the PredicateObjectMap in.
        predicate_value : Literal
            Predicate IRI value for PredicateObjectMap.
        object_value : Literal
            Object value for PredicateObjectMap.

        Returns
        -------
        predicate_object_map_iri : BNode
            Predicate Object Map blank node ID.
        """
        predicate_object_map_iri = BNode()
        predicate_map_iri = BNode()
        object_map_iri = BNode()

        mapping.add((predicate_map_iri, R2RML.constant, predicate_value))
        mapping.add((predicate_map_iri, RDF.type, R2RML.PredicateMap))
        if self._data_format == 'postgresql':
            mapping.add((object_map_iri, R2RML.column, object_value))
        else:
            mapping.add((object_map_iri, RML.reference, object_value))
        mapping.add((object_map_iri, RDF.type, R2RML.ObjectMap))
        mapping.add((predicate_object_map_iri, R2RML.predicateMap,
                     predicate_map_iri))
        mapping.add((predicate_object_map_iri, R2RML.objectMap,
                     object_map_iri))
        mapping.add((predicate_object_map_iri, RDF.type,
                     R2RML.PredicateObjectMap))
        mapping.add((triplesmap_iri, R2RML.predicateObjectMap,
                     predicate_object_map_iri))

        return predicate_object_map_iri

    def _add_join_predicate_object_map(self, mapping: Graph,
                                       triplesmap_iri: URIRef,
                                       predicate_value: URIRef,
                                       object_value: Literal,
                                       parent_triplesmap_iri: URIRef,
                                       child_value: Literal,
                                       parent_value: Literal) -> BNode:
        """Insert a join with join condition into a [R2]RML mapping

        Parameters
        ----------
        mapping : Graph
            [R2]RML mapping as an RDFLib Graph.
        triples_map_iri : URIRef
            IRI of the Triples Map to insert the PredicateObjectMap in.
        predicate_value : URIRef
            Predicate IRI value for PredicateObjectMap.
        object_value : Literal
            Object value for PredicateObjectMap.

        Returns
        -------
        predicat_object_map_with_join_iri : BNode
            Predicate Object Map with join blank node ID.
        """
        predicate_object_map_iri = BNode()
        predicate_map_iri = BNode()
        object_map_iri = BNode()
        join_condition_iri = BNode()

        mapping.add((join_condition_iri, R2RML.child, child_value))
        mapping.add((join_condition_iri, R2RML.parent, parent_value))
        mapping.add((join_condition_iri, RDF.type, R2RML.JoinCondition))
        mapping.add((predicate_map_iri, R2RML.constant, predicate_value))
        mapping.add((predicate_map_iri, RDF.type, R2RML.PredicateMap))
        mapping.add((object_map_iri, RDF.type, R2RML.ReferenceObjectMap))
        mapping.add((object_map_iri, R2RML.parentTriplesMap,
                     parent_triplesmap_iri))
        mapping.add((object_map_iri, R2RML.joinCondition, join_condition_iri))
        mapping.add((predicate_object_map_iri, R2RML.predicateMap,
                     predicate_map_iri))
        mapping.add((predicate_object_map_iri, R2RML.objectMap,
                     object_map_iri))
        mapping.add((predicate_object_map_iri, RDF.type,
                     R2RML.PredicateObjectMap))
        mapping.add((triplesmap_iri, R2RML.predicateObjectMap,
                     predicate_object_map_iri))

        return join_condition_iri

    def _add_triples_map_source(self, mapping: Graph, subject_value: Literal,
                                source_path: Literal,
                                number: int = 1) -> URIRef:
        """Insert a TriplesMap into a RML mapping with a Logical Source

        Parameters
        ----------
        mapping : Graph
            [R2]RML mapping as an RDFLib Graph.
        subject_value : Literal
            Subject IRI template value.
        source_path : Literal
            Path to source file.
        number : int
            Triples Map number, default 1.

        Returns
        -------
        triples_map_iri : URIRef
            IRI of the Triples Map inserted into the mapping.
        """
        triples_map_iri = URIRef(f'{mapping.base}#TriplesMap{number}')
        subject_map_iri = BNode()
        logical_source_iri = BNode()

        mapping.add((logical_source_iri, RML.source, source_path))
        mapping.add((logical_source_iri, RML.referenceFormulation, QL.CSV))
        mapping.add((logical_source_iri, RDF.type, RML.LogicalSource))
        mapping.add((triples_map_iri, RML.logicalSource, logical_source_iri))
        mapping.add((triples_map_iri, R2RML.subjectMap, subject_map_iri))
        mapping.add((triples_map_iri, RDF.type, R2RML.TriplesMap))
        mapping.add((subject_map_iri, R2RML.template, subject_value))

        return triples_map_iri

    def _add_triples_map_table(self, mapping: Graph, subject_value: Literal,
                               table_name: Literal, number: int = 1) -> URIRef:
        """Insert a TriplesMap into a [R2]RML mapping with a Logical Table

        Parameters
        ----------
        mapping : Graph
            [R2]RML mapping as an RDFLib Graph.
        subject_value : Literal
            Subject IRI template value.
        table_name : Literal
            SQL table name to add.
        number : int
            Triples Map number, default 1.

        Returns
        -------
        triples_map_iri : URIRef
            IRI of the Triples Map inserted into the mapping.
        """
        triples_map_iri = URIRef(f'{mapping.base}#TriplesMap{number}')
        subject_map_iri = BNode()
        logical_table_iri = BNode()

        mapping.add((logical_table_iri, R2RML.tableName, table_name))
        mapping.add((logical_table_iri, RDF.type, R2RML.LogicalTable))
        mapping.add((triples_map_iri, R2RML.logicalTable, logical_table_iri))
        mapping.add((triples_map_iri, R2RML.subjectMap, subject_map_iri))
        mapping.add((triples_map_iri, RDF.type, R2RML.TriplesMap))
        mapping.add((subject_map_iri, R2RML.template, subject_value))

        return triples_map_iri
