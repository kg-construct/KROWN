#!/usr/bin/env python3
"""
This module holds the Collector class which is responsible for collecting
metrics during the execution of a case. It also collects hardware information
for provenance reasons when comparing results from cases.

The following metrics are collected:

**General**
- `name`: name of the case being executed.
- `index`: incremental index for each collected sample.
- `step`: Number of the step of a collected sample.
- `timestamp`: The time when the sample was collected.
- `version`: format version of the collected version, currently v2.

**CPU**
- `cpu_user`: CPU time spent in userspace.
- `cpu_system`: CPU time spent in kernelspace.
- `cpu_user_system`: sum of CPU time userspace and kernelspace.
- `cpu_idle`: CPU time spent in idle mode.
- `cpu_iowait`: Time that the CPU has to wait for IO operations to complete.

**Memory**
- `memory_ram`: Amount of RAM memory in use.
- `memory_swap`: Amount of SWAP memory in use.
- `memory_ram_swap`: Sum of the RAM and SWAP memory in use.

**Disk**
- `disk_read_count`: Number of disk reads.
- `disk_write_count`: Number of disk writes.
- `disk_read_bytes`: Number of bytes read from disk.
- `disk_write_bytes`: Number of bytes written to disk.
- `disk_read_time`: Time spent to read from disk.
- `disk_write_time`: Time spent to write to disk.
- `disk_busy_time`: Time that the disk is busy and all actions are pending.

**Network**
- `network_received_count`: Number of network packets received.
- `network_sent_count`: Number of network packets sent.
- `network_received_bytes`: Number of bytes received over network.
- `network_sent_bytes`: Number of bytes sent over network.
- `network_received_error`: Number of errors occured during receiving over
network.
- `network_sent_error`: Number of errors occured during sending over network.
- `network_received_drop`: Number of packets dropped during receiving over
network.
- `network_sent_drop`: Number of packets dropped during sending over network.
"""

import os
import platform
import psutil as ps
from csv import DictWriter
from datetime import datetime, timezone
from time import time, sleep
from subprocess import run, CalledProcessError
from threading import Thread, Event
from typing import TYPE_CHECKING, Dict, Union, Optional, List
from bench_executor.logger import Logger
from bench_executor.docker import Docker

# psutil types are platform specific, provide stubs at runtime as checking is
# not done there
if TYPE_CHECKING:
    from psutil._common import sswap, snetio
    from psutil._pslinux import svmem, sdiskio
    from psutil._psaix import scputimes
else:
    from collections import namedtuple
    scputimes = namedtuple('scputimes', [])
    sswap = namedtuple('sswap', [])
    svmem = namedtuple('svmem', [])
    sdiskio = namedtuple('sdiskio', [])
    snetio = namedtuple('snetio', [])

#
# Hardware and case information is logged to 'case-info.txt' on construction.
#
# All data are stored in a CSV as 'stats.csv'.
# These data are accumulated among all CPU cores, all memory banks, all network
# interfaces, etc. individual devices are not logged.
#

CASE_INFO_FILE_NAME: str = 'case-info.txt'
METRICS_FILE_NAME: str = 'metrics.csv'
METRICS_VERSION: int = 3
FIELDNAMES: List[str] = [
    'name',
    'run',
    'index',
    'step',
    'timestamp',
    'version',
    'cpu_user',
    'cpu_system',
    'cpu_user_system',
    'cpu_idle',
    'cpu_iowait',
    'memory_ram',
    'memory_swap',
    'memory_ram_swap',
    'disk_read_count',
    'disk_write_count',
    'disk_read_bytes',
    'disk_write_bytes',
    'disk_read_time',
    'disk_write_time',
    'disk_busy_time',
    'network_received_count',
    'network_sent_count',
    'network_received_bytes',
    'network_sent_bytes',
    'network_received_error',
    'network_sent_error',
    'network_received_drop',
    'network_sent_drop'
]
ROUND: int = 4

step_id: int = 1


def _collect_metrics(stop_event: Event, name: str, run: int, metrics_path: str,
                     sample_interval: float, initial_timestamp: float,
                     initial_cpu: scputimes, initial_ram: svmem,
                     initial_swap: sswap, initial_disk_io: Optional[sdiskio],
                     initial_network_io: snetio):
    """Thread function to collect a sample at specific intervals"""
    global step_id
    index = 1
    row: Dict[str, Union[int, float, str]]

    # Create metrics file
    with open(metrics_path, 'w') as f:
        writer = DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()

        # Initial values
        row = {
            'name': name,
            'run': run,
            'index': index,
            'step': step_id,
            'timestamp': 0.0,
            'version': METRICS_VERSION,
            'cpu_user': 0.0,
            'cpu_system': 0.0,
            'cpu_user_system': 0.0,
            'cpu_idle': 0.0,
            'cpu_iowait': 0.0,
            'memory_ram': 0,
            'memory_swap': 0,
            'memory_ram_swap': 0,
            'disk_read_count': 0,
            'disk_write_count': 0,
            'disk_read_bytes': 0,
            'disk_write_bytes': 0,
            'disk_read_time': 0,
            'disk_write_time': 0,
            'disk_busy_time': 0,
            'network_received_count': 0,
            'network_sent_count': 0,
            'network_received_bytes': 0,
            'network_sent_bytes': 0,
            'network_received_error': 0,
            'network_sent_error': 0,
            'network_received_drop': 0,
            'network_sent_drop': 0
        }
        writer.writerow(row)
        index += 1
        sleep(sample_interval - (initial_timestamp - time()))

        while not stop_event.wait(0):
            # Collect metrics
            timestamp = time()
            cpu: scputimes = ps.cpu_times()
            ram: svmem = ps.virtual_memory()
            swap: sswap = ps.swap_memory()
            disk_io: Optional[sdiskio] = ps.disk_io_counters()  # type: ignore
            network_io: snetio = ps.net_io_counters()

            # Write to file
            diff = round(timestamp - initial_timestamp, ROUND)
            cpu_user = round(cpu.user - initial_cpu.user, ROUND)
            cpu_system = round(cpu.system - initial_cpu.system, ROUND)
            cpu_idle = round(cpu.idle - initial_cpu.idle, ROUND)
            cpu_iowait = round(cpu.iowait - initial_cpu.iowait, ROUND)
            network_recv_count = \
                network_io.packets_recv - initial_network_io.packets_recv
            network_sent_count = \
                network_io.packets_sent - initial_network_io.packets_sent
            network_recv_bytes = \
                network_io.bytes_recv - initial_network_io.bytes_recv
            network_sent_bytes = \
                network_io.bytes_sent - initial_network_io.bytes_sent
            network_errin = \
                network_io.errin - initial_network_io.errin
            network_errout = \
                network_io.errout - initial_network_io.errout
            network_dropin = \
                network_io.dropin - initial_network_io.dropin
            network_dropout = \
                network_io.dropout - initial_network_io.dropout

            row = {
                'name': name,
                'run': run,
                'index': index,
                'step': step_id,
                'timestamp': diff,
                'version': METRICS_VERSION,
                'cpu_user': cpu_user,
                'cpu_system': cpu_system,
                'cpu_user_system': cpu_user + cpu_system,
                'cpu_idle': cpu_idle,
                'cpu_iowait': cpu_iowait,
                'memory_ram': ram.used,
                'memory_swap': swap.used,
                'memory_ram_swap': ram.used + swap.used,
                'network_received_count': network_recv_count,
                'network_sent_count': network_sent_count,
                'network_received_bytes': network_recv_bytes,
                'network_sent_bytes': network_sent_bytes,
                'network_received_error': network_errin,
                'network_sent_error': network_errout,
                'network_received_drop': network_dropin,
                'network_sent_drop': network_dropout
            }

            # Diskless machines will return None for diskio
            if disk_io is not None and initial_disk_io is not None:
                row['disk_read_count'] = \
                   disk_io.read_count - initial_disk_io.read_count
                row['disk_write_count'] = \
                    disk_io.write_count - initial_disk_io.write_count
                row['disk_read_bytes'] = \
                    disk_io.read_bytes - initial_disk_io.read_bytes
                row['disk_write_bytes'] = \
                    disk_io.write_bytes - initial_disk_io.write_bytes
                row['disk_read_time'] = \
                    disk_io.read_time - initial_disk_io.read_time
                row['disk_write_time'] = \
                    disk_io.write_time - initial_disk_io.write_time
                row['disk_busy_time'] = \
                    disk_io.busy_time - initial_disk_io.busy_time
            writer.writerow(row)
            index += 1

            # Honor sample time, remove metrics logging overhead
            sleep(sample_interval - (timestamp - time()))


class Collector():
    """Collect metrics samples at a given interval for a run of a case."""

    def __init__(self, case_name: str, results_run_path: str,
                 sample_interval: float, number_of_steps: int, run_id: int,
                 directory: str, verbose: bool):
        """
        Create an instance of the Collector class.

        Instantiating this class will automatically generate a `case-info.txt`
        file which describes the hardware used during collection of the
        metrics. The file describes:

        - **Case**:
            - Name of the case.
            - Timestamp when started.
            - Directory of the case.
            - Number of the run.
            - Number of steps in a case.
        - **Hardware**:
            - CPU name.
            - Number of CPU cores.
            - Minimum and maximum CPU core frequency.
            - Amount of RAM and SWAP memory
            - Available disk storage.
            - Available network interfaces and their link speed.
        - **Docker**:
            - Version of the Docker daemon
            - Docker root directory
            - Docker storage driver
            - Docker CgroupFS driver and version

        Parameters
        ----------
        case_name : str
            Name of the case being executed.
        results_run_path : str
            Path to the results directory of the run currently being executed.
        sample_interval : float
            Sample interval in seconds for collecting metrics.
        number_of_steps : int
            The number of steps of the case that is being executed.
        run_id : int
            The number of the run that is being executed.
        directory : str
            Path to the directory to store logs.
        verbose : bool
            Enable verbose logs.
        """

        self._started: bool = False
        self._data_path: str = os.path.abspath(results_run_path)
        self._number_of_steps: int = number_of_steps
        self._stop_event: Event = Event()
        self._logger = Logger(__name__, directory, verbose)
        self._docker = Docker(self._logger)

        # Only Linux is supported
        if platform.system() != 'Linux':
            msg = f'"{platform.system()} is not supported as OS'
            self._logger.error(msg)
            raise ValueError(msg)

        # Initialize step ID
        global step_id
        step_id = 1

        # System information: OS, kernel, architecture
        system_hostname = 'UNKNOWN'
        system_os_name = 'UNKNOWN'
        system_os_version = 'UNKNOWN'
        try:
            system_os_name = platform.freedesktop_os_release()['NAME']
            system_os_version = platform.freedesktop_os_release()['VERSION']
        except (OSError, KeyError):
            self._logger.warning('Cannot extract Freedesktop OS release data')
        system_hostname = platform.node()
        system_kernel = platform.platform()
        system_architecture = platform.uname().machine

        # CPU information: name, max frequency, core count
        cpu_name = 'UNKNOWN'
        try:
            raw = run(['lscpu'], capture_output=True)
            for line in raw.stdout.decode('utf-8').split('\n'):
                if 'Model name:' in line:
                    cpu_name = line.split(':')[1].strip()
                    break
        except CalledProcessError as e:
            self._logger.warning('Unable to determine CPU processor name: '
                                 f'{e}')

        cpu_cores = ps.cpu_count()
        cpu_min_freq = ps.cpu_freq().min
        cpu_max_freq = ps.cpu_freq().max

        # Memory information: RAM total, SWAP total
        memory_total = ps.virtual_memory().total
        swap_total = ps.swap_memory().total

        # Disk IO: name
        partitions: Dict[str, int] = {}
        for disk in ps.disk_partitions():
            # Skip Docker's overlayFS
            if disk.fstype and 'docker' not in disk.mountpoint:
                total = ps.disk_usage(disk.mountpoint).total
                partitions[disk.mountpoint] = total

        # Network IO: name, speed, MTU
        network_interfaces = ps.net_if_stats()

        # Docker daemon: version, storage driver, cgroupfs
        success, docker_info = self._docker.info()
        if not success:
            self._logger.error('Failed to retrieve Docker daemon information')

        # Write machine information to disk
        case_info_file = os.path.join(self._data_path, CASE_INFO_FILE_NAME)
        with open(case_info_file, 'w') as f:
            f.write('===> CASE <===\n')
            f.write(f'Name: {case_name}\n')
            f.write(f'Timestamp: {datetime.now(timezone.utc).isoformat()}\n')
            f.write(f'Directory: {directory}\n')
            f.write(f'Run: {run_id}\n')
            f.write(f'Number of steps: {self._number_of_steps}\n')
            f.write('\n')
            f.write('===> HARDWARE <===\n')
            f.write('System\n')
            f.write(f'\tHostname: {system_hostname}\n')
            f.write(f'\tOS name: {system_os_name}\n')
            f.write(f'\tOS version: {system_os_version}\n')
            f.write(f'\tKernel: {system_kernel}\n')
            f.write(f'\tArchitecture: {system_architecture}\n')
            f.write('CPU\n')
            f.write(f'\tName: {cpu_name}\n')
            f.write(f'\tCores: {cpu_cores}\n')
            f.write(f'\tMinimum frequency: {int(cpu_min_freq)} Hz\n')
            f.write(f'\tMaximum frequency: {int(cpu_max_freq)} Hz\n')
            f.write('Memory\n')
            f.write(f'\tRAM memory: {int(memory_total / 10 ** 6)} MB\n')
            f.write(f'\tSWAP memory: {int(swap_total / 10 ** 6)} MB\n')
            f.write('Storage\n')
            for disk_name, size in partitions.items():
                f.write(f'\tDisk "{disk_name}": '
                        f'{round(size / 10 ** 9, 2)} GB\n')
            f.write('Network\n')
            for interface_name, stats in network_interfaces.items():
                speed = stats.speed
                if speed == 0:
                    f.write(f'\tInterface "{interface_name}"\n')
                else:
                    f.write(f'\tInterface "{interface_name}": {speed} mbps\n')

            f.write('\n')
            f.write('===> DOCKER <===\n')
            f.write('Version: '
                    f'{docker_info.get("ServerVersion", "UNKNOWN")}\n')
            f.write('Root directory: '
                    f'{docker_info.get("DockerRootDir", "UNKNOWN")}\n')
            f.write('Drivers:\n')
            f.write('\tStorage: '
                    f'{docker_info.get("Driver", "UNKNOWN")}\n')
            f.write('\tCgroupFS: '
                    f'{docker_info.get("CgroupDriver", "UNKNOWN")} '
                    f'v{docker_info.get("CgroupVersion", "UNKNOWN")}\n')

        # Set initial metric values and start collection thread
        metrics_path = os.path.join(results_run_path, METRICS_FILE_NAME)
        initial_timestamp = time()
        initial_cpu = ps.cpu_times()
        initial_ram = ps.virtual_memory().used
        initial_swap = ps.swap_memory().used
        initial_disk_io = ps.disk_io_counters()
        initial_network_io = ps.net_io_counters()
        self._thread: Thread = Thread(target=_collect_metrics,
                                      daemon=True,
                                      args=(self._stop_event,
                                            case_name,
                                            run_id,
                                            metrics_path,
                                            sample_interval,
                                            initial_timestamp,
                                            initial_cpu,
                                            initial_ram,
                                            initial_swap,
                                            initial_disk_io,
                                            initial_network_io))
        self._thread.start()

    @property
    def name(self):
        """Name of the class: Collector"""
        return self.__class__.__name__

    def next_step(self):
        """Increment the step number by one.

        The step number must always be equal or lower than the number of steps
        in the case.
        """
        global step_id
        step_id += 1

        msg = f'Step ({step_id}) is higher than number of steps ' + \
              f'({self._number_of_steps})'
        assert (step_id <= self._number_of_steps), msg

    def stop(self):
        """End metrics collection.

        Signal the metrics collection thread to stop collecting any metrics.
        """
        self._stop_event.set()
