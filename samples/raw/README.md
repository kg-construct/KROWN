# Raw

All samples are available in the [RMLMapper](./RMLMapper) directory
with RMLMapper as materialisation system.

## Samples

![Parameters raw](https://kg-construct.github.io/KROWN/figures/parameters-raw.svg "Parameters raw")

Increasing the number of rows results in more RDF subjects,
more columns results in more RDF predicates and objects per RDF subject.
Increasing the cell value size results in larger RDF Literals for the RDF object.

- [Number of rows: 10](./RMLMapper/postgresql/raw_10_2_0)
- [Number of rows: 100](./RMLMapper/postgresql/raw_100_2_0)
- [Number of rows: 1000](./RMLMapper/postgresql/raw_1000_2_0)
- [Number of rows: 10000](./RMLMapper/postgresql/raw_10000_2_0)
- [Number of columns: 1](./RMLMapper/postgresql/raw_10_1_0)
- [Number of columns: 3](./RMLMapper/postgresql/raw_10_3_0)
- [Number of columns: 5](./RMLMapper/postgresql/raw_10_5_0)
- [Number of columns: 7](./RMLMapper/postgresql/raw_10_7_0)
- [Cell value size: 10](./RMLMapper/postgresql/raw_10_2_10)
- [Cell value size: 50](./RMLMapper/postgresql/raw_10_2_50)
- [Cell value size: 100](./RMLMapper/postgresql/raw_10_2_100)
- [Cell value size: 500](./RMLMapper/postgresql/raw_10_2_500)

## Examples

### Raw 10 rows and 2 columns

All rows are mapped to a RDF graph, more rows causes the RDF graph to be larger
in size with more RDF subjects.

#### Input data

```
id,p1,p2
1,V_1-1,V_2-1
2,V_1-2,V_2-2
3,V_1-3,V_2-3
4,V_1-4,V_2-4
5,V_1-5,V_2-5
6,V_1-6,V_2-6
7,V_1-7,V_2-7
8,V_1-8,V_2-8
9,V_1-9,V_2-9
10,V_1-10,V_2-10
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
<http://ex.com/table/1> <http://example.com/p1> "V_1-1" .
<http://ex.com/table/1> <http://example.com/p2> "V_2-1" .
<http://ex.com/table/10> <http://example.com/p1> "V_1-10" .
<http://ex.com/table/10> <http://example.com/p2> "V_2-10" .
<http://ex.com/table/2> <http://example.com/p1> "V_1-2" .
<http://ex.com/table/2> <http://example.com/p2> "V_2-2" .
<http://ex.com/table/3> <http://example.com/p1> "V_1-3" .
<http://ex.com/table/3> <http://example.com/p2> "V_2-3" .
<http://ex.com/table/4> <http://example.com/p1> "V_1-4" .
<http://ex.com/table/4> <http://example.com/p2> "V_2-4" .
<http://ex.com/table/5> <http://example.com/p1> "V_1-5" .
<http://ex.com/table/5> <http://example.com/p2> "V_2-5" .
<http://ex.com/table/6> <http://example.com/p1> "V_1-6" .
<http://ex.com/table/6> <http://example.com/p2> "V_2-6" .
<http://ex.com/table/7> <http://example.com/p1> "V_1-7" .
<http://ex.com/table/7> <http://example.com/p2> "V_2-7" .
<http://ex.com/table/8> <http://example.com/p1> "V_1-8" .
<http://ex.com/table/8> <http://example.com/p2> "V_2-8" .
<http://ex.com/table/9> <http://example.com/p1> "V_1-9" .
<http://ex.com/table/9> <http://example.com/p2> "V_2-9" .
```

### Raw 10 rows and 5 columns

All columns are mapped to a RDF graph, more columns causes the RDF graph 
to be larger in size with more RDF predicates and objects.

#### Input data

```
id,p1,p2,p3,p4,p5
1,V_1-1,V_2-1,V_3-1,V_4-1,V_5-1
2,V_1-2,V_2-2,V_3-2,V_4-2,V_5-2
3,V_1-3,V_2-3,V_3-3,V_4-3,V_5-3
4,V_1-4,V_2-4,V_3-4,V_4-4,V_5-4
5,V_1-5,V_2-5,V_3-5,V_4-5,V_5-5
6,V_1-6,V_2-6,V_3-6,V_4-6,V_5-6
7,V_1-7,V_2-7,V_3-7,V_4-7,V_5-7
8,V_1-8,V_2-8,V_3-8,V_4-8,V_5-8
9,V_1-9,V_2-9,V_3-9,V_4-9,V_5-9
10,V_1-10,V_2-10,V_3-10,V_4-10,V_5-10
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
                    rr:column "p4" ] ;
            rr:predicateMap [ a rr:PredicateMap ;
                    rr:constant ex:p4 ] ],
        [ a rr:PredicateObjectMap ;
            rr:objectMap [ a rr:ObjectMap ;
                    rr:column "p5" ] ;
            rr:predicateMap [ a rr:PredicateMap ;
                    rr:constant ex:p5 ] ],
        [ a rr:PredicateObjectMap ;
            rr:objectMap [ a rr:ObjectMap ;
                    rr:column "p1" ] ;
            rr:predicateMap [ a rr:PredicateMap ;
                    rr:constant ex:p1 ] ],
        [ a rr:PredicateObjectMap ;
            rr:objectMap [ a rr:ObjectMap ;
                    rr:column "p2" ] ;
            rr:predicateMap [ a rr:PredicateMap ;
                    rr:constant ex:p2 ] ],
        [ a rr:PredicateObjectMap ;
            rr:objectMap [ a rr:ObjectMap ;
                    rr:column "p3" ] ;
            rr:predicateMap [ a rr:PredicateMap ;
                    rr:constant ex:p3 ] ] ;
    rr:subjectMap [ rr:template "http://ex.com/table/{id}" ] .
```

#### Output RDF

```
<http://ex.com/table/1> <http://example.com/p1> "V_1-1" .
<http://ex.com/table/1> <http://example.com/p2> "V_2-1" .
<http://ex.com/table/1> <http://example.com/p3> "V_3-1" .
<http://ex.com/table/1> <http://example.com/p4> "V_4-1" .
<http://ex.com/table/1> <http://example.com/p5> "V_5-1" .
<http://ex.com/table/10> <http://example.com/p1> "V_1-10" .
<http://ex.com/table/10> <http://example.com/p2> "V_2-10" .
<http://ex.com/table/10> <http://example.com/p3> "V_3-10" .
<http://ex.com/table/10> <http://example.com/p4> "V_4-10" .
<http://ex.com/table/10> <http://example.com/p5> "V_5-10" .
<http://ex.com/table/2> <http://example.com/p1> "V_1-2" .
<http://ex.com/table/2> <http://example.com/p2> "V_2-2" .
<http://ex.com/table/2> <http://example.com/p3> "V_3-2" .
<http://ex.com/table/2> <http://example.com/p4> "V_4-2" .
<http://ex.com/table/2> <http://example.com/p5> "V_5-2" .
<http://ex.com/table/3> <http://example.com/p1> "V_1-3" .
<http://ex.com/table/3> <http://example.com/p2> "V_2-3" .
<http://ex.com/table/3> <http://example.com/p3> "V_3-3" .
<http://ex.com/table/3> <http://example.com/p4> "V_4-3" .
<http://ex.com/table/3> <http://example.com/p5> "V_5-3" .
<http://ex.com/table/4> <http://example.com/p1> "V_1-4" .
<http://ex.com/table/4> <http://example.com/p2> "V_2-4" .
<http://ex.com/table/4> <http://example.com/p3> "V_3-4" .
<http://ex.com/table/4> <http://example.com/p4> "V_4-4" .
<http://ex.com/table/4> <http://example.com/p5> "V_5-4" .
<http://ex.com/table/5> <http://example.com/p1> "V_1-5" .
<http://ex.com/table/5> <http://example.com/p2> "V_2-5" .
<http://ex.com/table/5> <http://example.com/p3> "V_3-5" .
<http://ex.com/table/5> <http://example.com/p4> "V_4-5" .
<http://ex.com/table/5> <http://example.com/p5> "V_5-5" .
<http://ex.com/table/6> <http://example.com/p1> "V_1-6" .
<http://ex.com/table/6> <http://example.com/p2> "V_2-6" .
<http://ex.com/table/6> <http://example.com/p3> "V_3-6" .
<http://ex.com/table/6> <http://example.com/p4> "V_4-6" .
<http://ex.com/table/6> <http://example.com/p5> "V_5-6" .
<http://ex.com/table/7> <http://example.com/p1> "V_1-7" .
<http://ex.com/table/7> <http://example.com/p2> "V_2-7" .
<http://ex.com/table/7> <http://example.com/p3> "V_3-7" .
<http://ex.com/table/7> <http://example.com/p4> "V_4-7" .
<http://ex.com/table/7> <http://example.com/p5> "V_5-7" .
<http://ex.com/table/8> <http://example.com/p1> "V_1-8" .
<http://ex.com/table/8> <http://example.com/p2> "V_2-8" .
<http://ex.com/table/8> <http://example.com/p3> "V_3-8" .
<http://ex.com/table/8> <http://example.com/p4> "V_4-8" .
<http://ex.com/table/8> <http://example.com/p5> "V_5-8" .
<http://ex.com/table/9> <http://example.com/p1> "V_1-9" .
<http://ex.com/table/9> <http://example.com/p2> "V_2-9" .
<http://ex.com/table/9> <http://example.com/p3> "V_3-9" .
<http://ex.com/table/9> <http://example.com/p4> "V_4-9" .
<http://ex.com/table/9> <http://example.com/p5> "V_5-9" .
```

### Raw 10 rows, 2 columns and 10 additional characters as value size

Increasing the value size results in larger RDF Literals which are
mapped to an RDF graph as RDF objects. 10 characters are appended to each
cell value.

#### Input data

```
id,p1,p2
1,V_1-1_abcdefghij,V_2-1_abcdefghij
2,V_1-2_abcdefghij,V_2-2_abcdefghij
3,V_1-3_abcdefghij,V_2-3_abcdefghij
4,V_1-4_abcdefghij,V_2-4_abcdefghij
5,V_1-5_abcdefghij,V_2-5_abcdefghij
6,V_1-6_abcdefghij,V_2-6_abcdefghij
7,V_1-7_abcdefghij,V_2-7_abcdefghij
8,V_1-8_abcdefghij,V_2-8_abcdefghij
9,V_1-9_abcdefghij,V_2-9_abcdefghij
10,V_1-10_abcdefghij,V_2-10_abcdefghij
```

#### RML mapping

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
<http://ex.com/table/1> <http://example.com/p1> "V_1-1_abcdefghij" .
<http://ex.com/table/1> <http://example.com/p2> "V_2-1_abcdefghij" .
<http://ex.com/table/10> <http://example.com/p1> "V_1-10_abcdefghij" .
<http://ex.com/table/10> <http://example.com/p2> "V_2-10_abcdefghij" .
<http://ex.com/table/2> <http://example.com/p1> "V_1-2_abcdefghij" .
<http://ex.com/table/2> <http://example.com/p2> "V_2-2_abcdefghij" .
<http://ex.com/table/3> <http://example.com/p1> "V_1-3_abcdefghij" .
<http://ex.com/table/3> <http://example.com/p2> "V_2-3_abcdefghij" .
<http://ex.com/table/4> <http://example.com/p1> "V_1-4_abcdefghij" .
<http://ex.com/table/4> <http://example.com/p2> "V_2-4_abcdefghij" .
<http://ex.com/table/5> <http://example.com/p1> "V_1-5_abcdefghij" .
<http://ex.com/table/5> <http://example.com/p2> "V_2-5_abcdefghij" .
<http://ex.com/table/6> <http://example.com/p1> "V_1-6_abcdefghij" .
<http://ex.com/table/6> <http://example.com/p2> "V_2-6_abcdefghij" .
<http://ex.com/table/7> <http://example.com/p1> "V_1-7_abcdefghij" .
<http://ex.com/table/7> <http://example.com/p2> "V_2-7_abcdefghij" .
<http://ex.com/table/8> <http://example.com/p1> "V_1-8_abcdefghij" .
<http://ex.com/table/8> <http://example.com/p2> "V_2-8_abcdefghij" .
<http://ex.com/table/9> <http://example.com/p1> "V_1-9_abcdefghij" .
<http://ex.com/table/9> <http://example.com/p2> "V_2-9_abcdefghij" .
```
