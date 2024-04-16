# Documentation

Documentation is generated with [pdoc](https://pdoc.dev) for all source code in the [bench_executor](./bench_executor) module.
The Numpy documentation style guide is used and must be honored when adding
new code to this project.

## How to?

Install `pdoc`:

```
pip install pdoc
```

Generate documentation and output to `docs` folder:

```
pdoc --docformat numpy bench_executor/*.py -o docs
```
