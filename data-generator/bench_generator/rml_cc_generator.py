#!/usr/bin/env python3

"""
This module holds the RawData class which scales the dataset size
by the number of members in a dataset such as number of rows for tabular data.
"""

import os
import shutil
import string
from pandas import DataFrame
from abc import abstractmethod
from pandas.core.series import doc
from rdflib import Graph, Literal, Namespace
from bench_generator.scenario import Scenario
from bench_generator.logger import Logger
from bench_generator.rmlcc.scale_join import main as join_main
from bench_generator.rmlcc.scale_data_multi import main as multi_main
from bench_generator.rmlcc.scale_data_one import main as simple_main
from bench_generator.rmlcc.scale_duplication import main as duplicate_main

MAPPING_FILE_PAIRS = """RMLTC-CC-0001-Alt,simple
RMLTC-CC-0001-Bag,simple
RMLTC-CC-0001-List,simple
RMLTC-CC-0001-Seq,simple
RMLTC-CC-0002-Bag,simple
RMLTC-CC-0002-List,simple
RMLTC-CC-0004-SM1,simple
RMLTC-CC-0004-SM2,simple
RMLTC-CC-0004-SM3,simple
RMLTC-CC-0004-SM4,simple
RMLTC-CC-0004-SM5,simple
RMLTC-CC-0005-App1,multivalues
RMLTC-CC-0005-App2,multivalues
RMLTC-CC-0005-Car1,multivalues
RMLTC-CC-0005-Car2,multivalues
RMLTC-CC-0006-IT0,simple
RMLTC-CC-0006-IT1,simple
RMLTC-CC-0006-IT2,multivalues
RMLTC-CC-0006-IT3,simple
RMLTC-CC-0006-IT4,simple
RMLTC-CC-0006-IT5,multivalues
RMLTC-CC-0007-NES,multivalues
RMLTC-CC-0008-ROMa,join
RMLTC-CC-0008-ROMb,join
RMLTC-CC-0009-DUP-Bag,duplicates
RMLTC-CC-0009-DUP-List,duplicates
"""
DATA_FILE = "data.csv"
RESOURCE_FOLDER = "resources/rml-cc"
SEED_MULTI_FILE = f"{RESOURCE_FOLDER}/seed_data/multivalues.json"
SEED_DUPLI_FILE = f"{RESOURCE_FOLDER}/seed_data/duplicate.json"
SEED_SIMPLE_FILE = f"{RESOURCE_FOLDER}/seed_data/simple.json"
SEED_JOIN_FILE = f"{RESOURCE_FOLDER}/seed_data/join.csv"
RML = Namespace("http://w3id.org/rml/")
EX = Namespace("http://example.com/")


class RMLCCData(Scenario):
    def __init__(
        self,
        main_directory: str,
        verbose: bool,
        data_format: str,
        engine: str,
        data_type: str,
        add_values: int = 0,
        count: int = 10000,
        list_length: int = 10,
        unique: bool = True,
        duplication_rate: float = 0.0,
    ):
        """Initializes a Collections and Containers Scenario.

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
        super().__init__(data_format, engine, main_directory, verbose)
        self._data_type = data_type
        self._unique = unique
        self._list_length = list_length
        self._count = count
        self._add_values = add_values
        self._duplication_rate = duplication_rate
        self._logger = Logger(__name__, self._main_directory, self._verbose)
        self._mapping_folder_dict: dict = dict()
        mapping_file_pairs = [x.split(",") for x in MAPPING_FILE_PAIRS.splitlines()]

        for pair in mapping_file_pairs:
            mapping_file = pair[0]
            data_type = pair[1]
            if data_type in self._mapping_folder_dict:
                self._mapping_folder_dict[data_type].append(mapping_file)
            else:
                self._mapping_folder_dict[data_type] = [mapping_file]

    def generate(self) -> bool:
        """Generate the instance using RML CC scenario.
        Only JSON files are currently implemented!

        Returns
        -------
        success : bool
            True if success, otherwise false.
        """
        if self._data_format == "json":
            return self._generate()
        else:
            raise NotImplementedError(
                f"Data format {self._data_format} " f"is not implemented by {__name__}"
            )

    def path(self) -> str:
        """Builds the file path for the instance of a scenario.

        Returns
        -------
        path : str
            File path for the scenario's instance
        """
        key = (
            f"rmlcc_{self._data_type}_{self._duplication_rate:.2f}_"
            f"{self._count}_{self._list_length}_"
            f"{self._add_values}_{self._unique}"
        )
        path = os.path.join(self._main_directory, self._engine, self._data_format, key)
        self._logger.debug(f"Generating to {path}")
        os.makedirs(path, exist_ok=True)
        return path

    def _generate_metadata_data_type(self) -> bool:
        iri: str = (
            f"http://example.org/rmlcc/eval/scenario/{self._data_type}/"
            + f"{self._count}/{self._add_values}/{self._unique}/{self._list_length}/{self._duplication_rate:.2f}"
        )
        name: str = (
            f"{self._data_type}_{self._count}_{self._add_values}_{self._unique}_{self._list_length}_{self._duplication_rate:.2f}"
        )

        description: str = (
            f"RML CC performance benchmark for type: {self._data_type} with count {self._count} and added values {self._add_values}"
        )

        metadata = self._build_metadata(iri, name, description)
        for mapping_folder in self._mapping_folder_dict[self._data_type]:
            print(mapping_folder)
            parameters = {
                "mapping_file": f'{mapping_folder}_mapping.ttl',
                "output_file": f'{mapping_folder}_out.nt',
            }
            metadata["steps"].append(
                self._build_step(
                    f'{iri}/step1',
                    f'Execute mapping for RML-CC case {mapping_folder} with scenario type {self._data_type}',
                    self._engine,
                    "execute_mapping",
                    parameters,
                )
            )

        self._write_metadata(self.path(), metadata)
        return True

    def _generate_mapping(self, output_dir: str) -> bool:
        mapping_folders = self._mapping_folder_dict[self._data_type]
        for mapping_folder in mapping_folders:
            mapping_file = f"{RESOURCE_FOLDER}/{mapping_folder}/mapping.ttl"
            shutil.copy(mapping_file, f'{output_dir}/{mapping_folder}_mapping.ttl')
        return True

    def _generate(self) -> bool:
        output_path = f"{self.path()}/data/shared"
        os.makedirs(output_path, exist_ok=True)

        self._generate_metadata_data_type()
        self._generate_mapping(output_path)

        if not os.path.exists(output_path):
            os.mkdir(output_path)
        if self._data_type == "simple":
            return self._generate_simple(output_path)
        elif self._data_type == "multivalues":
            return self._generate_multivalues(output_path)
        elif self._data_type == "join":
            return self._generate_join(output_path)
        elif self._data_type == "duplicates":
            return self._generate_duplicate(output_path)
        return False

    def _generate_multivalues(self, output_path: str) -> bool:
        multi_main(
            SEED_MULTI_FILE, f"{output_path}/data.json", self._add_values, self._unique
        )
        return True

    def _generate_simple(self, output_path: str) -> bool:
        simple_main(
            SEED_SIMPLE_FILE, f"{output_path}/data.json", self._count, self._list_length
        )
        return True

    def _generate_join(self, output_path: str) -> bool:
        join_main(
            SEED_JOIN_FILE,
            f"{output_path}/data.json",
            self._count,
            self._duplication_rate,
        )
        return False

    def _generate_duplicate(self, output_path: str) -> bool:
        duplicate_main(
            SEED_DUPLI_FILE,
            f"{output_path}/data.json",
            self._count,
            self._list_length,
            self._duplication_rate,
        )
        return False
