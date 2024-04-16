#!/usr/bin/env python3

"""
This module holds the Container and ContainerManager classes. The Container
class is responsible for abstracting the Docker containers and allow running
containers easily and make sure they are initialized before using them.
The Containermanager class allows to create container networks, list all
running containers and stop them.
"""

from time import time, sleep
from typing import List, Tuple, Optional
from bench_executor.logger import Logger
from bench_executor.docker import Docker

WAIT_TIME = 1  # seconds
TIMEOUT_TIME = 600  # seconds
NETWORK_NAME = 'bench_executor'


class ContainerManager():
    """Manage containers and networks."""

    def __init__(self, docker: Docker):
        """Creates an instance of the ContainerManager class."""
        self._docker = docker

    def create_network(self, name: str):
        """Create a container network.

        Parameters
        ----------
        name : str
            Name of the network
        """
        self._docker.create_network(name)


class Container():
    """Container abstracts a Docker container

    Abstract how to run a command in a container, start or stop a container,
    or retrieve logs. Also allow to wait for a certain log entry to appear or
    exit successfully.
    """

    def __init__(self, container: str, name: str, logger: Logger,
                 ports: dict = {}, environment: dict = {},
                 volumes: List[str] = []):
        """Creates an instance of the Container class.

        Parameters
        ----------
        container : str
            Container ID.
        name : str
            Pretty name of the container.
        logger : Logger
            Logger class to use for container logs.
        ports : dict
            Ports mapping of the container onto the host.
        volumes : list
            Volumes mapping of the container onto the host.
        """
        self._docker = Docker(logger)
        self._manager = ContainerManager(self._docker)
        self._container_id: Optional[str] = None
        self._container_name = container
        self._name = name
        self._ports = ports
        self._volumes = volumes
        self._environment = environment
        self._proc_pid = None
        self._long_id = None
        self._cgroups_mode = None
        self._cgroups_dir = None
        self._started = False
        self._logger = logger

        # create network if not exist
        self._manager.create_network(NETWORK_NAME)

    @property
    def started(self) -> bool:
        """Indicates if the container is already started"""
        return self._started

    @property
    def name(self) -> str:
        """The pretty name of the container"""
        return self._name

    def run(self, command: str = '', detach=True) -> bool:
        """Run the container.

        This is used for containers which are long running to provide services
        such as a database or endpoint.

        Parameters
        ----------
        command : str
            The command to execute in the container, optionally and defaults to
            no command.
        detach : bool
            If the container may run in the background, default True.

        Returns
        -------
        success : bool
            Whether running the container was successfull or not.
        """
        e = self._environment
        v = self._volumes
        self._started, self._container_id = \
            self._docker.run(self._container_name, command, self._name, detach,
                             self._ports, NETWORK_NAME, e, v)

        if not self._started:
            self._logger.error(f'Starting container "{self._name}" failed!')
        return self._started

    def exec(self, command: str) -> Tuple[bool, List[str]]:
        """Execute a command in the container.

        Parameters
        ----------
        command : str
            The command to execute in the container.

        Returns
        -------
        success : bool
            Whether the command was executed successfully or not.
        logs : list
            The logs of the container for executing the command.
        """
        logs: List[str] = []

        if self._container_id is None:
            self._logger.error('Container is not initialized yet')
            return False, []
        exit_code = self._docker.exec(self._container_id, command)
        logs = self._docker.logs(self._container_id)
        if exit_code == 0:
            return True, logs

        return False, logs

    def run_and_wait_for_log(self, log_line: str, command: str = '') -> bool:
        """Run the container and wait for a log line to appear.

        This blocks until the container's log contains the `log_line`.

        Parameters
        ----------
        log_line : str
            The log line to wait for in the logs.
        command : str
            The command to execute in the container, optionally and defaults to
            no command.

        Returns
        -------
        success : bool
            Whether the container exited with status code 0 or not.
        """
        if not self.run(command):
            self._logger.error(f'Command "{command}" failed')
            return False

        if self._container_id is None:
            self._logger.error('Container is not initialized yet')
            return False

        start = time()
        found_line = False
        line_number = 0
        while (True):
            logs = self._docker.logs(self._container_id)
            for index, line in enumerate(logs):
                # Only print new lines when iterating
                if index > line_number:
                    line_number = index
                    self._logger.debug(line)

                if time() - start > TIMEOUT_TIME:
                    msg = f'Starting container "{self._name}" timed out!'
                    self._logger.error(msg)
                    break

                if log_line in line:
                    found_line = True
                    break

            if found_line:
                sleep(WAIT_TIME)
                return True

        # Logs are collected on success, log them on failure
        self._logger.error(f'Waiting for container "{self._name}" failed!')
        logs = self._docker.logs(self._container_id)
        for line in logs:
            self._logger.error(line)
        return False

    def run_and_wait_for_exit(self, command: str = '') -> bool:
        """Run the container and wait for exit

        This blocks until the container exit and gives a status code.

        Parameters
        ----------
        command : str
            The command to execute in the container, optionally and defaults to
            no command.

        Returns
        -------
       success : bool
            Whether the container exited with status code 0 or not.
        """
        if not self.run(command):
            return False

        if self._container_id is None:
            self._logger.error('Container is not initialized yet')
            return False

        status_code = self._docker.wait(self._container_id)
        logs = self._docker.logs(self._container_id)
        if logs is not None:
            for line in logs:
                # On success, logs are collected when the container is stopped.
                if status_code != 0:
                    self._logger.error(line)
                else:
                    self._logger.debug(line)

        if status_code == 0:
            self.stop()
            return True

        self._logger.error('Command failed while waiting for exit with status '
                           f'code: {status_code}')
        return False

    def stop(self) -> bool:
        """Stop a running container

        Stops the container and removes it, including its volumes.

        Returns
        -------
        success : bool
            Whether stopping the container was successfull or not.
        """

        if self._container_id is None:
            self._logger.error('Container is not initialized yet')
            return False

        self._docker.stop(self._container_id)
        return True
