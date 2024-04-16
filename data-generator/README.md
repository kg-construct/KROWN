# KROWN's data-generator

KROWN's data generator is a tool to generate synthetic benchmarks
for evaluating the impact of various parameters
e.g. data size, mappings, joins, etc. on materialization systems
for Knowledge Graph Construction.
KROWN's data generator is exposed as a CLI interface `exgentool`.

KROWN's data generator allows to **generate various benchmark scenarios**
and can be extended with more generators dynamically by adding a new one in
the [bench_generator](./bench_generator). Each generator is configurable
as **scenarios** with **scaling parameters**
which are stored in a JSON **configuration file**
([./configs](configs)). Multiple scenarios can be stored inside a configuration
file. By storing the scenarios in a configuration file, we can share it
for **reproducibility**.

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
                        Root directory for generating or listing scenarios
  --scenario SCENARIO   Path to configuration file with scenario's
  --verbose             Turn on verbose output

Please cite our paper if you make use of this tool
```

## List available scenarios

If you want to list all scenarios specified in a configuration file,
you can use the `list` command:

```
./exgentool list --scenario=/path/to/scenario
```

## Generation of scenarios

Generating scenarios is similar to listing them, but usin the `generate`
command instead:

```
./exgentool generate --scenario=/path/to/scenario
```

## Installation

**Ubuntu 22.04 LTS**

1. Install dependencies

```
pip install --user -r requirements.txt
```

2. Verify installation

Execute one of the unit tests:

```
cd tests
./raw-data 
```

## Citation

See main [README.md](../README.md).

## License

Licensed under the [MIT license](./LICENSE)<br>
Written by Dylan Van Assche (dylan.vanassche@ugent.be)
