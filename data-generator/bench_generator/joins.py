#!/usr/bin/env python3

"""
This module holds the Joins class which scales the dataset size
by the number of members in a dataset such as number of rows for tabular data.
"""

import os
import string
import random
from pandas import DataFrame
from rdflib.namespace import RDF
from rdflib import Graph, URIRef, BNode, Literal, Namespace
from bench_generator.scenario import Scenario
from bench_generator.logger import Logger

DATA_FILE1 = 'data1.csv'
DATA_FILE2 = 'data2.csv'
MAPPING_FILE = 'mapping.r2rml.ttl'
R2RML = Namespace('http://www.w3.org/ns/r2rml#')
QL = Namespace('http://semweb.mmlab.be/ns/ql#')
EX = Namespace('http://example.com/')


class Joins(Scenario):
    def __init__(self, main_directory: str, verbose: bool, percentage: float,
                 number_of_members: int, number_of_properties: int,
                 value_size: int, data_format: str, engine: str,
                 seed: int = 0, join_n: int = 1, join_m: int = 1):
        """Initialize a Raw Data scenario.

        Parameters
        ----------
        main_directory : str
            Root directory for generating instances of Raw Data.
        verbose : bool
            Verbose logging enabled or not.
        percentage : float
            Percentage of members which should result into a join.
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
        seed : int
            Random seed to use, default 0.
        join_n : int
            Join N-M relationship value N, default 1.
        join_m: int
            Join N-M relationship value M, default 1.
        """
        self._percentage = percentage
        self._number_of_members: int = number_of_members
        self._number_of_properties: int = number_of_properties
        self._value_size: int = value_size
        self._data_format: str = data_format
        self._engine: str = engine
        self._join_n: int = join_n
        self._join_m: int = join_m
        random.seed(seed)

        if self._data_format != 'csv':
            raise NotImplementedError(f'Data format {self._data_format} '
                                      f'is not implemented by {__name__}')

        super().__init__(main_directory, verbose)
        self._logger = Logger(__name__, self._main_directory, self._verbose)
        self._logger.debug(f'Generating join {self._join_n}-{self._join_m}'
                           f' with {self._percentage}%')

    def generate(self) -> bool:
        """Generate the instance using the Raw Data scenario.

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
        """Builds the file path for the instance of a Raw Data scenario.

        Returns
        -------
        path : str
            File path for the Raw Data's instance.
        """
        key = f'joins_{self._join_n}-{self._join_m}_{self._percentage}'
        path = os.path.join(self._main_directory, self._engine,
                            self._data_format, key)
        self._logger.debug(f'Generating to {path}')
        os.makedirs(path, exist_ok=True)
        return path

    def _generate_dataframe(self, member_offset: int = 1,
                            property_offset: int = 1) -> DataFrame:
        """Generate joins.

        Parameters
        ----------
        member_offset : int
            Offset to start member ID generation from. Default 1 (no offset).
        property_offset : int
            Offset to start property ID generation from. Default 1 (no offset).

        Returns
        -------
        dataframe : DataFrame
            Panda's DataFrame with generated joins.
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

    def _update_one_on_one(self, dataframe1: DataFrame,
                           dataframe2: DataFrame) -> DataFrame:
        # 0% percentage results in zero matches for the join condition,
        # don't even bother to try to match the dataframes
        if self._percentage == 0.0:
            return dataframe1, dataframe2

        # Sample both dataframes
        percentage_members = int(self._number_of_members *
                                 (self._percentage / 100.0))
        dataframe1_sample = dataframe1 \
            .loc[random.sample(list(dataframe1.index), percentage_members)]
        dataframe1_sample.reset_index(drop=True)
        number_of_members_n = self._number_of_members * percentage_members
        number_of_members_to_join_n = number_of_members_n / self._join_n
        number_of_members_m = self._number_of_members * percentage_members
        number_of_members_to_join_m = number_of_members_m / self._join_m

        members_sample_size = max(int(number_of_members_to_join_n + 0.5),
                                  int(number_of_members_to_join_m + 0.5))
        members_sample = dataframe1.iloc[random.sample(list(dataframe1.index),
                                         members_sample_size)]

        # Extract unique values of p1 from dataframe 1, only those sampled for
        # percentage to dataframe 2
        members_value = \
            list(set([row[1]['p1'] for row in members_sample.iterrows()]))\
            [:int(number_of_members_to_join_m + 0.5)]
        # Repeat the values M times to honor the relation size
        members_value = members_value * self.join_m

        # Limit number of values because we may have more values than members
        if len(members_value) > self._number_of_members:
            members_value = members_value[:self._number_of_members]

        dataframe2_sample = dataframe2 \
            .loc[random.sample(list(dataframe2.index), percentage_members)]

        # Update dataframe2 to match with dataframe1
        for i, j in zip(members_value, list(dataframe1_sample.index)):
            dataframe2.loc[j, 'id'] = i

        # Extract unique values of p1 from dataframe 2, only those sampled for
        # percentage to dataframe 1
        members_value = \
            list(set([row[1]['p1'] for row in members_sample.iterrows()]))\
            [:int(number_of_members_to_join_n + 0.5)]
        # Repeat the values M times to honor the relation size
        members_value = members_value * self.join_n

        if len(members_value) > self._number_of_members:
            members_value = members_value[:self._number_of_members]

        dataframe1_sample = dataframe1 \
            .loc[random.sample(list(dataframe1.index), percentage_members)]

        # Update dataframe1 to match with dataframe2
        for i, j in zip(members_value, list(dataframe2_sample.index)):
            dataframe1.loc[j, 'id'] = i

        return dataframe1, dataframe2

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
        predicate_value : URIRef
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
        mapping.add((object_map_iri, R2RML.column, object_value))
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

    def _add_triples_map(self, mapping: Graph, subject_value: Literal,
                         table_name: Literal, number: int = 1) -> URIRef:
        """Insert a TriplesMap into a [R2]RML mapping

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
        mapping.add((triples_map_iri, R2RML.logicalTable, logical_table_iri))
        mapping.add((triples_map_iri, R2RML.subjectMap, subject_map_iri))
        mapping.add((triples_map_iri, RDF.type, R2RML.TriplesMap))
        mapping.add((subject_map_iri, R2RML.template, subject_value))

        return triples_map_iri

    def _generate_mapping(self) -> Graph:
        """Generate a [R2]RML mapping for a Joins instance.

        Returns
        -------
        mapping : Graph
            [R2]RML mapping as an RDFLib Graph.
        """
        mapping: Graph = Graph(base='http://ex.com/')
        mapping.bind('rr', R2RML)
        mapping.bind('ql', QL)
        mapping.bind('ex', EX)
        subject1_template = Literal('http://ex.com/table1/{id}')
        subject2_template = Literal('http://ex.com/table2/{id}')
        triples_map1_iri = self._add_triples_map(mapping, subject1_template,
                                                 Literal('data'), number=1)
        triples_map2_iri = self._add_triples_map(mapping, subject2_template,
                                                 Literal('data'), number=2)

        self._add_join_predicate_object_map(mapping, triples_map1_iri,
                                            EX['j1'], Literal('p1'),
                                            triples_map2_iri, Literal('id'),
                                            Literal('id'))

        return mapping

    def _generate_csv(self) -> bool:
        """Generate the instance as CSV files.

        Returns
        -------
        success : bool
            True if successfull, false otherwise
        """
        data1_path = os.path.join(self.path(), DATA_FILE1)
        dataframe1 = self._generate_dataframe()
        data2_path = os.path.join(self.path(), DATA_FILE2)
        dataframe2 = self._generate_dataframe(self._number_of_members + 1,
                                              self._number_of_properties + 1)
        dataframe1, dataframe2 = self._update_one_on_one(dataframe1,
                                                         dataframe2)
        dataframe1.to_csv(data1_path, index=False)
        dataframe2.to_csv(data2_path, index=False)

        mapping_path = os.path.join(self.path(), MAPPING_FILE)
        mapping: Graph = self._generate_mapping()
        mapping.serialize(destination=mapping_path, format='turtle')

        return True

    def _generate_postgresql(self) -> bool:
        """Generate the instance as PostgreSQL with CSV files to load.

        Returns
        -------
        success : bool
            True if successfull, false otherwise
        """
        data1_path = os.path.join(self.path(), DATA_FILE1)
        self._generate_dataframe().to_csv(data1_path, index=False)
        data2_path = os.path.join(self.path(), DATA_FILE2)
        self._generate_dataframe().to_csv(data2_path, index=False)

        mapping_path = os.path.join(self.path(), MAPPING_FILE)
        mapping: Graph = self._generate_mapping()
        mapping.serialize(destination=mapping_path, format='turtle')

        return True
