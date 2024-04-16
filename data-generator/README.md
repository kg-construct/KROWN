# EXGEN (EXperiment GENerator)

EXGEN (EXperiment GENerator) is a simple tool to generate synthetic benchmarks
for evaluating the impact of various parameters
e.g. data size, mappings, joins, etc. on Knowledge Graph construction.
EXGEN exposes a CLI interface `exgentool`.

## How to use?

You can list all options and arguments with `--help`

```
usage: exgentool [-h] [--version] [--root MAIN_DIRECTORY] [--scenario SCENARIO] [--verbose] command

Copyright by (c) Dylan Van Assche (2022-2024), available under the MIT license

positional arguments:
  command               Command to execute, available commands: "list", "generate"

options:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  --root MAIN_DIRECTORY
                        Root directory for generated scenarios
  --scenario SCENARIO   Path to file with scenario's instances
  --verbose             Turn on verbose output

Please cite our paper if you make use of this tool
```

## License

Licensed under the [MIT license](./LICENSE)<br>
Written by Dylan Van Assche (dylan.vanassche@ugent.be)
