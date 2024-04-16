#!/usr/bin/env python3

"""
This module holds the NamedGraph class which scales the dataset size
by the number of members in a dataset such as number of rows for tabular data.
"""

import os
import string
from pandas import DataFrame
from rdflib.namespace import RDF
from rdflib import Graph, URIRef, BNode, Literal, Namespace
from bench_generator.scenario import Scenario
from bench_generator.logger import Logger

DATA_FILE = 'data.csv'
CSV_MAPPING_FILE = 'mapping.rml.ttl'
RDB_MAPPING_FILE = 'mapping.r2rml.ttl'
R2RML = Namespace('http://www.w3.org/ns/r2rml#')
RML = Namespace('http://semweb.mmlab.be/ns/rml#')
QL = Namespace('http://semweb.mmlab.be/ns/ql#')
EX = Namespace('http://example.com/')


class NamedGraph(Scenario):
    def __init__(self, main_directory: str, verbose: bool,
                 number_of_ng_pom: int, number_of_ng_s: int, static: bool,
                 number_of_tms: int, number_of_poms: int,
                 number_of_members: int, number_of_properties: int,
                 value_size: int, data_format: str, engine: str):
        """Initialize a NamedGraph scenario.

        Parameters
        ----------
        main_directory : str
            Root directory for generating instances of NamedGraph.
        verbose : bool
            Verbose logging enabled or not.
        number_of_ng_pom : int
            Number of named graphs per Predicate Object Map.
        number_of_ng_s : int
            Number of named graphs for Subject Map.
        number_of_members : int
            Number of members to generate, for example 5000 for 5K rows in a
            tabular data structure.
        number_of_properties : int
            Number of properties per member to generate, for example 20 for
            20 columns in a tabular data structure.
        value_size : int
            Number of characters to add to default value generation,
            for example: 256 will expand all values to 256 characters.
        data_format : str
            Data format to use for generating the data set, for example:
            "csv", "json", "xml", "postgresql", "mysql"
        engine : str
            Engine to use for execution of the generated scenario's instance,
            for example: "RMLMapper", "RMLStreamer", "SDMRDFizer", "MorphKGC",
            or "OntopMaterialize"
        """
        self._number_of_ng_pom: int = number_of_ng_pom
        self._number_of_ng_s: int = number_of_ng_s
        self._static: bool = static
        self._number_of_tms: int = number_of_tms
        self._number_of_poms: int = number_of_poms
        self._number_of_members: int = number_of_members
        self._number_of_properties: int = number_of_properties
        self._value_size: int = value_size

        super().__init__(data_format, engine, main_directory, verbose)
        self._logger = Logger(__name__, self._main_directory, self._verbose)

    def generate(self) -> bool:
        """Generate the instance using the NamedGraph scenario.

        Only CSV files are currently implemented!
        """
        if self._data_format == 'csv':
            return self._generate_csv()
        elif self._data_format == 'postgresql':
            return self._generate_postgresql()
        else:
            raise NotImplementedError(f'Data format {self._data_format} '
                                      f'is not implemented by {__name__}')

    def path(self) -> str:
        """Builds the file path for the instance of a NamedGraph scenario.

        Returns
        -------
        path : str
            File path for the NamedGraph's instance.
        """
        key = f'namedgraph_{self._number_of_ng_s}SM-NG_' \
              f'{self._number_of_ng_pom}POM-NG_{self._number_of_tms}TM_' \
              f'{self._number_of_poms}POM_{self._static}'
        path = os.path.join(self._main_directory, self._engine,
                            self._data_format, key)
        self._logger.debug(f'Generating to {path}')
        os.makedirs(path, exist_ok=True)
        return path

    def _generate_dataframe(self, member_offset: int = 1,
                            property_offset: int = 1) -> DataFrame:
        """Generate mappings.

        Parameters
        ----------
        member_offset : int
            Offset to start member ID generation from. Default 1 (no offset).
        property_offset : int
            Offset to start property ID generation from. Default 1 (no offset).

        Returns
        -------
        dataframe : DataFrame
            Panda's DataFrame with generated mappings.
        """
        subject_id = range(member_offset,
                           self._number_of_members + member_offset)
        value_id = range(property_offset,
                         self._number_of_members + property_offset)
        data: dict = {'id': subject_id}
        n_ascii = len(string.ascii_letters)

        for j in range(1, self._number_of_properties + 1):
            # Append ASCII characters if necessary, use modulo to avoid out of
            # range in ASCII table
            append_value = ''
            if self._value_size > 0:
                append_value = '_'
            for n in range(self._value_size):
                append_value += string.ascii_letters[n % n_ascii]

            # Generate value V_{property}_{member} honoring the value size
            value = [f'V_{j}-{i}{append_value}' for i in value_id]
            data[f'p{j}'] = value

        return DataFrame(data)

    def _add_predicate_object_map(self, mapping: Graph, triplesmap_iri: URIRef,
                                  predicate_value: URIRef,
                                  object_value: Literal, named_graphs: int = 0,
                                  static: bool = True) -> BNode:
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

        for i in range(1, named_graphs + 1):
            if static:
                if self._number_of_ng_s == 0:
                    mapping.add((predicate_object_map_iri, R2RML.graph,
                                URIRef(f'http://example.org/graph{i}')))
                else:
                    mapping.add((predicate_object_map_iri, R2RML.graph,
                                URIRef(f'http://example.org/pom/graph{i}')))
            else:
                graph_map_iri = BNode()
                mapping.add((predicate_object_map_iri, R2RML.graphMap,
                             graph_map_iri))
                if self._number_of_ng_s == 0:
                    mapping.add((graph_map_iri, R2RML.template,
                                 Literal(f'http://example.org/graph{{p{i}}}')))
                else:
                    mapping.add((graph_map_iri, R2RML.template,
                                 Literal('http://example.org/pom/'
                                         f'graph{{p{i}}}')))

        return predicate_object_map_iri

    def _add_triples_map_source(self, mapping: Graph, subject_value: Literal,
                                source_path: Literal, number: int = 1,
                                named_graphs: int = 0,
                                static: bool = True) -> URIRef:
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
        named_graphs : int
            Number of named graphs, default 0.

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

        for i in range(1, named_graphs + 1):
            if static:
                mapping.add((subject_map_iri, R2RML.graph,
                             URIRef(f'http://example.org/graph{i}')))
            else:
                graph_map_iri = BNode()
                mapping.add((subject_map_iri, R2RML.graphMap, graph_map_iri))
                mapping.add((graph_map_iri, R2RML.template,
                             Literal(f'http://example.org/graph{{p{i}}}')))

        return triples_map_iri

    def _add_triples_map_table(self, mapping: Graph, subject_value: Literal,
                               table_name: Literal, number: int = 1,
                               named_graphs: int = 0,
                               static: bool = True) -> URIRef:
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
        named_graphs : int
            Number of named graphs, default 0.

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

        for i in range(1, named_graphs + 1):
            if static:
                mapping.add((subject_map_iri, R2RML.graph,
                             URIRef(f'http://example.org/graph{i}')))
            else:
                graph_map_iri = BNode()
                mapping.add((subject_map_iri, R2RML.graphMap, graph_map_iri))
                mapping.add((graph_map_iri, R2RML.template,
                             Literal(f'http://example.org/graph{{p{i}}}')))

        return triples_map_iri

    def _generate_mapping(self) -> Graph:
        """Generate a [R2]RML mapping for a NamedGraph instance.

        Returns
        -------
        mapping : Graph
            [R2]RML mapping as an RDFLib Graph.
        """
        mapping: Graph = Graph(base='http://ex.com/')
        mapping.bind('rr', R2RML)
        mapping.bind('ql', QL)
        mapping.bind('ex', EX)

        for i in range(1, self._number_of_tms + 1):
            subject_template = Literal(f'http://ex.com/table/{{p{i}}}')
            if self._data_format == 'postgresql':
                triples_map_iri = self._add_triples_map_table(mapping,
                                                              subject_template,
                                                              Literal('data'),
                                                              number=i,
                                                              named_graphs=self._number_of_ng_s,
                                                              static=self._static)
            elif self._data_format == 'csv':
                csv_path = Literal('/data/shared/data.csv')
                triples_map_iri = \
                    self._add_triples_map_source(mapping, subject_template,
                                                 csv_path, number=i,
                                                 named_graphs=self._number_of_ng_s,
                                                 static=self._static)
            else:
                msg = f'{self._data_format} not implemented'
                raise NotImplementedError(msg)

            for j in range(1, self._number_of_poms + 1):
                self._add_predicate_object_map(mapping, triples_map_iri,
                                               EX[f'p{j}'], Literal(f'p{j}'),
                                               named_graphs=self._number_of_ng_pom,
                                               static=self._static)

        return mapping

    def _generate_csv(self) -> bool:
        """Generate the instance as CSV files.

        Returns
        -------
        success : bool
            True if successfull, false otherwise
        """
        os.makedirs(os.path.join(self.path(), 'data', 'shared'), exist_ok=True)
        data_path = os.path.join(self.path(), 'data', 'shared', DATA_FILE)
        self._generate_dataframe().to_csv(data_path, index=False)

        mapping_path = os.path.join(self.path(), 'data', 'shared',
                                    CSV_MAPPING_FILE)
        mapping: Graph = self._generate_mapping()
        mapping.serialize(destination=mapping_path, format='turtle')
        self._generate_scenario()

        return True

    def _generate_postgresql(self) -> bool:
        """Generate the instance as PostgreSQL with CSV files to load.

        Returns
        -------
        success : bool
            True if successfull, false otherwise
        """
        os.makedirs(os.path.join(self.path(), 'data', 'shared'), exist_ok=True)
        data_path = os.path.join(self.path(), 'data', 'shared', DATA_FILE)
        self._generate_dataframe().to_csv(data_path, index=False)

        mapping_path = os.path.join(self.path(), 'data', 'shared',
                                    RDB_MAPPING_FILE)
        mapping: Graph = self._generate_mapping()
        mapping.serialize(destination=mapping_path, format='turtle')
        self._generate_scenario()

        return True

    def _generate_scenario(self) -> bool:
        """Generate the metadata for this scenario.

        Configures the execution pipeline automatically.

        Returns
        -------
        success : bool
            True if successfull, false otherwise
        """
        name: str = f'namedgraph_{self._number_of_ng_s}_' \
                    f'{self._number_of_ng_pom}_{self._number_of_tms}_' \
                    f'{self._number_of_poms}_{self._static}'
        description: str = f'NamedGraph {self._number_of_tms}TM + ' + \
                           f'{self._number_of_poms}POMs'
        iri: str = f'http://example.org/mappings/{self._number_of_tms}/' + \
                   f'{self._number_of_poms}/{self._number_of_ng_s}/' + \
                   f'{self._number_of_ng_pom}/{self._static}'

        if self._data_format == 'postgresql':
            return self._generate_metadata(iri, name, description,
                                           RDB_MAPPING_FILE,
                                           serialization='nquads')
        elif self._data_format == 'csv':
            return self._generate_metadata(iri, name, description,
                                           CSV_MAPPING_FILE,
                                           serialization='nquads')
        else:
            raise NotImplementedError(f'{self._data_format} not implemented')

        return False
