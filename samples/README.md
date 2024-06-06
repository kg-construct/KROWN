# Samples

In this directory you can find samples of all the scenarios currently
supported by KROWN's data generator.

![All parameters](https://kg-construct.github.io/KROWN/figures/parameters.svg "Parameters")

- [raw](./raw): scaling in number of rows, columns and cell size of the data.
- [mappings](./mappings): scaling in the number of Triples Maps, Predicate Object Maps, and Graph Maps.
- [duplicates-empty](./duplicates-empty): scaling the number of duplicates and empty values in the data.
- [joins](./joins): scaling the number of join conditions, the data involved in joins,
join relations, and duplicates generated through joins

You can generate these samples yourself with KROWN's data generator, the
scenario configuration is provided as `sample-$SCENARIO-rmlmapper.json`
within the directory of each sample. In the samples we use `RMLMapper` as
materialization engine, but any engine can be used by modifying the scenario
configuration file.

For example:

```
cd raw
./exgentool --scenario=sample-raw-rmlmapper.json generate
```

Generates all the scenarios for scaling the raw data among number of rows,
columns and cell size with RMLMapper as engine.
