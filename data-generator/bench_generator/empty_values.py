#!/usr/bin/env python3

"""
This module holds the EmptyValues class which scales the number of empty values
in a data set with a fixed data size.
"""

import os
import string
import random
from pandas import DataFrame
from rdflib.namespace import RDF
from rdflib import Graph, URIRef, BNode, Literal, Namespace
from bench_generator.scenario import Scenario
from bench_generator.logger import Logger

DATA_FILE = 'data.csv'
RDB_MAPPING_FILE = 'mapping.r2rml.ttl'
CSV_MAPPING_FILE = 'mapping.rml.ttl'
R2RML = Namespace('http://www.w3.org/ns/r2rml#')
RML = Namespace('http://semweb.mmlab.be/ns/rml#')
QL = Namespace('http://semweb.mmlab.be/ns/ql#')
EX = Namespace('http://example.com/')


class EmptyValues(Scenario):
    def __init__(self, main_directory: str, verbose: bool,
                 percentage: float, data_format: str, engine: str,
                 seed: int = 0, number_of_members: int = 100000,
                 number_of_properties: int = 20, value_size: int = 0):
        """Initialize a EmptyValues scenario.

        Parameters
        ----------
        main_directory : str
            Root directory for generating instances of EmptyValues.
        verbose : bool
            Verbose logging enabled or not.
        percentage : float
            Percentage empty values to generate, for example 50% results into
            a dataset with 50% the same data values.
        data_format : str
            Data format to use for generating the data set, for example:
            "csv", "json", "xml", "postgresql", "mysql"
        engine : str
            Engine to use for execution of the generated scenario's instance,
            for example: "RMLMapper", "RMLStreamer", "SDMRDFizer", "MorphKGC",
            or "OntopMaterialize"
        seed : int
            Random seed to use, default 0.
        number_of_members : int
            Number of members to generate, for example 5000 for 5K rows in a
            tabular data structure. Default 100K members.
        number_of_properties : int
            Number of properties per member to generate, for example 20 for
            20 columns in a tabular data structure. Default 20 properties.
        value_size : int
            Number of characters to add to default value generation,
            for example: 256 will expand all values to 256 characters.
            Default 0 added characters.
        """
        self._percentage: float = percentage
        self._number_of_members = number_of_members
        self._number_of_properties = number_of_properties
        self._value_size = value_size
        random.seed(seed)

        super().__init__(data_format, engine, main_directory, verbose)
        if self._data_format != 'csv':
            raise NotImplementedError(f'Data format {self._data_format} '
                                      f'is not implemented by {__name__}')

        self._logger = Logger(__name__, self._main_directory, self._verbose)

    def generate(self) -> bool:
        """Generate the instance using the Duplciates scenario.

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
        """Builds the file path for the instance of a EmptyValues scenario.

        Returns
        -------
        path : str
            File path for the EmptyValues' instance.
        """
        key = f'empty_{self._percentage}_percentage'
        path = os.path.join(self._main_directory, self._engine,
                            self._data_format, key)
        self._logger.debug(f'Generating to {path}')
        os.makedirs(path, exist_ok=True)
        return path

    def _generate_dataframe(self, member_offset: int = 1,
                            property_offset: int = 1) -> DataFrame:
        """Generate empty values data.

        Parameters
        ----------
        member_offset : int
            Offset to start member ID generation from. Default 1 (no offset).
        property_offset : int
            Offset to start property ID generation from. Default 1 (no offset).

        Returns
        -------
        dataframe : DataFrame
            Panda's DataFrame with generated data.
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

    def _update_dataframe(self, dataframe: DataFrame):
        """
        Sample a percentage of the dataframe to fill with the same value.

        Parameters
        ----------
        dataframe : DataFrame
            The dataframe to update.

        Returns
        -------
        dataframe : DataFrame
            The updated dataframe.
        """
        percentage_members: float = self._number_of_members * \
            (self._percentage / 100.0)
        sample = dataframe.iloc[random.sample(list(dataframe.index),
                                              int(percentage_members))]
        for i in list(sample.index):
            for j in range(1, self._number_of_properties + 1):
                dataframe.loc[i, f'p{j}'] = 'NULL'

        return dataframe

    def _generate_mapping(self) -> Graph:
        """Generate a [R2]RML mapping for a EmptyValues instance.

        Returns
        -------
        mapping : Graph
            [R2]RML mapping as an RDFLib Graph.
        """
        mapping: Graph = Graph(base='http://ex.com/')
        mapping.bind('rr', R2RML)
        mapping.bind('ql', QL)
        mapping.bind('ex', EX)
        subject_template = Literal('http://ex.com/table/{id}')

        if self._data_format == 'postgresql':
            triples_map_iri = self._add_triples_map_table(mapping,
                                                          subject_template,
                                                          Literal('data'))
        elif self._data_format == 'csv':
            triples_map_iri = \
                self._add_triples_map_source(mapping, subject_template,
                                             Literal('/data/shared/data.csv'))
        else:
            raise NotImplementedError(f'{self._data_format} not implemented')

        for i in range(1, self._number_of_properties + 1):
            self._add_predicate_object_map(mapping, triples_map_iri,
                                           EX[f'p{i}'], Literal(f'p{i}'))

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
        dataframe = self._generate_dataframe()
        dataframe = self._update_dataframe(dataframe)
        dataframe.to_csv(data_path, index=False)

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
        dataframe = self._generate_dataframe()
        dataframe = self._update_dataframe(dataframe)
        dataframe.to_csv(data_path, index=False)

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
        name: str = f'empty_{self._percentage}'
        description: str = f'Empty Values {self._percentage}'
        iri: str = f'http://example.org/empty/{self._percentage}/'

        if self._data_format == 'postgresql':
            return self._generate_metadata(iri, name, description,
                                           RDB_MAPPING_FILE)
        elif self._data_format == 'csv':
            return self._generate_metadata(iri, name, description,
                                           CSV_MAPPING_FILE)
        else:
            raise NotImplementedError(f'{self._data_format} not implemented')

        return False
