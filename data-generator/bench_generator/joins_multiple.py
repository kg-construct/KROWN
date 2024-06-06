#!/usr/bin/env python3

"""
This module holds the Joins class which scales the dataset size
by the number of members in a dataset such as number of rows for tabular data.
"""

import os
import string
import random
from typing import Tuple
from pandas import DataFrame
from rdflib.namespace import RDF
from rdflib import Graph, URIRef, BNode, Literal, Namespace
from bench_generator.scenario import Scenario
from bench_generator.logger import Logger

DATA_FILE1 = 'data1.csv'
DATA_FILE2 = 'data2.csv'
RDB_MAPPING_FILE = 'mapping.r2rml.ttl'
CSV_MAPPING_FILE = 'mapping.rml.ttl'
R2RML = Namespace('http://www.w3.org/ns/r2rml#')
QL = Namespace('http://semweb.mmlab.be/ns/ql#')
EX = Namespace('http://example.com/')
MEMBERS_PERCENTAGE = 50.0


class JoinsMultiple(Scenario):
    def __init__(self, main_directory: str, verbose: bool, percentage: float,
                 n: int, m: int, jc: int, number_of_members: int,
                 number_of_properties: int, value_size: int, data_format: str,
                 engine: str, seed: int = 0):
        """Initialize a Joins Multiple scenario.

        Member's percentage is always set to 50%.

        Parameters
        ----------
        main_directory : str
            Root directory for generating instances of Joins Multiple.
        verbose : bool
            Verbose logging enabled or not.
        percentage : float
            Percentage of relations which should result into a join.
        n : int
            Relation size N.
        m : int
            Relation size M.
        jc : int
            Number of Join Conditions.
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
        """
        self._percentage = percentage
        self._n = n
        self._m = m
        self._jc = jc
        self._number_of_members: int = number_of_members
        self._number_of_properties: int = number_of_properties
        self._value_size: int = value_size
        random.seed(seed)

        super().__init__(data_format, engine, main_directory, verbose)

        if self._data_format != 'csv' and self._data_format != 'postgresql':
            raise NotImplementedError(f'Data format {self._data_format} '
                                      f'is not implemented by {__name__}')

        self._logger = Logger(__name__, self._main_directory, self._verbose)
        self._logger.debug(f'Generating join relations {self._n}-{self._m}'
                           f' with {self._percentage}% of relations,')

    def generate(self) -> bool:
        """Generate the instance using the Joins Multiple scenario.

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
        """Builds the file path for the instance of a Joins Multiple scenario.

        Returns
        -------
        path : str
            File path for the Joins Multiple's instance.
        """
        key = f'joins_mutiple_{self._n}-{self._m}_{self._jc}jc' + \
              f'_{self._percentage}'
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

    def _update_many_on_many(self,
                             dataframe1: DataFrame,
                             dataframe2: DataFrame) -> Tuple[DataFrame,
                                                             DataFrame]:
        # 0% percentage results in zero matches for the join condition,
        # don't even bother to try to match the dataframes
        if self._percentage == 0.0:
            return dataframe1, dataframe2

        percentaged_members = \
            self._number_of_members * (self._percentage / 100.0)

        sample1 = dataframe1.iloc[random.sample(list(dataframe1.index),
                                                int(percentaged_members))]
        sample1_v = sample1.reset_index(drop=True)
        sample2 = dataframe2.iloc[random.sample(list(dataframe2.index),
                                                int(percentaged_members))]
        sample2_v = sample2.reset_index(drop=True)

        number_of_members_n = self._number_of_members * (self._percentage / 100.0)
        number_of_members_m = self._number_of_members * (self._percentage / 100.0)
        members_to_join_n = number_of_members_n / self._n
        members_to_join_m = number_of_members_m / self._m

        k = max(int(members_to_join_n + 0.5), int(members_to_join_m + 0.5))
        sample_members = sample1_v.iloc[random.sample(list(sample1_v.index),
                                                      k)]
        values = list(set([m[1]['p1'] for m in sample_members.iterrows()]))[:int(members_to_join_m + 0.5)]
        values = values * self._m
        if len(values) > self._number_of_members:
            values = values[:self._number_of_members]

        sample2_v = dataframe2.iloc[random.sample(list(dataframe2.index),
                                                  len(values))]

        for jc in range(1, self._jc + 1):
            for i, j in zip(values, list(sample2_v.index)):
                dataframe2.loc[j, f'p{jc}'] = i

        ####
        values = list(set([m[1]['p1'] for m in sample_members.iterrows()]))[:int(members_to_join_n + 0.5)]
        values = values * self._n
        if len(values) > self._number_of_members:
            values = values[:self._number_of_members]

        sample1_v = dataframe1.iloc[random.sample(list(dataframe1.index),
                                                  len(values))]
        for jc in range(1, self._jc + 1):
            for i, j in zip(values, list(sample1_v.index)):
                dataframe1.loc[j, f'p{jc}'] = i

        return dataframe1, dataframe2

    def _add_join_multiple_predicate_object_map(self, mapping: Graph,
                                                triplesmap_iri: URIRef,
                                                predicate_value: URIRef,
                                                object_value: Literal,
                                                parent_triplesmap_iri: URIRef,
                                                jc_values: list) -> Graph:
        predicate_object_map_iri = BNode()
        predicate_map_iri = BNode()
        object_map_iri = BNode()

        for jc in jc_values:
            join_condition_iri = BNode()
            mapping.add((join_condition_iri, R2RML.child, jc['child']))
            mapping.add((join_condition_iri, R2RML.parent, jc['parent']))
            mapping.add((join_condition_iri, RDF.type, R2RML.JoinCondition))
            mapping.add((object_map_iri, R2RML.joinCondition, join_condition_iri))

        mapping.add((predicate_map_iri, R2RML.constant, predicate_value))
        mapping.add((predicate_map_iri, RDF.type, R2RML.PredicateMap))
        mapping.add((object_map_iri, RDF.type, R2RML.ReferenceObjectMap))
        mapping.add((object_map_iri, R2RML.parentTriplesMap, parent_triplesmap_iri))
        mapping.add((predicate_object_map_iri, R2RML.predicateMap, predicate_map_iri))
        mapping.add((predicate_object_map_iri, R2RML.objectMap, object_map_iri))
        mapping.add((predicate_object_map_iri, RDF.type, R2RML.PredicateObjectMap))
        mapping.add((triplesmap_iri, R2RML.predicateObjectMap, predicate_object_map_iri))

        return mapping

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
        if self._data_format == 'postgresql':
            triples_map1_iri = self._add_triples_map_table(mapping,
                                                           subject1_template,
                                                           Literal('data1'),
                                                           number=1)
            triples_map2_iri = self._add_triples_map_table(mapping,
                                                           subject2_template,
                                                           Literal('data2'),
                                                           number=2)
        elif self._data_format == 'csv':
            triples_map1_iri = \
                self._add_triples_map_source(mapping, subject1_template,
                                             Literal('/data/shared/data1.csv'),
                                             number=1)
            triples_map2_iri = \
                self._add_triples_map_source(mapping, subject1_template,
                                             Literal('/data/shared/data2.csv'),
                                             number=2)
        else:
            raise NotImplementedError(f'{self._data_format} not implemented')

        jc_values = []
        for i in range(1, self._jc + 1):
            jc_values.append({
                'child': Literal(f'p{i}'),
                'parent': Literal(f'p{i}')
            })

        self._add_join_multiple_predicate_object_map(mapping, triples_map1_iri,
                                                     EX['j1'], Literal('p1'),
                                                     triples_map2_iri,
                                                     jc_values)

        return mapping

    def _generate_csv(self) -> bool:
        """Generate the instance as CSV files.

        Returns
        -------
        success : bool
            True if successfull, false otherwise
        """
        os.makedirs(os.path.join(self.path(), 'data', 'shared'), exist_ok=True)
        data1_path = os.path.join(self.path(), 'data', 'shared', DATA_FILE1)
        dataframe1 = self._generate_dataframe()
        data2_path = os.path.join(self.path(), 'data', 'shared', DATA_FILE2)
        dataframe2 = self._generate_dataframe(self._number_of_members + 1,
                                              self._number_of_properties + 1)
        dataframe1, dataframe2 = self._update_many_on_many(dataframe1,
                                                           dataframe2)
        dataframe1.to_csv(data1_path, index=False)
        dataframe2.to_csv(data2_path, index=False)

        mapping_path = os.path.join(self.path(), 'data', 'shared', CSV_MAPPING_FILE)
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
        data1_path = os.path.join(self.path(), 'data', 'shared', DATA_FILE1)
        dataframe1 = self._generate_dataframe()
        data2_path = os.path.join(self.path(), 'data', 'shared', DATA_FILE2)
        dataframe2 = self._generate_dataframe(self._number_of_members + 1,
                                              self._number_of_properties + 1)
        dataframe1, dataframe2 = self._update_many_on_many(dataframe1,
                                                           dataframe2)
        dataframe1.to_csv(data1_path, index=False)
        dataframe2.to_csv(data2_path, index=False)

        mapping_path = os.path.join(self.path(), 'data', 'shared', RDB_MAPPING_FILE)
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
        name: str = f'join_multiple_{self._n}-{self._m}_{self._jc}_{self._percentage}'
        description: str = f'Join Multiple {self._n}-{self._m} {self._jc}JC {self._percentage}% '
        iri: str = f'http://example.org/join-percentage/{self._percentage}/'

        if self._data_format == 'postgresql':
            return self._generate_metadata(iri, name, description,
                                           RDB_MAPPING_FILE, joins=True)
        elif self._data_format == 'csv':
            return self._generate_metadata(iri, name, description,
                                           CSV_MAPPING_FILE, joins=True)
        else:
            raise NotImplementedError(f'{self._data_format} not implemented')

        return False
