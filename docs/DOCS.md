# Documentation

Documentation is generated with [pdoc](https://pdoc.dev) for all source code
in the [bench_executor](./bench_executor) and [bench_generator](./bench_generator) modules.
The Numpy documentation style guide is used and must be honored when adding
new code to this project.

## How to?

Install `pdoc`:

```
pip install pdoc
```

Generate documentation and output to `docs` folder:

**data-generator**

```
cd data-generator
pdoc --docformat numpy bench_generator/*.py -o ../docs/data-generator
```

**execution-framework**

```
cd execution-framework
pdoc --docformat numpy bench_executor/*.py -o ../docs/execution-framework
```
