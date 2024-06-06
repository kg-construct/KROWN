# Duplicates & empty values

All samples are available in the [RMLMapper](./RMLMapper) directory
with RMLMapper as materialisation system.

## Samples

![Parameters duplicates and empty values](https://kg-construct.github.io/KROWN/figures/parameters-duplicates-empty.svg "Parameters duplicates and empty values")
The higher the percentage, the more data in the dataset contains duplicates
or empty values.

- [Duplicates 0%](./RMLMapper/postgresql/duplicates_0.0_percentage)
- [Duplicates 25%](./RMLMapper/postgresql/duplicates_25.0_percentage)
- [Duplicates 50%](./RMLMapper/postgresql/duplicates_50.0_percentage)
- [Duplicates 75%](./RMLMapper/postgresql/duplicates_75.0_percentage)
- [Duplicates 100%](./RMLMapper/postgresql/duplicates_100.0_percentage)
- [Empty values 0%](./RMLMapper/postgresql/empty_0.0_percentage)
- [Empty values 25%](./RMLMapper/postgresql/empty_25.0_percentage)
- [Empty values 50%](./RMLMapper/postgresql/empty_50.0_percentage)
- [Empty values 75%](./RMLMapper/postgresql/empty_75.0_percentage)
- [Empty values 100%](./RMLMapper/postgresql/empty_100.0_percentage)

## Examples

We show for both duplicates and empty values the input data, mapping and expected
output. We use 50% as parameter which means that half of the input data contains
duplicates or empty values. For demonstration purposes, we use CSV format and
10 rows with 2 property + 1 ID columns only.

### Duplicates 50%

Only the rows which are not duplicated, are mapped + once the duplicated row.

#### Input data

```
id,p1,p2
9223372036854775807,DUPLICATE,DUPLICATE
2,V_1-2,V_2-2
9223372036854775807,DUPLICATE,DUPLICATE
4,V_1-4,V_2-4
9223372036854775807,DUPLICATE,DUPLICATE
6,V_1-6,V_2-6
9223372036854775807,DUPLICATE,DUPLICATE
8,V_1-8,V_2-8
9,V_1-9,V_2-9
9223372036854775807,DUPLICATE,DUPLICATE
```

#### RML Mapping

```
@base <http://ex.com/> .
@prefix ex: <http://example.com/> .
@prefix rr: <http://www.w3.org/ns/r2rml#> .

<#TriplesMap1> a rr:TriplesMap ;
    rr:logicalTable [ a rr:LogicalTable ;
            rr:tableName "data" ] ;
    rr:predicateObjectMap [ a rr:PredicateObjectMap ;
            rr:objectMap [ a rr:ObjectMap ;
                    rr:column "p2" ] ;
            rr:predicateMap [ a rr:PredicateMap ;
                    rr:constant ex:p2 ] ],
        [ a rr:PredicateObjectMap ;
            rr:objectMap [ a rr:ObjectMap ;
                    rr:column "p1" ] ;
            rr:predicateMap [ a rr:PredicateMap ;
                    rr:constant ex:p1 ] ] ;
    rr:subjectMap [ rr:template "http://ex.com/table/{id}" ] .
```

#### Output RDF

```
<http://ex.com/table/2> <http://example.com/p1> "V_1-2" .
<http://ex.com/table/2> <http://example.com/p2> "V_2-2" .
<http://ex.com/table/4> <http://example.com/p1> "V_1-4" .
<http://ex.com/table/4> <http://example.com/p2> "V_2-4" .
<http://ex.com/table/6> <http://example.com/p1> "V_1-6" .
<http://ex.com/table/6> <http://example.com/p2> "V_2-6" .
<http://ex.com/table/8> <http://example.com/p1> "V_1-8" .
<http://ex.com/table/8> <http://example.com/p2> "V_2-8" .
<http://ex.com/table/9> <http://example.com/p1> "V_1-9" .
<http://ex.com/table/9> <http://example.com/p2> "V_2-9" .
<http://ex.com/table/9223372036854775807> <http://example.com/p1> "DUPLICATE" .
<http://ex.com/table/9223372036854775807> <http://example.com/p2> "DUPLICATE" .
```

### Empty values 50%

Only the rows that have no empty values are mapped.

#### Input data

```
id,p1,p2
1,NULL,NULL
2,V_1-2,V_2-2
3,NULL,NULL
4,V_1-4,V_2-4
5,NULL,NULL
6,V_1-6,V_2-6
7,NULL,NULL
8,V_1-8,V_2-8
9,V_1-9,V_2-9
10,NULL,NULL
```

#### RML Mapping

```
@base <http://ex.com/> .
@prefix ex: <http://example.com/> .
@prefix rr: <http://www.w3.org/ns/r2rml#> .

<#TriplesMap1> a rr:TriplesMap ;
    rr:logicalTable [ a rr:LogicalTable ;
            rr:tableName "data" ] ;
    rr:predicateObjectMap [ a rr:PredicateObjectMap ;
            rr:objectMap [ a rr:ObjectMap ;
                    rr:column "p2" ] ;
            rr:predicateMap [ a rr:PredicateMap ;
                    rr:constant ex:p2 ] ],
        [ a rr:PredicateObjectMap ;
            rr:objectMap [ a rr:ObjectMap ;
                    rr:column "p1" ] ;
            rr:predicateMap [ a rr:PredicateMap ;
                    rr:constant ex:p1 ] ] ;
    rr:subjectMap [ rr:template "http://ex.com/table/{id}" ] .
```

#### Output RDF

```
<http://ex.com/table/2> <http://example.com/p1> "V_1-2" .
<http://ex.com/table/2> <http://example.com/p2> "V_2-2" .
<http://ex.com/table/4> <http://example.com/p1> "V_1-4" .
<http://ex.com/table/4> <http://example.com/p2> "V_2-4" .
<http://ex.com/table/6> <http://example.com/p1> "V_1-6" .
<http://ex.com/table/6> <http://example.com/p2> "V_2-6" .
<http://ex.com/table/8> <http://example.com/p1> "V_1-8" .
<http://ex.com/table/8> <http://example.com/p2> "V_2-8" .
<http://ex.com/table/9> <http://example.com/p1> "V_1-9" .
<http://ex.com/table/9> <http://example.com/p2> "V_2-9" .
```
