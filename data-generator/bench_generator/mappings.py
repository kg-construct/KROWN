#!/usr/bin/env python3

"""
This module holds the Mappings class which scales the dataset size
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
QL = Namespace('http://semweb.mmlab.be/ns/ql#')
EX = Namespace('http://example.com/')


class Mappings(Scenario):
    def __init__(self, main_directory: str, verbose: bool, number_of_tms: int,
                 number_of_poms: int, number_of_members: int,
                 number_of_properties: int, value_size: int, data_format: str,
                 engine: str):
        """Initialize a Mappings scenario.

        Parameters
        ----------
        main_directory : str
            Root directory for generating instances of Mappings.
        verbose : bool
            Verbose logging enabled or not.
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
        self._number_of_tms: int = number_of_tms
        self._number_of_poms: int = number_of_poms
        self._number_of_members: int = number_of_members
        self._number_of_properties: int = number_of_properties
        self._value_size: int = value_size

        super().__init__(data_format, engine, main_directory, verbose)
        if self._data_format != 'csv' and self._data_format != 'postgresql':
            raise NotImplementedError(f'Data format {self._data_format} '
                                      f'is not implemented by {__name__}')

        self._logger = Logger(__name__, self._main_directory, self._verbose)

    def generate(self) -> bool:
        """Generate the instance using the Mappings scenario.

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
        """Builds the file path for the instance of a Mappings scenario.

        Returns
        -------
        path : str
            File path for the Mappings's instance.
        """
        key = f'mappings_{self._number_of_tms}_' \
              f'{self._number_of_poms}'
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

    def _generate_mapping(self) -> Graph:
        """Generate a [R2]RML mapping for a Mappings instance.

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
                                                              number=i)
            elif self._data_format == 'csv':
                csv_path = Literal('/data/shared/data.csv')
                triples_map_iri = \
                    self._add_triples_map_source(mapping, subject_template,
                                                 csv_path, number=i)
            else:
                msg = f'{self._data_format} not implemented'
                raise NotImplementedError(msg)

            for j in range(1, self._number_of_poms + 1):
                self._add_predicate_object_map(mapping, triples_map_iri,
                                               EX[f'p{j}'], Literal(f'p{j}'))

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
        name: str = f'mappings_{self._number_of_tms}_{self._number_of_poms}'
        description: str = f'Mappings {self._number_of_tms}TM + ' + \
                           f'{self._number_of_poms}POMs'
        iri: str = f'http://example.org/mappings/{self._number_of_tms}/' + \
                   f'{self._number_of_poms}'

        if self._data_format == 'postgresql':
            return self._generate_metadata(iri, name, description,
                                           RDB_MAPPING_FILE)
        elif self._data_format == 'csv':
            return self._generate_metadata(iri, name, description,
                                           CSV_MAPPING_FILE)
        else:
            raise NotImplementedError(f'{self._data_format} not implemented')

        return False
