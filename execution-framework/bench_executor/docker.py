#!/usr/bin/env python3

"""
This module holds the Docker class which implements the necessary API calls
for the Container class to control Docker containers. The docker-py module
which is similar has serious issues with resource leaking for years.
"""

import json
import subprocess
from time import sleep
from typing import List, Tuple
from bench_executor.logger import Logger


class Docker():
    """Client for the Docker CLI."""

    def __init__(self, logger: Logger):
        """Creates an instance of the Docker class.

        """
        self._logger = logger

    def exec(self, container_id: str, command: str) -> int:
        """Execute a command inside a running Docker container.

        Parameters
        ----------
        container_id : str
            ID of the Docker container.
        command : str
            Command to execute inside the Docker container.

        Returns
        -------
        status_code : int
            The exit status code of the executed command.
        """

        cmd = f'docker exec "{container_id}" {command}'
        self._logger.debug(f'Executing command in Docker container: {cmd}')
        status_code, output = subprocess.getstatusoutput(cmd)

        return status_code

    def wait(self, container_id: str) -> int:
        """Wait for Docker container to exit.

        Parameters
        ----------
        container_id : str
            ID of the Docker container.

        Returns
        -------
        status_code : int
            The exit status code of the Docker container.
        """

        cmd = f'docker wait "{container_id}"'
        self._logger.debug(f'Waiting for Docker container: {cmd}')
        status_code, output = subprocess.getstatusoutput(cmd)

        return status_code

    def stop(self, container_id: str) -> bool:
        """Stop a running Docker container.

        Parameters
        ----------
        container_id : str
            ID of the Docker container.

        Returns
        -------
        success : bool
            True if stopping the container was successful.
        """

        cmd = f'docker stop "{container_id}"'
        self._logger.debug(f'Stopping Docker container: {cmd}')
        status_code, output = subprocess.getstatusoutput(cmd)

        if status_code != 0:
            return False

        cmd = f'docker rm "{container_id}"'
        self._logger.debug(f'Removing Docker container: {cmd}')
        status_code, output = subprocess.getstatusoutput(cmd)

        return status_code == 0

    def logs(self, container_id: str) -> List[str]:
        """Retrieve the logs of a container.

        Parameters
        ----------
        container_id : str
            ID of the Docker container.

        Returns
        -------
        logs : List[str]
            List of loglines from the container.
        """

        cmd = f'docker logs "{container_id}"'
        status_code, output = subprocess.getstatusoutput(cmd)

        logs = []
        for line in output.split('\n'):
            logs.append(line.strip())

        return logs

    def pull(self, image: str) -> bool:
        """Pull a Docker image from DockerHub or other registries.

        If the image exists locally, pulling will be skipped without
        the force flag.

        Parameters
        ----------
        image : str
            Name of the Docker container image.

        Returns
        -------
        success : bool
            True if starting the container was successful.
        """
        # Check if the image already exists
        cmd = f'docker inspect "{image}"'
        status_code, output = subprocess.getstatusoutput(cmd)
        if status_code == 0:
            return True

        # Pull the image
        cmd = f'docker pull -q "{image}"'
        status_code, output = subprocess.getstatusoutput(cmd)
        return status_code == 0

    def run(self, image: str, command: str, name: str, detach: bool,
            ports: dict, network: str, environment: dict,
            volumes: List[str], must_pull: bool = True) -> Tuple[bool, str]:
        """Start a Docker container.

        Parameters
        ----------
        image : str
            Name of the Docker container image.
        command : str
            Command to execute in the Docker container.
        name : str
            Canonical name to assign to the container.
        detach : bool
            Whether to detach from the container or not.
        ports : dict
            Ports to expose from the container to the host.
        network : str
            Name of the Docker network to attach the container to.
        environment : dict
            Environment variables to set.
        volumes : List[str]
            Volumes to mount on the container from the host.
        must_pull: bool
            Whether the image should be pulled first, default is True.

        Returns
        -------
        success : bool
            True if starting the container was successful.
        container_id : str
            ID of the container that was started.
        """

        # Make sure the image is available locally
        if must_pull:
            self.pull(image)

        # Avoid race condition between removing and starting the same container
        removing = False
        while (True):
            cmd = f'docker ps -a | grep "{name}"'
            status_code, output = subprocess.getstatusoutput(cmd)
            if status_code == 0 and not removing:
                cmd = f'docker stop "{name}" && docker rm "{name}"'
                subprocess.getstatusoutput(cmd)
                self._logger.debug(f'Schedule container "{name}" for removal')
                removing = True
            elif status_code != 0:
                break
            sleep(0.1)

        # Start container
        cmd = f'docker run --name "{name}"'
        if detach:
            cmd += ' --detach'
        for variable, value in environment.items():
            cmd += f' --env "{variable}={value}"'
        for host_port, container_port in ports.items():
            cmd += f' -p "{host_port}:{container_port}"'
        for volume in volumes:
            cmd += f' -v "{volume}"'
        cmd += f' --network "{network}"'
        cmd += f' {image} {command}'
        self._logger.debug(f'Starting Docker container: {cmd}')
        status_code, container_id = subprocess.getstatusoutput(cmd)
        container_id = container_id.strip()
        self._logger.debug(f'Container "{container_id}" running')

        return status_code == 0, container_id

    def create_network(self, network: str) -> bool:
        """Create a Docker container network.

        If the network already exist, it will not be recreated.

        Parameters
        ----------
        network : str
            Name of the network.

        Returns
        -------
        success : bool
            True if the network was created
        """

        # Check if network exist
        cmd = f'docker network ls | grep "{network}"'
        status_code, output = subprocess.getstatusoutput(cmd)
        if status_code == 0:
            return True

        # Create it as it does not exist yet
        cmd = f'docker network create "{network}"'
        status_code, output = subprocess.getstatusoutput(cmd)
        self._logger.debug(f'Created network "{network}"')

        return status_code == 0

    def info(self) -> Tuple[bool, dict]:
        """Dump the Docker daemon system information.

        Returns
        -------
        success : bool
            True if the command succeed.
        info : dict
            Docker daemon system information as dictionary.
        """

        # Check if network exist
        cmd = 'docker info --format \'{{json .}}\''
        status_code, output = subprocess.getstatusoutput(cmd)

        if status_code != 0:
            return False, {}

        try:
            info = json.loads(output)
        except json.decoder.JSONDecodeError as e:
            self._logger.error('Unable to extract Docker daemon system information.'
                               'Do you have access to Docker?')
            self._logger.debug(f'Docker daemon JSON response:\n{output}')
            raise e

        self._logger.debug('Docker daemon system information successfully')
        return True, info
