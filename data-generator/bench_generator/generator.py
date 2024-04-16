#!/usr/bin/env python3

"""
This module holds the Generator class which is responsible for generating a
benchmark testbed. All features of this tool can be accessed through the
Generator class, other classes should not be used directly.
"""

import os
import sys
import json
import importlib
import inspect
import jsonschema
from glob import glob
from typing import List, Dict, Any
from bench_generator.logger import Logger

SCHEMA_FILE = 'metadata.schema'
DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')


class Generator:
    """
    Generator class generates a benchmark testbed.
    """

    def __init__(self, main_directory: str, verbose: bool = False):
        """Create an instance of the Benchmark class.

        Parameters
        ----------
        main_directory : str
            The root directory of all the cases to execute.
        verbose : bool
            Enables verbose logs.
        """
        self._main_directory = os.path.abspath(main_directory)
        self._resources: List[Dict[str, Any]] = []
        self._class_module_mapping: Dict[str, Any] = {}
        self._verbose = verbose
        self._logger = Logger(__name__, self._main_directory, self._verbose)
        self._schema = {}

        with open(os.path.join(DATA_DIR, SCHEMA_FILE)) as f:
            self._schema = json.load(f)

        self._init_resources()

    @property
    def main_directory(self) -> str:
        """The main directory of all the cases.

        Returns
        -------
        main_directory : str
            The path to the main directory of the cases.
        """
        return self._main_directory

    def _init_resources(self) -> None:
        """Initialize resources of a case

        Resources are discovered automatically by analyzing Python modules.
        """

        # Discover all modules to import
        sys.path.append(os.path.dirname(__file__))
        self._modules = list(filter(lambda x: x.endswith('.py')
                                    and '__init__' not in x
                                    and '__pycache__' not in x,
                                    os.listdir(os.path.dirname(__file__))))

        # Discover all classes in each module
        for m in self._modules:
            module_name = os.path.splitext(m)[0]
            parent_module = os.path.split(os.path.dirname(__file__))[-1]
            import_name = '.'.join([parent_module, module_name])
            imported_module = importlib.import_module(import_name)
            for name, cls in inspect.getmembers(imported_module,
                                                inspect.isclass):
                parent_cls = cls.__base__

                # Skip hidden classes
                if name.startswith('_') or name[0].islower():
                    continue

                # Skip classes which do not inherit from Scenario
                if parent_cls is None or parent_cls.__name__ != 'Scenario':
                    continue

                # Store class-module mapping for reverse look-up
                self._class_module_mapping[name] = imported_module

                # Discover all methods and their parameters in each class
                methods: Dict[str, List[Dict[str, str]]] = {}
                filt = inspect.getmembers(cls, inspect.isfunction)
                for method_name, method in filt:
                    parameters = inspect.signature(method).parameters
                    methods[method_name] = []
                    for key in parameters.keys():
                        if key == 'self':
                            continue
                        p = parameters[key]
                        required = (p.default == inspect.Parameter.empty)
                        methods[method_name].append({'name': p.name,
                                                     'required': required})

                if name not in list(filter(lambda x: x['name'],
                                           self._resources)):
                    self._resources.append({'name': name, 'commands': methods})

    def _resources_all_names(self) -> list:
        """Retrieve all resources' name in a case.

        Returns
        -------
        names : list
            List of all resources' name in a case.
        """
        names = []
        for r in self._resources:
            names.append(r['name'])

        return names

    def _resources_all_commands_by_name(self, name: str) -> list:
        """Retrieve all resources' commands.

        Parameters
        ----------
        name : str
            The resource's name.

        Returns
        -------
        commands : list
            List of commands for the resource.
        """
        commands = []
        for r in filter(lambda x: x['name'] == name, self._resources):
            commands += list(r['commands'].keys())  # type: ignore

        return commands

    def _resources_all_parameters_by_command(self, name: str,
                                             command: str,
                                             required_only=False) -> list:
        """Retrieve all parameters of a command of a resource.

        Parameters
        ----------
        name : str
            The resource's name.
        command : str
            The command's name.
        required_only : bool
            Only return the required parameters of a command. Default all
            parameters are returned.

        Returns
        -------
        parameters : list
            List of parameters of the resource's command. None if failed.

        Raises
        ------
        KeyError : Exception
            If the command cannot be found for the resource.
        """
        parameters = []
        for r in filter(lambda x: x['name'] == name, self._resources):
            try:
                for p in r['commands'][command]:
                    if required_only:
                        if p['required']:
                            parameters.append(p['name'])
                    else:
                        parameters.append(p['name'])
            except KeyError as e:
                self._logger.error(f'Command "{command}" not found for '
                                   f'resource "{name}": {e}')
                raise e

        return parameters

    def _validate_instance(self, generator: str, parameters: dict) -> bool:
        # Verify if we have a generator implementation available
        if generator not in self._resources_all_names():
            return False

        init_params = self._resources_all_parameters_by_command(generator,
                                                                '__init__',
                                                                True)
        for p in init_params:
            if p == 'main_directory' or p == 'verbose':
                continue
            if p not in parameters:
                print(f'❌ Parameter "{p}" is missing for generator'
                      f' "{generator}"', file=sys.stderr)
                return False
        return True

    def list(self, scenario) -> list:
        """List all scenarios in file.

        Returns
        -------
        scenarios : list
            List of scenarios in file.
        """
        scenarios: list = []
        path = os.path.join(self._main_directory, scenario)

        if not os.path.exists(path):
            print(f'❌ "{scenario}" does not exist', file=sys.stderr)
            return []

        with open(path, 'r') as f:
            data = json.load(f)
            for s in data['instances']:
                scenarios.append(s['name'])

        return scenarios

    def _generate_scenario(self, scenario: dict) -> bool:
        """Generate a scenario.

        Parameters
        ----------
        scenario : dict
            Scenario description.

        Returns
        -------
        success : bool
            True if successfull, otherwise false.
        """
        generator: str = scenario['generator']
        parameters: dict = scenario['parameters']

        module = self._class_module_mapping[generator]
        cls = getattr(module, generator)(self._main_directory, self._verbose,
                                         **parameters)
        getattr(cls, 'generate')()

        return True

    def generate(self, scenario: str) -> bool:
        """Generate scenarios listed in supplied file.

        Parameters
        ----------
        scenario : str
            Path to file with scenarios to generate.

        Returns
        -------
        success : bool
            True if successfully generated, otherwise false.
        """
        if not os.path.exists(os.path.join(self._main_directory, scenario)):
            print(f'"{scenario}" does not exist', file=sys.stderr)
            return False

        path = os.path.join(self._main_directory, scenario)
        success: bool = True
        with open(path, 'r') as f:
            data = json.load(f)

        # Validate scenario instances
        try:
            jsonschema.validate(data, self._schema)
            for s in data['instances']:
                generator = s['generator']
                parameters = s['parameters']
                if not self._validate_instance(generator, parameters):
                    return False
            self._logger.debug('Scenario instances valid')
        except jsonschema.ValidationError:
            msg = f'{path}: JSON schema violation'
            self._logger.error(msg)
            return False

        # Generate instances
        self._logger.debug(f'Scenario: {data["name"]}')
        print('Generating scenario\'s instances:')
        for s in data['instances']:
            if not self._generate_scenario(s):
                print('    ❌ Failed to generate scenario'
                      f' "{s["name"]}"',
                      file=sys.stderr)
                success = False
            else:
                print(f'    ✅ {s["name"]}')

        return success
