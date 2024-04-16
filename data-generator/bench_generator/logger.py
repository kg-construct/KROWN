#!/usr/bin/env python3

"""
This module contains the Logger class which is responsible for logging.
This class is a small wrapper around the Python logging module to automatically
configure the loggers and handle unittest logging.
"""

import os
import sys
import logging

LOG_FILE_NAME = 'log.txt'
LOGGER_FORMAT_FILE = '[%(asctime)s] %(levelname)-8s %(message)-s'
LOGGER_FORMAT_CONSOLE = '%(levelname)s: %(message)s'


class Logger:
    """Log messages to a log file and console."""

    def __init__(self, name: str, directory: str, verbose: bool):
        """Creates an instance of the Logger class.

        During unittests, the `UNITTEST` environment variable is set which
        disables the console logger.

        Parameters
        ----------
        name : str
            Name of the logger
        directory : str
            The path to the directory where the logs must be stored.
        verbose : bool
            Enable verbose logs
        """
        self._logger = logging.getLogger(name)

        # Configure logging level
        self._verbose = verbose
        level = logging.INFO
        if self._verbose:
            level = logging.DEBUG
        self._logger.setLevel(level)

        # Disable default handlers
        handlers = self._logger.handlers
        for h in handlers:
            self._logger.removeHandler(h)

        # Configure handlers
        directory = os.path.abspath(directory)
        os.makedirs(directory, exist_ok=True)
        log_file = logging.FileHandler(os.path.join(directory, LOG_FILE_NAME))
        log_file.setLevel(logging.DEBUG)
        format_file = logging.Formatter(LOGGER_FORMAT_FILE)
        log_file.setFormatter(format_file)
        self._logger.addHandler(log_file)

        # Silence console logging during unittests, logs are available in the
        # log file anyway
        if os.environ.get('UNITTEST') is None:
            log_console = logging.StreamHandler(sys.stderr)
            log_console.setLevel(level)
            format_console = logging.Formatter(LOGGER_FORMAT_CONSOLE)
            log_console.setFormatter(format_console)
            self._logger.addHandler(log_console)

    def __del__(self):
        """Close any handlers if needed"""
        handlers = self._logger.handlers
        for h in handlers:
            try:
                h.close()
            except AttributeError:
                pass
            self._logger.removeHandler(h)

    @property
    def verbose(self) -> bool:
        """Verbose logging enabled.

        Returns
        -------
        verbose : bool
            Verbose logging enabled or not.
        """
        return self._verbose

    def debug(self, msg):
        """Log a message with level DEBUG."""
        self._logger.debug(msg)

    def info(self, msg):
        """Log a message with level INFO."""
        self._logger.info(msg)

    def warning(self, msg):
        """Log a message with level WARNING."""
        self._logger.warning(msg)

    def error(self, msg):
        """Log a message with level ERROR."""
        self._logger.error(msg)
