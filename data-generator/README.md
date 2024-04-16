# KROWN 👑's data-generator

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
([config](config) folder). Multiple scenarios can be stored inside a configuration
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

## Adding your own scenario

Expanding KROWN's data generator was considered from the beginning of the 
generator's development to make it future proof. Each generator is a Python
class with a method `generate()`. This way, you can add your own Python class
and it will be picked up dynamically by KROWN's data generator. Parameters
for your generator can be specified as well when instantiating the class.
The latter is done automatically when the user triggers the generation with
the `generate` command of the CLI interface.

To ease development of new generators, you can subclass the `Scenario` Python
class which provides several utility methods to automatically construct
the pipeline steps (`metadata.json`), creating RML mappings based upon your
scenario you want to generate, for KROWN's execution framework. Moreover,
it enforces the implementation of the `generate()` method to ensure that your
new data generator is always picked up automatically.

In this example, we will create a data generator called `MyGenerator`.

1. Add a new Python class `MyGenerator` inside `my_generator.py`.

```
class MyGenerator(Scenario):
    def __init__(self, main_directoru: str, verbose: bool):
        pass
        
    def generate(self):
        pass
```

2. Add parameters for your generator, for example: `my_param`.

```

class MyGenerator(Scenario):
    def __init__(self, main_directory: str, verbose: bool, my_param: str):
        self._my_param: str = my_param
        
    def generate(self):
        pass
```

You can use this parameter later on when generating scenarios using your
generator.

3. Add the actual generator inside the `generate()` method

```

class MyGenerator(Scenario):
    def __init__(self, main_directory: str, verbose: bool, my_param: str):
        self._my_param: str = my_param
        
    def generate(self):
        do_generation(self._my_param)
```

In this example, we reduced the generator to a function call called `do_generation`.
If you want to see a real implementation, have a look at [raw_data.py](./bench_generator/raw_data.py).

**Note**: the parameters `main_directory` and `verbose` are always supplied.
The `main_directory` indicates the root directory where the generator is
executed and `verbose` specifies if debug logs should be printed.

4. Use your generator in a configuration file called `my_scenario.json`.

```
{
    "@id": "http://example.com/my-scenario",
    "name": "My New Scenario",
    "description": "Example configuration for MyGenerator",
    "instances": [
        {
            "@id": "http://example.com/my-scenario#5",
            "name": "My Scenario with scaling parameter 5",
            "generator": "MyGenerator",
            "parameters": {
                "my_param": 5
            }
        }
    ]
}
```

Each `instance` is a scenario you want to generate with your brand-new 
generator. In the example, we give it a `name` and specify that we want to use
`MyGenerator` as `generator`. The generator will receive a scaling parameter
called `my_param` with value `5`.

5. Test your generator

Now that you have everything ready, you can test your generator through
the CLI interface:

**Listing scenario**

```
./exgentool --scenario=my_scenario.json list
```

**Generating scenario**

```
./exgentool --scenario=my_scenario.json generate
```

If you stored the configuration file `my_scenario.json` not inside the same
directory as `exgentool`, you can specify that directory by using the `--root`
CLI parameter.

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
