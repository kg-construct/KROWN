# KROWN 👑: Knowledge Graph Construction Benchmark

KROWN (Knowledge gRaph cOnstruction beNchmark) is a benchmark for 
materialization systems to construct Knowledge Graphs from 
(semi-)heterogeneous data sources using declarative mappings
such as [RML](http://w3id.org/rml/portal).

Many benchmarks already exist for virtualization systems
e.g. [GTFS-Madrid-Bench](https://github.com/oeg-upm/gtfs-bench),
[NPD](https://ontop-vkg.org/npd-benchmark/),
[BSBM](http://wbsg.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/)
which focus on complex queries with a single declarative mapping.
However, materialization systems are unaffected
by complex queries since their input is the dataset and the mappings to
generate a Knowledge Graph. Some specialized datasets exist to benchmark
specific limitations of materialization systems such as duplicated or empty
values in datasets e.g. [GENOMICS](https://doi.org/10.57702/4c9ivpgs), 
but they do not cover all aspects of materialization systems.
Therefore, it is hard to compare materialization systems
among each other in general which is where KROWN comes in!

## Data generator

KROWN provides a data generator to scale the different benchmark scenarios
with multiple scaling parameters, configurable through a set of 
JSON configuration files. This way, any combination can be used of scaling
parameters and their values are stored to easily reproduce 
the generation in the future.

**Example usage**

```
./exgentool generate --scenario=/path/to/config.json
```

## Execution framework

KROWN provides also an execution framework to reproducible execute benchmark
scenarios as a pipeline of Docker containers while measuring metrics e.g.
execution time, CPU time, memory consumption, storage usage, etc.

**Example usage**

```
./exectool --runs=5 --root=/path/to/scenarios run
```

The execution framework of KROWN has been used in the
[Knowledge Graph Construction Workshop Challenges](https://w3id.org/kg-construct/workshop/2024/challenge.html)
at ESWC 2023 and 2024.
It was also used in benchmarking incremental mappings with
[IncRML (under review)](https://semantic-web-journal.net/content/incrml-incremental-knowledge-graph-construction-heterogeneous-data-sources).

## Citation

```
@software{Van_Assche_KROWN_A_Benchmark_2024,
  author = {Van Assche, Dylan and Chaves-Fraga, David and Dimou, Anastasia},
  doi = {TODO},
  license = {MIT},
  month = apr,
  title = {{KROWN: A Benchmark for RDF Graph Materialization}},
  url = {https://w3id.org/kg-construct/KROWN},
  version = {1.0.0},
  year = {2024}
}
```

## License

Licensed under the [MIT license](./LICENSE).
