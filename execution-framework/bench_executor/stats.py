#!/usr/bin/env python3
"""
This module holds the Stats class which is responsible for generating
staticstics from executed cases. It will automatically aggregate all runs of an
executed case to generate an `aggregated.csv` and `summary.csv` files which can
be used to compare various cases with each other.

- `aggregated.csv`: For each run of a case, the median execution time of each
  step is calculated. For each step, the results of the run with the median
  execution time is used to assemble the aggregated results.
- `summary.csv`: The summary is similar to the previous file, but provides a
  single result for each step to immediately see how long the step took, how
  many samples are provided for the step, etc.
"""

import os
import psutil
from glob import glob
from statistics import median, stdev, mean
from csv import DictWriter, DictReader
from typing import List, Optional
from bench_executor.collector import FIELDNAMES, METRICS_FILE_NAME
from bench_executor.logger import Logger

METRICS_AGGREGATED_FILE_NAME = 'aggregated.csv'
METRICS_SUMMARY_FILE_NAME = 'summary.csv'
METRICS_STATS_FILE_NAME = 'stats.csv'
FIELDNAMES_STRING = ['name']
FIELDNAMES_FLOAT = ['timestamp', 'cpu_user', 'cpu_system', 'cpu_idle',
                    'cpu_iowait', 'cpu_user_system']
FIELDNAMES_INT = ['run', 'index', 'step', 'version', 'memory_ram',
                  'memory_swap', 'memory_ram_swap', 'disk_read_count',
                  'disk_write_count', 'disk_read_bytes', 'disk_write_bytes',
                  'disk_read_time', 'disk_write_time', 'disk_busy_time',
                  'network_received_count', 'network_sent_count',
                  'network_received_bytes', 'network_sent_bytes',
                  'network_received_error', 'network_sent_error',
                  'network_received_drop', 'network_sent_drop']
FIELDNAMES_SUMMARY = [
    'name',
    'run',
    'number_of_samples',
    'step',
    'duration',
    'version',
    'cpu_user_diff',
    'cpu_system_diff',
    'cpu_user_system_diff',
    'cpu_idle_diff',
    'cpu_iowait_diff',
    'memory_ram_max',
    'memory_swap_max',
    'memory_ram_swap_max',
    'memory_ram_min',
    'memory_swap_min',
    'memory_ram_swap_min',
    'disk_read_count_diff',
    'disk_write_count_diff',
    'disk_read_bytes_diff',
    'disk_write_bytes_diff',
    'disk_read_time_diff',
    'disk_write_time_diff',
    'disk_busy_time_diff',
    'network_received_count_diff',
    'network_sent_count_diff',
    'network_received_bytes_diff',
    'network_sent_bytes_diff',
    'network_received_error_diff',
    'network_sent_error_diff',
    'network_received_drop_diff',
    'network_sent_drop_diff'
]
ROUND = 4

#
# Generate stats from the result runs by aggregating it on
# median execution time for each step. Processing is done for each step per
# run and unnecessary values are skipped to reduce the memory consumption.
#
# The median run is available in 'aggregated.csv' while a summarized version
# which only reports the diff or max value of each step in 'summary.csv'
#


class Stats():
    """Generate statistics for an executed case."""

    def __init__(self, results_path: str, number_of_steps: int,
                 directory: str, verbose: bool):
        """Create an instance of the Stats class.

        Parameters
        ----------
        results_path : str
            The path to the results directory of the case
        number_of_steps : int
            The number of steps of the case
        directory : str
            The path to the directory where the logs must be stored.
        verbose : bool
            Enable verbose logs.
        """
        self._results_path: str = os.path.abspath(results_path)
        self._number_of_steps: int = number_of_steps
        self._logger = Logger(__name__, directory, verbose)
        self._parsed_data: dict = {}

        if not os.path.exists(results_path):
            msg = f'Results do not exist: {results_path}'
            self._logger.error(msg)
            raise ValueError(msg)

    def _parse_field(self, field, value):
        """Parse the field of the metrics field in a Python data type."""
        try:
            if field in FIELDNAMES_FLOAT:
                return float(value)
            elif field in FIELDNAMES_INT:
                return int(value)
            elif field in FIELDNAMES_STRING:
                return str(value)
            else:
                msg = f'Field "{field}" type is unknown'
                self._logger.error(msg)
                raise ValueError(msg)
        except TypeError:
            return -1

    def _parse_v2(self, run_path: str, fields: list = FIELDNAMES,
                  step: Optional[int] = None):
        """Parse the CSV metrics file in v2 format."""
        data = []

        # Drop cache if memory usage is too high
        used_memory = psutil.virtual_memory().percent
        if used_memory > 85.0:
            self._logger.debug('Releasing memory of cache...')
            del self._parsed_data
            self._parsed_data = {}

        # Pull data from cache if available
        if run_path in self._parsed_data:
            if step is not None:
                return list(filter(lambda x: x['step'] == step,
                                   self._parsed_data[run_path]))
            return self._parsed_data[run_path]

        metrics_file = os.path.join(run_path, METRICS_FILE_NAME)
        if not os.path.exists(metrics_file):
            self._logger.error(f'Metrics file "{metrics_file}" does not exist')
            return []

        # Filter the fields we want from above, this way we don't load all
        # the data in memory during processing.
        self._logger.debug('Reading metrics file...')
        with open(metrics_file, 'r') as f:
            reader = DictReader(f)
            for line in reader:
                corrupt: bool = False

                # Filter on field names
                filtered: dict = {}
                for key in fields:
                    if key in line:
                        filtered[key] = line[key]

                entry = {}
                for key, value in filtered.items():
                    v = self._parse_field(key, value)
                    if v == -1:
                        corrupt = True
                        msg = f'Corrupt entry {key} with value {value} in ' + \
                              f'{metrics_file}, skipped'
                        self._logger.info(msg)
                        break

                    entry[key] = v

                if not corrupt:
                    data.append(entry)

        self._parsed_data[run_path] = data
        if step is not None:
            return list(filter(lambda x: x['step'] == step, data))

        return data

    def statistics(self) -> bool:
        """Calculate basic statistics on the steps by aggregating them from
        all runs and applying standard deviation, median, min, max, mean for
        each measured metric.

        Returns
        -------
        success : bool
            Whether the standard deviation calculation was successfully or not.
        """
        summary_by_step: dict = {}
        stats: list = []

        for run_path in glob(f'{self._results_path}/run_*/'):
            for step_index in range(self._number_of_steps):
                step_data = self._parse_v2(run_path,
                                           step=step_index + 1)
                # If a step failed and no data is available, do not crash
                if not step_data:
                    continue

                for field in FIELDNAMES:
                    if f'step_{step_index}' not in summary_by_step:
                        summary_by_step[f'step_{step_index}'] = {
                            'step': step_index,
                            'name': None,
                            'version': None,
                            'duration': [],
                            'number_of_samples': [],
                        }
                    sbs = summary_by_step[f'step_{step_index}']

                    # Some fields are not present on v2 while they are in v3+
                    if field not in step_data[0]:
                        continue

                    if 'memory' in field:
                        if f'{field}_min' not in sbs:
                            sbs[f'{field}_min'] = []
                        if f'{field}_max' not in sbs:
                            sbs[f'{field}_max'] = []
                    elif not any(name in field for name in ['index', 'version',
                                                            'step', 'name',
                                                            'run',
                                                            'timestamp']):
                        if f'{field}_diff' not in sbs:
                            sbs[f'{field}_diff'] = []

                    # Report max memory peak for this step
                    if 'memory' in field:
                        values = []
                        for data in step_data:
                            values.append(data[field])
                        sbs[f'{field}_min'].append(min(values))
                        sbs[f'{field}_max'].append(max(values))
                    # Skip fields which are not applicable
                    elif field in ['run']:
                        continue
                    # Leave some fields like they are
                    elif field in ['version', 'step', 'name']:
                        sbs[field] = step_data[0][field]
                    # All other fields are accumulated data values for which we
                    # report the diff for the step
                    else:
                        first = step_data[0][field]
                        last = step_data[-1][field]
                        diff = round(last - first, ROUND)
                        if field == 'index':
                            # diff will be 0 for 1 sample, but we have this
                            # sample, so include it
                            sbs['number_of_samples'].append(diff + 1)
                        elif field == 'timestamp':
                            sbs['duration'].append(diff)
                        else:
                            sbs[f'{field}_diff'].append(diff)

        stats_fieldnames = []
        for step in summary_by_step:
            stats_step = {}
            for field in summary_by_step[step]:
                if any(name in field for name in ['index', 'version', 'step',
                                                  'name', 'run', 'timestamp']):
                    stats_step[field] = summary_by_step[step][field]
                    if field not in stats_fieldnames:
                        stats_fieldnames.append(field)
                    continue

                if f'{field}_median' not in stats_fieldnames:
                    stats_fieldnames.append(f'{field}_median')
                    stats_fieldnames.append(f'{field}_average')
                    stats_fieldnames.append(f'{field}_max')
                    stats_fieldnames.append(f'{field}_min')
                    stats_fieldnames.append(f'{field}_stdev')
                    stats_fieldnames.append(f'{field}_values')

                try:
                    field_values = summary_by_step[step][field]
                    stats_step[f'{field}_median'] = median(field_values)
                    stats_step[f'{field}_average'] = mean(field_values)
                    stats_step[f'{field}_max'] = max(field_values)
                    stats_step[f'{field}_min'] = min(field_values)
                    stats_step[f'{field}_stdev'] = stdev(field_values)
                    stats_step[f'{field}_values'] = field_values
                except Exception as e:
                    print(step, field, summary_by_step[step][field])
                    self._logger.error(f'Generating stats failed: {e}')
            stats.append(stats_step)

        stats_file = os.path.join(self._results_path,
                                  METRICS_STATS_FILE_NAME)
        self._logger.debug('Generated stats')

        with open(stats_file, 'w') as f:
            writer = DictWriter(f, fieldnames=stats_fieldnames)
            writer.writeheader()
            for step in stats:
                writer.writerow(step)

        return True

    def aggregate(self) -> bool:
        """Aggregate the metrics of the different runs of a case.

        Find the median execution time of each step across all runs and extract
        the step from the run which has this median execution time to assemble
        an aggregated version and summary version of the case's metrics.

        Returns
        -------
        success : bool
            Whether the aggregation was successfully or not.
        """
        # Find each median step of all runs before extracting more data for
        # memory consumption reasons
        runs = []
        for run_path in glob(f'{self._results_path}/run_*/'):
            # Extract run number
            try:
                run_folder: str = os.path.split(os.path.dirname(run_path))[-1]
                run_id: int = int(run_folder.replace('run_', ''))
            except ValueError:
                self._logger.error(f'Run "{run_id}" is not a number')
                return False

            # Extract steps and timestamps of this run.
            # v3 is the same as v2 with an additional field
            data = self._parse_v2(run_path)
            self._logger.debug(f'Parsed metrics of run {run_id}')

            # Calculate timestamp diff for each step
            step = 1
            timestamps = []
            step_end = 0.0
            step_begin = 0.0
            for entry in data:
                entry_step = entry['step']
                assert (entry_step >= step), 'Entry step decreased over time'

                # Next step
                if entry_step > step:
                    if entry_step - step > 1:
                        self._logger.warning(f"{entry_step - step} step(s) "
                                             "are missing between steps "
                                             f"[{step},{entry_step}]. "
                                             "Try increasing the sample time "
                                             "and re-run.")
                    # Calculate diff of current step if at least 2 entries
                    # for the step exist, if not the diff is 0.0 and we fall
                    # back to the step_begin timestamp which will make sure we
                    # use the run with the timestamp that is the median of all
                    # runs. For example: [4.5, 5.0, 6.5] will return run 2 as
                    # 5.0 is the median.
                    diff = step_end - step_begin
                    if diff == 0.0:
                        self._logger.warning(f'Only 1 entry for step {step} '
                                             f'found, falling back to median '
                                             f'timestamp instead of diff')
                        diff = step_begin

                    timestamps.append(diff)

                    # Reset for next step
                    step = entry_step
                    step_begin = entry['timestamp']
                    step_end = entry['timestamp']
                # step_end keeps increasing until the step changes
                else:
                    step_end = entry['timestamp']
            # Final step does not cause an increment, add manually
            timestamps.append(step_end - step_begin)
            runs.append((run_id, timestamps))

            self._logger.debug('Timestamp difference between steps calculated')

        # Statistics rely on uneven number of runs
        assert (len(runs) % 2 != 0), 'Number of runs should never be even'

        # Runs are unsorted as glob does not have a fixed order, sort them
        # based on run number in tuple
        runs.sort(key=lambda element: element[0])
        self._logger.debug('Sorting runs complete')

        # Find median for each step across runs
        timestamps_by_step: List[List[float]] = []
        for step_index in range(self._number_of_steps):
            timestamps_by_step.append([])

        for run in runs:
            run_id = run[0]
            timestamps = run[1]

            # Do not process incomplete runs
            if (len(timestamps) != self._number_of_steps):
                msg = f'Number of steps ({self._number_of_steps}) does ' + \
                      'not match with extracted steps of ' + \
                      f'run ({len(timestamps)}). Skipping run {run_id}'
                self._logger.warning(msg)
                continue

            # Create list of timestamps for each step from all runs
            for step_index in range(self._number_of_steps):
                timestamps_by_step[step_index].append(timestamps[step_index])
        self._logger.debug('Extracted median')

        # Create a list of our steps with the run_id which has the median value
        # for that step
        aggregated_entries = []
        summary_entries = []
        index_number = 1
        for step_index, step_timestamps in enumerate(timestamps_by_step):
            # If we do not have a single timestamp for a step, we cannot
            # process the data. This can happen when the steps are processed
            # faster than the configured sample time.
            if not step_timestamps:
                self._logger.error("Unable to aggregate because some steps "
                                   "have no measurements")
                return False

            # We ensure that the number of runs is always uneven so the median
            # is always a measured data point instead of the average of 2 data
            # points with even number of runs
            try:
                median_run_id = timestamps_by_step[step_index] \
                    .index(median(step_timestamps)) + 1
            except ValueError:
                continue
            median_run_path = os.path.join(self._results_path,
                                           f'run_{median_run_id}')
            median_step_data = self._parse_v2(median_run_path,
                                              step=step_index + 1)

            # Rewrite indexes to match new number of samples
            for entry in median_step_data:
                entry['index'] = index_number

                aggregated_entries.append(entry)
                index_number += 1
        self._logger.debug('Generated median run from steps')

        # Summary data of a step: diff per step
        for step_index, step_timestamps in enumerate(timestamps_by_step):
            summary = {}
            try:
                median_run_id = timestamps_by_step[step_index] \
                    .index(median(step_timestamps)) + 1
            except ValueError:
                continue
            median_run_path = os.path.join(self._results_path,
                                           f'run_{median_run_id}')
            median_step_data = self._parse_v2(median_run_path,
                                              step=step_index + 1)
            # If a step failed and no data is available, do not crash
            if not median_step_data:
                continue

            for field in FIELDNAMES:
                # Some fields are not present on v2 while they are in v3+
                if field not in median_step_data[0]:
                    continue

                # Report max memory peak for this step
                if 'memory' in field:
                    values = []
                    for data in median_step_data:
                        values.append(data[field])
                    summary[f'{field}_min'] = min(values)
                    summary[f'{field}_max'] = max(values)
                # Leave some fields like they are
                elif field in ['version', 'step', 'name', 'run']:
                    summary[field] = median_step_data[0][field]
                # All other fields are accumulated data values for which we
                # report the diff for the step
                else:
                    first = median_step_data[0][field]
                    last = median_step_data[-1][field]
                    diff = round(last - first, ROUND)
                    if field == 'index':
                        # diff will be 0 for 1 sample, but we have this sample,
                        # so include it
                        summary['number_of_samples'] = diff + 1
                    elif field == 'timestamp':
                        summary['duration'] = diff
                    else:
                        summary[f'{field}_diff'] = diff
            summary_entries.append(summary)

        aggregated_file = os.path.join(self._results_path,
                                       METRICS_AGGREGATED_FILE_NAME)
        summary_file = os.path.join(self._results_path,
                                    METRICS_SUMMARY_FILE_NAME)
        self._logger.debug('Generated summary')

        # Store aggregated data
        with open(aggregated_file, 'w') as f:
            writer = DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()
            for entry in aggregated_entries:
                writer.writerow(entry)

        # Store summary data
        with open(summary_file, 'w') as f:
            writer = DictWriter(f, fieldnames=FIELDNAMES_SUMMARY)
            writer.writeheader()
            for entry in summary_entries:
                writer.writerow(entry)
        self._logger.debug('Wrote results')

        return True
