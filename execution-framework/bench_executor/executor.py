#!/usr/bin/env python3

"""
This module holds the Executor class which is responsible for executing a case,
collecting metrics, and exposing this functionality to the CLI.
All features of this tool can be accessed through the Executor class, other
classes should not be used directly.
"""

import os
import sys
import json
import jsonschema
import importlib
import inspect
import shutil
from glob import glob
from datetime import datetime
from time import sleep
from typing import List, Dict, Any
from bench_executor.collector import Collector, METRICS_FILE_NAME
from bench_executor.stats import Stats
from bench_executor.logger import Logger, LOG_FILE_NAME

METADATA_FILE = 'metadata.json'
SCHEMA_FILE = 'metadata.schema'
CONFIG_DIR = os.path.join(os.path.dirname(__file__), 'config')
WAIT_TIME = 15  # seconds
CHECKPOINT_FILE_NAME = '.done'


# Dummy callback in case no callback was provided
def _progress_cb(resource: str, name: str, success: bool):
    pass


class Executor:
    """
    Executor class executes a case.
    """

    def __init__(self, main_directory: str, verbose: bool = False,
                 progress_cb=_progress_cb):
        """Create an instance of the Executor class.

        Parameters
        ----------
        main_directory : str
            The root directory of all the cases to execute.
        verbose : bool
            Enables verbose logs.
        process_cb : function
            Callback to call when a step is completed of the case. By default,
            a dummy callback is provided if the argument is missing.
        """
        self._main_directory = os.path.abspath(main_directory)
        self._schema = {}
        self._resources: List[Dict[str, Any]] = []
        self._class_module_mapping: Dict[str, Any] = {}
        self._verbose = verbose
        self._progress_cb = progress_cb
        self._logger = Logger(__name__, self._main_directory, self._verbose)

        self._init_resources()

        with open(os.path.join(os.path.dirname(__file__), 'data',
                               SCHEMA_FILE)) as f:
            self._schema = json.load(f)

    @property
    def verbose(self) -> bool:
        """Verbose logs enabled."""
        return self._verbose

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
                if name.startswith('_') or name[0].islower():
                    continue

                # Store class-module mapping for reverse look-up
                self._class_module_mapping[name] = imported_module

                # Discover all methods and their parameters in each class
                methods: Dict[str, List[Dict[str, str]]] = {}
                filt = filter(lambda x: '__init__' not in x,
                              inspect.getmembers(cls, inspect.isfunction))
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

    def _validate_case(self, case: dict, path: str) -> bool:
        """Validate a case's syntax.

        Verify if a case has a valid syntax or not. Report any errors
        discovered through logging and return if the validation succeeded or
        not.

        Parameters
        ----------
        case : dict
            The case to validate.
        path : str
            The file path to the case.

        Returns
        -------
        success : bool
            Whether the validation of the case succeeded or not.
        """
        try:
            # Verify schema
            jsonschema.validate(case, self._schema)

            # Verify values
            for step in case['steps']:
                # Check if resource is known
                names = self._resources_all_names()
                if step['resource'] not in names:
                    msg = f'{path}: Unknown resource "{step["resource"]}"'
                    self._logger.error(msg)
                    return False

                # Check if command is known
                r = step['resource']
                commands = self._resources_all_commands_by_name(r)
                if commands is None or step['command'] not in commands:
                    msg = f'{path}: Unknown command "{step["command"]}" ' + \
                          f'for resource "{step["resource"]}"'
                    self._logger.error(msg)
                    return False

                # Check if parameters are known
                r = step['resource']
                c = step['command']
                parameters = self._resources_all_parameters_by_command(r, c)
                if parameters is None:
                    return False

                for p in step['parameters'].keys():
                    if p not in parameters:
                        msg = f'{path}: Unkown parameter "{p}" for ' + \
                              f'command "{step["command"]}" of resource ' + \
                              f'"{step["resource"]}"'
                        self._logger.error(msg)
                        return False

                # Check if all required parameters are provided
                r = step['resource']
                c = step['command']
                parameters = \
                    self._resources_all_parameters_by_command(r, c, True)
                for p in parameters:
                    if p not in step['parameters'].keys():
                        msg = f'{path}: Missing required parameter "{p}" ' + \
                              f'for command "{step["command"]}" ' + \
                              f'of resource "{step["resource"]}"'
                        self._logger.error(msg)
                        return False

        except jsonschema.ValidationError:
            msg = f'{path}: JSON schema violation'
            self._logger.error(msg)
            return False

        return True

    def stats(self, case: dict) -> bool:
        """Generate statistics for a case.

        Generate statistics for an executed case. The case must be executed
        before to succeed.

        Parameters
        ----------
        case : dict
            The case to generate statistics for.

        Returns
        -------
        success : bool
            Whether the statistics are generated with success or not.

        """
        data = case['data']
        directory = case['directory']
        results_path = os.path.join(directory, 'results')

        if not os.path.exists(results_path):
            msg = f'Results do not exist for case "{data["name"]}"'
            self._logger.error(msg)
            return False

        stats = Stats(results_path, len(data['steps']), directory,
                      self._verbose)
        self._logger.info('Generating stats...')
        if not stats.statistics():
            return False

        self._logger.info('Generating aggregated data...')
        return stats.aggregate()

    def clean(self, case: dict) -> bool:
        """Clean a case.

        Clean up all results and metrics for a case to start it fresh.

        Parameters
        ----------
        case : dict
            The case to clean.

        Returns
        -------
        success : bool
            Whether the cleaning of the case succeeded or not.
        """
        # Checkpoints
        checkpoint_file = os.path.join(case['directory'], CHECKPOINT_FILE_NAME)
        if os.path.exists(checkpoint_file):
            os.remove(checkpoint_file)

        # Results: log files, metric measurements, run checkpoints
        for result_dir in glob(f'{case["directory"]}/results'):
            shutil.rmtree(result_dir)

        # Data: persistent storage
        for data_dir in glob(f'{case["directory"]}/data/*'):
            if not data_dir.endswith('shared'):
                shutil.rmtree(data_dir)

        return True

    def run(self, case: dict, interval: float,
            run: int, checkpoint: bool) -> bool:
        """Execute a case.

        Execute all steps of a case while collecting metrics and logs.
        The metrics are collected at a given interval and for a specific run of
        the case to allow multiple executions of the same case. Checkpoints of
        runs can be enabled to allow the executor to restart where it stopped
        in case of a failure, electricity blackout, etc.

        Parameters
        ----------
        case : dict
            The case to execute.
        interval : float
            The sample interval for the metrics collection.
        run : int
            The run number of the case.
        checkpoint : bool
            Enable checkpoints after each run to allow restarts.

        Returns
        -------
        success : bool
            Whether the case was executed successfully or not.
        """
        success = True
        data = case['data']
        directory = case['directory']
        data_path = os.path.join(directory, 'data')
        results_run_path = os.path.join(directory, 'results', f'run_{run}')
        checkpoint_file = os.path.join(directory, CHECKPOINT_FILE_NAME)
        run_checkpoint_file = os.path.join(results_run_path,
                                           CHECKPOINT_FILE_NAME)
        active_resources = []

        # Make sure we start with a clean setup before the first run
        if run == 1:
            self.clean(case)

        # create directories
        os.umask(0)
        os.makedirs(data_path, exist_ok=True)
        os.makedirs(results_run_path, exist_ok=True)

        # Initialize resources if needed
        # Some resources have to perform an initialization step such as
        # configuring database users, storage, etc. which is only done once
        for step in data['steps']:
            module = self._class_module_mapping[step['resource']]
            resource = getattr(module, step['resource'])(data_path, CONFIG_DIR,
                                                         directory,
                                                         self._verbose)
            if hasattr(resource, 'initialization'):
                if not resource.initialization():
                    self._logger.error('Failed to initialize resource '
                                       f'{step["resource"]}')
                    return False

                self._logger.debug(f'Resource {step["resource"]} initialized')
                self._progress_cb('Initializing', step['resource'], success)

        # Launch metrics collection
        collector = Collector(data['name'], results_run_path, interval,
                              len(data['steps']), run, directory,
                              self._verbose)

        # Execute steps
        for index, step in enumerate(data['steps']):
            success = True
            module = self._class_module_mapping[step['resource']]
            resource = getattr(module, step['resource'])(data_path, CONFIG_DIR,
                                                         directory,
                                                         self._verbose)
            active_resources.append(resource)

            # Containers may need to start up first before executing a command
            if hasattr(resource, 'wait_until_ready'):
                if not resource.wait_until_ready():
                    success = False
                    self._logger.error('Waiting until resource '
                                       f'"{step["resource"]} is ready failed')
                    self._progress_cb(step['resource'], step['name'], success)
                    break
                self._logger.debug(f'Resource {step["resource"]} ready')

            # Execute command
            command = getattr(resource, step['command'])
            if not command(**step['parameters']):
                success = False
                msg = f'Executing command "{step["command"]}" ' + \
                      f'failed for resource "{step["resource"]}"'
                # Some steps are non-critical like queries, they may fail but
                # should not cause a complete case failure. Allow these
                # failures if the may_fail key is present
                if step.get('may_fail', False):
                    self._logger.warning(msg)
                    self._progress_cb(step['resource'], step['name'], success)
                    continue
                else:
                    self._logger.error(msg)
                    self._progress_cb(step['resource'], step['name'], success)
                    break
            self._logger.debug(f'Command "{step["command"]}" executed on '
                               f'resource {step["resource"]}')

            # Step complete
            self._progress_cb(step['resource'], step['name'], success)

            # Step finished, let metric collector know
            if (index + 1) < len(data['steps']):
                collector.next_step()

        # Stop metrics collection
        collector.stop()

        # Stop active containers
        for resource in active_resources:
            if resource is not None and hasattr(resource, 'stop'):
                resource.stop()

        self._logger.debug('Cleaned up all resource')
        self._progress_cb('Cleaner', 'Clean up resources', True)

        # Mark checkpoint if necessary
        if checkpoint and success:
            self._logger.debug('Writing checkpoint...')
            with open(checkpoint_file, 'w') as f:
                d = datetime.now().replace(microsecond=0).isoformat()
                f.write(f'{d}\n')

        # Log file
        os.makedirs(os.path.join(results_run_path), exist_ok=True)
        shutil.move(os.path.join(directory, LOG_FILE_NAME),
                    os.path.join(results_run_path, LOG_FILE_NAME))
        self._logger.debug('Copied logs to run results path')

        # Metrics measurements
        for metrics_file in glob(f'{data_path}/*/{METRICS_FILE_NAME}'):
            subdir = metrics_file.replace(f'{data_path}/', '') \
                    .replace('/METRICS_FILE_NAME', '')
            os.makedirs(os.path.join(results_run_path, subdir), exist_ok=True)
            shutil.move(metrics_file, os.path.join(results_run_path, subdir,
                                                   METRICS_FILE_NAME))
        self._logger.debug('Copied metric measurements to run results path')

        # Results: all 'output_file' and 'result_file' values
        if success:
            self._logger.debug('Copying generated files for run')
            for step in data['steps']:
                subdir = step['resource'].lower().replace('_', '')
                parameters = step['parameters']
                os.makedirs(os.path.join(results_run_path, subdir),
                            exist_ok=True)
                if parameters.get('results_file', False):
                    results_file = parameters['results_file']
                    p1 = os.path.join(directory, 'data/shared', results_file)
                    p2 = os.path.join(results_run_path, subdir, results_file)
                    try:
                        shutil.move(p1, p2)
                    except FileNotFoundError as e:
                        msg = f'Cannot find results file "{p1}": {e}'
                        self._logger.warning(msg)

                if parameters.get('output_file', False) \
                        and not parameters.get('multiple_files', False):
                    output_dir = os.path.join(results_run_path, subdir)
                    for out_file in glob(os.path.join(str(directory), 'data',
                                         'shared', '*.nt')):
                        out_path = os.path.join(output_dir,
                                                os.path.basename(out_file))
                        try:
                            shutil.move(out_file, out_path)
                        except FileNotFoundError as e:
                            msg = f'Cannot find output file "{out_file}": {e}'
                            self._logger.warning(msg)

            # Run complete, mark it
            run_checkpoint_file = os.path.join(results_run_path,
                                               CHECKPOINT_FILE_NAME)
            self._logger.debug('Writing run checkpoint...')
            with open(run_checkpoint_file, 'w') as f:
                d = datetime.now().replace(microsecond=0).isoformat()
                f.write(f'{d}\n')

        self._logger.debug(f'Cooling down for {WAIT_TIME}s')
        self._progress_cb('Cooldown', f'Hardware cooldown period {WAIT_TIME}s',
                          True)
        sleep(WAIT_TIME)

        return success

    def list(self) -> list:
        """List all cases in a root directory.

            Retrieve a list of all discovered valid cases in a given directory.
            Cases which do not pass the validation, are excluded and their
            validation errors are reported through logging.

            Returns
            -------
            cases : list
                List of discovered cases.
        """
        cases = []

        for directory in glob(self._main_directory):
            for root, dirs, files in os.walk(directory):
                for file in files:
                    if os.path.basename(file) == METADATA_FILE:
                        path = os.path.join(root, file)
                        with open(path, 'r') as f:
                            data = json.load(f)
                            if self._validate_case(data, path):
                                cases.append({
                                    'directory': os.path.dirname(path),
                                    'data': data
                                })

        return cases
