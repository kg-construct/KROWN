# Mappings

All samples are available in the [RMLMapper](./RMLMapper) directory
with RMLMapper as materialisation system.

## Samples

![Parameters mappings](https://kg-construct.github.io/KROWN/figures/parameters-mappings.svg "Parameters mappings")

The more Triples Maps (TMs), the more RDF subjects are generated.
The more Predicate Object Maps (POMs), the more RDF objects and predicates
are generated for a RDF subject.
The more Graph Maps (GMs), the more Named Graphs (NGs) are generated.
Named Graphs can be generated Dynamically (D) through an IRI template
or Statically (S) as a constant.

- [Empty values 100%](./RMLMapper/csv/empty_100.0_percentage)

## Examples


### 3 TMs + 1 POM

The more TMs, the more RDF subjects are generated.

#### Input data

```
```

#### RML Mapping

```
```

#### Output RDF

```
```

### 1 TM + 5 POMs

The more POMs, the more RDF predicates and objects are generated per RDF subject.

#### Input data

```
```

#### RML Mapping

```
```

#### Output RDF

```
```

### 1 TM + 1 POM + 3 GMs

The more GMs, the more NGs are generated. If multiple NGs are specified,
RDF triples will be duplicated and added to all NGs.

#### Input data

```
```

#### RML Mapping

```
```

#### Output RDF

```
```
