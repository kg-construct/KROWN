# Joins

All samples are available in the [RMLMapper](./RMLMapper) directory
with RMLMapper as materialisation system.

## Samples

![Parameters joins](https://kg-construct.github.io/KROWN/figures/parameters-duplicates-empty.svg "Parameters joins")

The higher the percentage, the more rows in the data results into a join.
More join conditions requires more conditions to be checked by the system
to result into a join. The relation N-M may affect the system's performance
depending on how the joins are implemented. Duplicates resulted from a join
need to be removed by the system.

- [Percentage 0% 1-1](./RMLMapper/postgresql/joins_perc_1-1_0)
- [Percentage 25% 1-1](./RMLMapper/postgresql/joins_perc_1-1_25.0)
- [Percentage 50% 1-1](./RMLMapper/postgresql/joins_perc_1-1_50.0)
- [Percentage 75% 1-1](./RMLMapper/postgresql/joins_perc_1-1_75.0)
- [Percentage 100% 1-1](./RMLMapper/postgresql/joins_perc_1-1_100.0)
- [Multiple conditions 5JC 50% 1-1](./RMLMapper/postgresql/joins_multiple_1-1_5jc_50.0)
- [Multiple conditions 5JC 50% 3-5](./RMLMapper/postgresql/joins_multiple_3-5_5jc_50.0)
- [Multiple conditions 5JC 50% 5-3](./RMLMapper/postgresql/joins_multiple_5-3_5jc_50.0)
- [Multiple conditions 10JC 50% 1-1](./RMLMapper/postgresql/joins_multiple_1-1_10jc_50.0)
- [Multiple conditions 10JC 50% 3-5](./RMLMapper/postgresql/joins_multiple_3-5_10jc_50.0)
- [Multiple conditions 10JC 50% 5-3](./RMLMapper/postgresql/joins_multiple_5-3_10jc_50.0)
- [Multiple conditions 15JC 50% 1-1](./RMLMapper/postgresql/joins_multiple_1-1_15jc_50.0)
- [Multiple conditions 15JC 50% 3-5](./RMLMapper/postgresql/joins_multiple_3-5_15jc_50.0)
- [Multiple conditions 15JC 50% 5-3](./RMLMapper/postgresql/joins_multiple_5-3_15jc_50.0)
- [Relations 1-3 50%](./RMLMapper/postgresql/joins_relations_1-3_50.0)
- [Relations 1-5 50%](./RMLMapper/postgresql/joins_relations_1-5_50.0)
- [Relations 1-10 50%](./RMLMapper/postgresql/joins_relations_1-10_50.0)
- [Relations 1-15 50%](./RMLMapper/postgresql/joins_relations_1-15_50.0)
- [Relations 10-1 0%](./RMLMapper/postgresql/joins_relations_10-1_0)
- [Relations 10-1 25%](./RMLMapper/postgresql/joins_relations_10-1_25.0)
- [Relations 10-1 50%](./RMLMapper/postgresql/joins_relations_10-1_50.0)
- [Relations 10-1 75%](./RMLMapper/postgresql/joins_relations_10-1_75.0)
- [Relations 10-1 100%](./RMLMapper/postgresql/joins_relations_10-1_100.0)
- [Relations 10-5 0%](./RMLMapper/postgresql/joins_relations_10-5_0)
- [Relations 10-5 25%](./RMLMapper/postgresql/joins_relations_10-5_25.0)
- [Relations 10-5 50%](./RMLMapper/postgresql/joins_relations_10-5_50.0)
- [Relations 10-5 75%](./RMLMapper/postgresql/joins_relations_10-5_75.0)
- [Relations 10-5 100%](./RMLMapper/postgresql/joins_relations_10-5_100.0)
- [Relations 1-10 0%](./RMLMapper/postgresql/joins_relations_1-10_0)
- [Relations 1-10 25%](./RMLMapper/postgresql/joins_relations_1-10_25.0)
- [Relations 1-10 50%](./RMLMapper/postgresql/joins_relations_1-10_50.0)
- [Relations 1-10 75%](./RMLMapper/postgresql/joins_relations_1-10_75.0)
- [Relations 1-10 100%](./RMLMapper/postgresql/joins_relations_1-10_100.0)
- [Relations 5-10 0%](./RMLMapper/postgresql/joins_relations_5-10_0)
- [Relations 5-10 25%](./RMLMapper/postgresql/joins_relations_5-10_25.0)
- [Relations 5-10 50%](./RMLMapper/postgresql/joins_relations_5-10_50.0)
- [Relations 5-10 75%](./RMLMapper/postgresql/joins_relations_5-10_75.0)
- [Relations 5-10 100%](./RMLMapper/postgresql/joins_relations_5-10_100.0)
- [Relations 5-3 0%](./RMLMapper/postgresql/joins_relations_5-3_0)
- [Relations 5-3 25%](./RMLMapper/postgresql/joins_relations_5-3_25.0)
- [Relations 5-3 50%](./RMLMapper/postgresql/joins_relations_5-3_50.0)
- [Relations 5-3 75%](./RMLMapper/postgresql/joins_relations_5-3_75.0)
- [Relations 5-3 100%](./RMLMapper/postgresql/joins_relations_5-3_100.0)
- [Relations 3-5 0%](./RMLMapper/postgresql/joins_relations_3-5_0)
- [Relations 3-5 25%](./RMLMapper/postgresql/joins_relations_3-5_25.0)
- [Relations 3-5 50%](./RMLMapper/postgresql/joins_relations_3-5_50.0)
- [Relations 3-5 75%](./RMLMapper/postgresql/joins_relations_3-5_75.0)
- [Relations 3-5 100%](./RMLMapper/postgresql/joins_relations_3-5_100.0)
- [Relations 3-3 0%](./RMLMapper/postgresql/joins_relations_3-3_0)
- [Relations 3-3 25%](./RMLMapper/postgresql/joins_relations_3-3_25.0)
- [Relations 3-3 50%](./RMLMapper/postgresql/joins_relations_3-3_50.0)
- [Relations 3-3 75%](./RMLMapper/postgresql/joins_relations_3-3_75.0)
- [Relations 3-3 100%](./RMLMapper/postgresql/joins_relations_3-3_100.0)
- [Duplicates 5 50%](./RMLMapper/postgresql/joins_duplicates_5_50.0)
- [Duplicates 10 50%](./RMLMapper/postgresql/joins_duplicates_10_50.0)
- [Duplicates 15 50%](./RMLMapper/postgresql/joins_duplicates_15_50.0)
- [Duplicates 10 0%](./RMLMapper/postgresql/joins_duplicates_10_0)
- [Duplicates 10 25%](./RMLMapper/postgresql/joins_duplicates_10_25.0)
- [Duplicates 10 75%](./RMLMapper/postgresql/joins_duplicates_10_75.0)
- [Duplicates 10 100%](./RMLMapper/postgresql/joins_duplicates_10_100.0)

## Examples

### Join percentage 50%

The higher the percentage, the more rows in the data results into a join.

#### Input data

**data1**
```
id,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10
1,V_1-1,V_2-1,V_3-1,V_4-1,V_5-1,V_6-1,V_7-1,V_8-1,V_9-1,V_10-1
2,V_1-2,V_2-2,V_3-2,V_4-2,V_5-2,V_6-2,V_7-2,V_8-2,V_9-2,V_10-2
3,V_1-3,V_2-3,V_3-3,V_4-3,V_5-3,V_6-3,V_7-3,V_8-3,V_9-3,V_10-3
4,V_1-4,V_2-4,V_3-4,V_4-4,V_5-4,V_6-4,V_7-4,V_8-4,V_9-4,V_10-4
5,V_1-5,V_2-5,V_3-5,V_4-5,V_5-5,V_6-5,V_7-5,V_8-5,V_9-5,V_10-5
6,V_1-6,V_2-6,V_3-6,V_4-6,V_5-6,V_6-6,V_7-6,V_8-6,V_9-6,V_10-6
7,V_1-7,V_2-7,V_3-7,V_4-7,V_5-7,V_6-7,V_7-7,V_8-7,V_9-7,V_10-7
8,V_1-8,V_2-8,V_3-8,V_4-8,V_5-8,V_6-8,V_7-8,V_8-8,V_9-8,V_10-8
9,V_1-9,V_2-9,V_3-9,V_4-9,V_5-9,V_6-9,V_7-9,V_8-9,V_9-9,V_10-9
10,V_1-10,V_2-10,V_3-10,V_4-10,V_5-10,V_6-10,V_7-10,V_8-10,V_9-10,V_10-10
11,V_1-11,V_2-11,V_3-11,V_4-11,V_5-11,V_6-11,V_7-11,V_8-11,V_9-11,V_10-11
12,V_1-12,V_2-12,V_3-12,V_4-12,V_5-12,V_6-12,V_7-12,V_8-12,V_9-12,V_10-12
13,V_1-13,V_2-13,V_3-13,V_4-13,V_5-13,V_6-13,V_7-13,V_8-13,V_9-13,V_10-13
14,V_1-14,V_2-14,V_3-14,V_4-14,V_5-14,V_6-14,V_7-14,V_8-14,V_9-14,V_10-14
15,V_1-15,V_2-15,V_3-15,V_4-15,V_5-15,V_6-15,V_7-15,V_8-15,V_9-15,V_10-15
16,V_1-16,V_2-16,V_3-16,V_4-16,V_5-16,V_6-16,V_7-16,V_8-16,V_9-16,V_10-16
17,V_1-17,V_2-17,V_3-17,V_4-17,V_5-17,V_6-17,V_7-17,V_8-17,V_9-17,V_10-17
18,V_1-18,V_2-18,V_3-18,V_4-18,V_5-18,V_6-18,V_7-18,V_8-18,V_9-18,V_10-18
19,V_1-19,V_2-19,V_3-19,V_4-19,V_5-19,V_6-19,V_7-19,V_8-19,V_9-19,V_10-19
20,V_1-20,V_2-20,V_3-20,V_4-20,V_5-20,V_6-20,V_7-20,V_8-20,V_9-20,V_10-20
```

**data2**
```
id,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10
21,V_1-11,V_2-11,V_3-11,V_4-11,V_5-11,V_6-11,V_7-11,V_8-11,V_9-11,V_10-11
5,V_1-12,V_2-12,V_3-12,V_4-12,V_5-12,V_6-12,V_7-12,V_8-12,V_9-12,V_10-12
7,V_1-13,V_2-13,V_3-13,V_4-13,V_5-13,V_6-13,V_7-13,V_8-13,V_9-13,V_10-13
24,V_1-14,V_2-14,V_3-14,V_4-14,V_5-14,V_6-14,V_7-14,V_8-14,V_9-14,V_10-14
9,V_1-15,V_2-15,V_3-15,V_4-15,V_5-15,V_6-15,V_7-15,V_8-15,V_9-15,V_10-15
26,V_1-16,V_2-16,V_3-16,V_4-16,V_5-16,V_6-16,V_7-16,V_8-16,V_9-16,V_10-16
14,V_1-17,V_2-17,V_3-17,V_4-17,V_5-17,V_6-17,V_7-17,V_8-17,V_9-17,V_10-17
28,V_1-18,V_2-18,V_3-18,V_4-18,V_5-18,V_6-18,V_7-18,V_8-18,V_9-18,V_10-18
29,V_1-19,V_2-19,V_3-19,V_4-19,V_5-19,V_6-19,V_7-19,V_8-19,V_9-19,V_10-19
16,V_1-20,V_2-20,V_3-20,V_4-20,V_5-20,V_6-20,V_7-20,V_8-20,V_9-20,V_10-20
31,V_1-21,V_2-21,V_3-21,V_4-21,V_5-21,V_6-21,V_7-21,V_8-21,V_9-21,V_10-21
32,V_1-22,V_2-22,V_3-22,V_4-22,V_5-22,V_6-22,V_7-22,V_8-22,V_9-22,V_10-22
20,V_1-23,V_2-23,V_3-23,V_4-23,V_5-23,V_6-23,V_7-23,V_8-23,V_9-23,V_10-23
34,V_1-24,V_2-24,V_3-24,V_4-24,V_5-24,V_6-24,V_7-24,V_8-24,V_9-24,V_10-24
35,V_1-25,V_2-25,V_3-25,V_4-25,V_5-25,V_6-25,V_7-25,V_8-25,V_9-25,V_10-25
8,V_1-26,V_2-26,V_3-26,V_4-26,V_5-26,V_6-26,V_7-26,V_8-26,V_9-26,V_10-26
2,V_1-27,V_2-27,V_3-27,V_4-27,V_5-27,V_6-27,V_7-27,V_8-27,V_9-27,V_10-27
6,V_1-28,V_2-28,V_3-28,V_4-28,V_5-28,V_6-28,V_7-28,V_8-28,V_9-28,V_10-28
13,V_1-29,V_2-29,V_3-29,V_4-29,V_5-29,V_6-29,V_7-29,V_8-29,V_9-29,V_10-29
40,V_1-30,V_2-30,V_3-30,V_4-30,V_5-30,V_6-30,V_7-30,V_8-30,V_9-30,V_10-30
```

#### RML Mapping

```
@base <http://ex.com/> .
@prefix ex: <http://example.com/> .
@prefix rr: <http://www.w3.org/ns/r2rml#> .

<#TriplesMap1> a rr:TriplesMap ;
    rr:logicalTable [ a rr:LogicalTable ;
            rr:tableName "data1" ] ;
    rr:predicateObjectMap [ a rr:PredicateObjectMap ;
            rr:objectMap [ a rr:ReferenceObjectMap ;
                    rr:joinCondition [ a rr:JoinCondition ;
                            rr:child "id" ;
                            rr:parent "id" ] ;
                    rr:parentTriplesMap <#TriplesMap2> ] ;
            rr:predicateMap [ a rr:PredicateMap ;
                    rr:constant ex:j1 ] ] ;
    rr:subjectMap [ rr:template "http://ex.com/table1/{id}" ] .

<#TriplesMap2> a rr:TriplesMap ;
    rr:logicalTable [ a rr:LogicalTable ;
            rr:tableName "data2" ] ;
    rr:subjectMap [ rr:template "http://ex.com/table2/{id}" ] .
```

#### Output RDF

```
<http://ex.com/table1/13> <http://example.com/j1> <http://ex.com/table2/13> .
<http://ex.com/table1/14> <http://example.com/j1> <http://ex.com/table2/14> .
<http://ex.com/table1/16> <http://example.com/j1> <http://ex.com/table2/16> .
<http://ex.com/table1/2> <http://example.com/j1> <http://ex.com/table2/2> .
<http://ex.com/table1/20> <http://example.com/j1> <http://ex.com/table2/20> .
<http://ex.com/table1/5> <http://example.com/j1> <http://ex.com/table2/5> .
<http://ex.com/table1/6> <http://example.com/j1> <http://ex.com/table2/6> .
<http://ex.com/table1/7> <http://example.com/j1> <http://ex.com/table2/7> .
<http://ex.com/table1/8> <http://example.com/j1> <http://ex.com/table2/8> .
<http://ex.com/table1/9> <http://example.com/j1> <http://ex.com/table2/9> .
```

### Join conditions 1-1 50% with 5 conditions

More join conditions requires more conditions to be checked by the system
to result into a join.

#### Input data

**data1**
```
id,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10
1,V_1-9,V_1-9,V_1-9,V_1-9,V_1-9,V_6-1,V_7-1,V_8-1,V_9-1,V_10-1
2,V_1-2,V_2-2,V_3-2,V_4-2,V_5-2,V_6-2,V_7-2,V_8-2,V_9-2,V_10-2
3,V_1-2,V_1-2,V_1-2,V_1-2,V_1-2,V_6-3,V_7-3,V_8-3,V_9-3,V_10-3
4,V_1-14,V_1-14,V_1-14,V_1-14,V_1-14,V_6-4,V_7-4,V_8-4,V_9-4,V_10-4
5,V_1-5,V_2-5,V_3-5,V_4-5,V_5-5,V_6-5,V_7-5,V_8-5,V_9-5,V_10-5
6,V_1-6,V_1-6,V_1-6,V_1-6,V_1-6,V_6-6,V_7-6,V_8-6,V_9-6,V_10-6
7,V_1-7,V_2-7,V_3-7,V_4-7,V_5-7,V_6-7,V_7-7,V_8-7,V_9-7,V_10-7
8,V_1-8,V_2-8,V_3-8,V_4-8,V_5-8,V_6-8,V_7-8,V_8-8,V_9-8,V_10-8
9,V_1-9,V_2-9,V_3-9,V_4-9,V_5-9,V_6-9,V_7-9,V_8-9,V_9-9,V_10-9
10,V_1-10,V_2-10,V_3-10,V_4-10,V_5-10,V_6-10,V_7-10,V_8-10,V_9-10,V_10-10
11,V_1-11,V_2-11,V_3-11,V_4-11,V_5-11,V_6-11,V_7-11,V_8-11,V_9-11,V_10-11
12,V_1-12,V_2-12,V_3-12,V_4-12,V_5-12,V_6-12,V_7-12,V_8-12,V_9-12,V_10-12
13,V_1-13,V_1-13,V_1-13,V_1-13,V_1-13,V_6-13,V_7-13,V_8-13,V_9-13,V_10-13
14,V_1-20,V_1-20,V_1-20,V_1-20,V_1-20,V_6-14,V_7-14,V_8-14,V_9-14,V_10-14
15,V_1-8,V_1-8,V_1-8,V_1-8,V_1-8,V_6-15,V_7-15,V_8-15,V_9-15,V_10-15
16,V_1-7,V_1-7,V_1-7,V_1-7,V_1-7,V_6-16,V_7-16,V_8-16,V_9-16,V_10-16
17,V_1-17,V_2-17,V_3-17,V_4-17,V_5-17,V_6-17,V_7-17,V_8-17,V_9-17,V_10-17
18,V_1-16,V_1-16,V_1-16,V_1-16,V_1-16,V_6-18,V_7-18,V_8-18,V_9-18,V_10-18
19,V_1-19,V_2-19,V_3-19,V_4-19,V_5-19,V_6-19,V_7-19,V_8-19,V_9-19,V_10-19
20,V_1-5,V_1-5,V_1-5,V_1-5,V_1-5,V_6-20,V_7-20,V_8-20,V_9-20,V_10-20
```

**data2**
```
id,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10
21,V_1-14,V_1-14,V_1-14,V_1-14,V_1-14,V_6-11,V_7-11,V_8-11,V_9-11,V_10-11
22,V_1-12,V_2-12,V_3-12,V_4-12,V_5-12,V_6-12,V_7-12,V_8-12,V_9-12,V_10-12
23,V_1-13,V_2-13,V_3-13,V_4-13,V_5-13,V_6-13,V_7-13,V_8-13,V_9-13,V_10-13
24,V_1-14,V_2-14,V_3-14,V_4-14,V_5-14,V_6-14,V_7-14,V_8-14,V_9-14,V_10-14
25,V_1-6,V_1-6,V_1-6,V_1-6,V_1-6,V_6-15,V_7-15,V_8-15,V_9-15,V_10-15
26,V_1-16,V_2-16,V_3-16,V_4-16,V_5-16,V_6-16,V_7-16,V_8-16,V_9-16,V_10-16
27,V_1-13,V_1-13,V_1-13,V_1-13,V_1-13,V_6-17,V_7-17,V_8-17,V_9-17,V_10-17
28,V_1-18,V_2-18,V_3-18,V_4-18,V_5-18,V_6-18,V_7-18,V_8-18,V_9-18,V_10-18
29,V_1-8,V_1-8,V_1-8,V_1-8,V_1-8,V_6-19,V_7-19,V_8-19,V_9-19,V_10-19
30,V_1-20,V_2-20,V_3-20,V_4-20,V_5-20,V_6-20,V_7-20,V_8-20,V_9-20,V_10-20
31,V_1-2,V_1-2,V_1-2,V_1-2,V_1-2,V_6-21,V_7-21,V_8-21,V_9-21,V_10-21
32,V_1-22,V_2-22,V_3-22,V_4-22,V_5-22,V_6-22,V_7-22,V_8-22,V_9-22,V_10-22
33,V_1-23,V_2-23,V_3-23,V_4-23,V_5-23,V_6-23,V_7-23,V_8-23,V_9-23,V_10-23
34,V_1-9,V_1-9,V_1-9,V_1-9,V_1-9,V_6-24,V_7-24,V_8-24,V_9-24,V_10-24
35,V_1-7,V_1-7,V_1-7,V_1-7,V_1-7,V_6-25,V_7-25,V_8-25,V_9-25,V_10-25
36,V_1-5,V_1-5,V_1-5,V_1-5,V_1-5,V_6-26,V_7-26,V_8-26,V_9-26,V_10-26
37,V_1-16,V_1-16,V_1-16,V_1-16,V_1-16,V_6-27,V_7-27,V_8-27,V_9-27,V_10-27
38,V_1-28,V_2-28,V_3-28,V_4-28,V_5-28,V_6-28,V_7-28,V_8-28,V_9-28,V_10-28
39,V_1-29,V_2-29,V_3-29,V_4-29,V_5-29,V_6-29,V_7-29,V_8-29,V_9-29,V_10-29
40,V_1-20,V_1-20,V_1-20,V_1-20,V_1-20,V_6-30,V_7-30,V_8-30,V_9-30,V_10-30
```

#### RML Mapping

```
@base <http://ex.com/> .
@prefix ex: <http://example.com/> .
@prefix rr: <http://www.w3.org/ns/r2rml#> .

<#TriplesMap1> a rr:TriplesMap ;
    rr:logicalTable [ a rr:LogicalTable ;
            rr:tableName "data1" ] ;
    rr:predicateObjectMap [ a rr:PredicateObjectMap ;
            rr:objectMap [ a rr:ReferenceObjectMap ;
                    rr:joinCondition [ a rr:JoinCondition ;
                            rr:child "p5" ;
                            rr:parent "p5" ],
                        [ a rr:JoinCondition ;
                            rr:child "p2" ;
                            rr:parent "p2" ],
                        [ a rr:JoinCondition ;
                            rr:child "p1" ;
                            rr:parent "p1" ],
                        [ a rr:JoinCondition ;
                            rr:child "p4" ;
                            rr:parent "p4" ],
                        [ a rr:JoinCondition ;
                            rr:child "p3" ;
                            rr:parent "p3" ] ;
                    rr:parentTriplesMap <#TriplesMap2> ] ;
            rr:predicateMap [ a rr:PredicateMap ;
                    rr:constant ex:j1 ] ] ;
    rr:subjectMap [ rr:template "http://ex.com/table1/{id}" ] .

<#TriplesMap2> a rr:TriplesMap ;
    rr:logicalTable [ a rr:LogicalTable ;
            rr:tableName "data2" ] ;
    rr:subjectMap [ rr:template "http://ex.com/table2/{id}" ] .
```

#### Output RDF

```
<http://ex.com/table1/1> <http://example.com/j1> <http://ex.com/table2/34> .
<http://ex.com/table1/12> <http://example.com/j1> <http://ex.com/table2/22> .
<http://ex.com/table1/13> <http://example.com/j1> <http://ex.com/table2/27> .
<http://ex.com/table1/14> <http://example.com/j1> <http://ex.com/table2/40> .
<http://ex.com/table1/15> <http://example.com/j1> <http://ex.com/table2/29> .
<http://ex.com/table1/16> <http://example.com/j1> <http://ex.com/table2/35> .
<http://ex.com/table1/18> <http://example.com/j1> <http://ex.com/table2/37> .
<http://ex.com/table1/20> <http://example.com/j1> <http://ex.com/table2/36> .
<http://ex.com/table1/3> <http://example.com/j1> <http://ex.com/table2/31> .
<http://ex.com/table1/4> <http://example.com/j1> <http://ex.com/table2/21> .
<http://ex.com/table1/6> <http://example.com/j1> <http://ex.com/table2/25> .
```

### Join relations

The relation N-M may affect the system's performance
depending on how the joins are implemented.

#### Input data

**data1**
```
id,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10
1,V_1-9,V_2-1,V_3-1,V_4-1,V_5-1,V_6-1,V_7-1,V_8-1,V_9-1,V_10-1
2,V_1-2,V_2-2,V_3-2,V_4-2,V_5-2,V_6-2,V_7-2,V_8-2,V_9-2,V_10-2
3,V_1-2,V_2-3,V_3-3,V_4-3,V_5-3,V_6-3,V_7-3,V_8-3,V_9-3,V_10-3
4,V_1-14,V_2-4,V_3-4,V_4-4,V_5-4,V_6-4,V_7-4,V_8-4,V_9-4,V_10-4
5,V_1-5,V_2-5,V_3-5,V_4-5,V_5-5,V_6-5,V_7-5,V_8-5,V_9-5,V_10-5
6,V_1-6,V_2-6,V_3-6,V_4-6,V_5-6,V_6-6,V_7-6,V_8-6,V_9-6,V_10-6
7,V_1-7,V_2-7,V_3-7,V_4-7,V_5-7,V_6-7,V_7-7,V_8-7,V_9-7,V_10-7
8,V_1-8,V_2-8,V_3-8,V_4-8,V_5-8,V_6-8,V_7-8,V_8-8,V_9-8,V_10-8
9,V_1-9,V_2-9,V_3-9,V_4-9,V_5-9,V_6-9,V_7-9,V_8-9,V_9-9,V_10-9
10,V_1-10,V_2-10,V_3-10,V_4-10,V_5-10,V_6-10,V_7-10,V_8-10,V_9-10,V_10-10
11,V_1-11,V_2-11,V_3-11,V_4-11,V_5-11,V_6-11,V_7-11,V_8-11,V_9-11,V_10-11
12,V_1-12,V_2-12,V_3-12,V_4-12,V_5-12,V_6-12,V_7-12,V_8-12,V_9-12,V_10-12
13,V_1-13,V_2-13,V_3-13,V_4-13,V_5-13,V_6-13,V_7-13,V_8-13,V_9-13,V_10-13
14,V_1-20,V_2-14,V_3-14,V_4-14,V_5-14,V_6-14,V_7-14,V_8-14,V_9-14,V_10-14
15,V_1-8,V_2-15,V_3-15,V_4-15,V_5-15,V_6-15,V_7-15,V_8-15,V_9-15,V_10-15
16,V_1-7,V_2-16,V_3-16,V_4-16,V_5-16,V_6-16,V_7-16,V_8-16,V_9-16,V_10-16
17,V_1-17,V_2-17,V_3-17,V_4-17,V_5-17,V_6-17,V_7-17,V_8-17,V_9-17,V_10-17
18,V_1-16,V_2-18,V_3-18,V_4-18,V_5-18,V_6-18,V_7-18,V_8-18,V_9-18,V_10-18
19,V_1-19,V_2-19,V_3-19,V_4-19,V_5-19,V_6-19,V_7-19,V_8-19,V_9-19,V_10-19
20,V_1-5,V_2-20,V_3-20,V_4-20,V_5-20,V_6-20,V_7-20,V_8-20,V_9-20,V_10-20
```
**data2**
```
id,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10
21,V_1-9,V_2-11,V_3-11,V_4-11,V_5-11,V_6-11,V_7-11,V_8-11,V_9-11,V_10-11
22,V_1-12,V_2-12,V_3-12,V_4-12,V_5-12,V_6-12,V_7-12,V_8-12,V_9-12,V_10-12
23,V_1-13,V_2-13,V_3-13,V_4-13,V_5-13,V_6-13,V_7-13,V_8-13,V_9-13,V_10-13
24,V_1-14,V_2-14,V_3-14,V_4-14,V_5-14,V_6-14,V_7-14,V_8-14,V_9-14,V_10-14
25,V_1-2,V_2-15,V_3-15,V_4-15,V_5-15,V_6-15,V_7-15,V_8-15,V_9-15,V_10-15
26,V_1-16,V_2-16,V_3-16,V_4-16,V_5-16,V_6-16,V_7-16,V_8-16,V_9-16,V_10-16
27,V_1-9,V_2-17,V_3-17,V_4-17,V_5-17,V_6-17,V_7-17,V_8-17,V_9-17,V_10-17
28,V_1-18,V_2-18,V_3-18,V_4-18,V_5-18,V_6-18,V_7-18,V_8-18,V_9-18,V_10-18
29,V_1-9,V_2-19,V_3-19,V_4-19,V_5-19,V_6-19,V_7-19,V_8-19,V_9-19,V_10-19
30,V_1-20,V_2-20,V_3-20,V_4-20,V_5-20,V_6-20,V_7-20,V_8-20,V_9-20,V_10-20
31,V_1-2,V_2-21,V_3-21,V_4-21,V_5-21,V_6-21,V_7-21,V_8-21,V_9-21,V_10-21
32,V_1-22,V_2-22,V_3-22,V_4-22,V_5-22,V_6-22,V_7-22,V_8-22,V_9-22,V_10-22
33,V_1-23,V_2-23,V_3-23,V_4-23,V_5-23,V_6-23,V_7-23,V_8-23,V_9-23,V_10-23
34,V_1-9,V_2-24,V_3-24,V_4-24,V_5-24,V_6-24,V_7-24,V_8-24,V_9-24,V_10-24
35,V_1-9,V_2-25,V_3-25,V_4-25,V_5-25,V_6-25,V_7-25,V_8-25,V_9-25,V_10-25
36,V_1-2,V_2-26,V_3-26,V_4-26,V_5-26,V_6-26,V_7-26,V_8-26,V_9-26,V_10-26
37,V_1-2,V_2-27,V_3-27,V_4-27,V_5-27,V_6-27,V_7-27,V_8-27,V_9-27,V_10-27
38,V_1-28,V_2-28,V_3-28,V_4-28,V_5-28,V_6-28,V_7-28,V_8-28,V_9-28,V_10-28
39,V_1-29,V_2-29,V_3-29,V_4-29,V_5-29,V_6-29,V_7-29,V_8-29,V_9-29,V_10-29
40,V_1-2,V_2-30,V_3-30,V_4-30,V_5-30,V_6-30,V_7-30,V_8-30,V_9-30,V_10-30
```

#### RML Mapping

```
@base <http://ex.com/> .
@prefix ex: <http://example.com/> .
@prefix rr: <http://www.w3.org/ns/r2rml#> .

<#TriplesMap1> a rr:TriplesMap ;
    rr:logicalTable [ a rr:LogicalTable ;
            rr:tableName "data1" ] ;
    rr:predicateObjectMap [ a rr:PredicateObjectMap ;
            rr:objectMap [ a rr:ReferenceObjectMap ;
                    rr:joinCondition [ a rr:JoinCondition ;
                            rr:child "p1" ;
                            rr:parent "p1" ] ;
                    rr:parentTriplesMap <#TriplesMap2> ] ;
            rr:predicateMap [ a rr:PredicateMap ;
                    rr:constant ex:j1 ] ] ;
    rr:subjectMap [ rr:template "http://ex.com/table1/{id}" ] .

<#TriplesMap2> a rr:TriplesMap ;
    rr:logicalTable [ a rr:LogicalTable ;
            rr:tableName "data2" ] ;
    rr:subjectMap [ rr:template "http://ex.com/table2/{id}" ] .
```

#### Output RDF

```
<http://ex.com/table1/1> <http://example.com/j1> <http://ex.com/table2/21> .
<http://ex.com/table1/1> <http://example.com/j1> <http://ex.com/table2/27> .
<http://ex.com/table1/1> <http://example.com/j1> <http://ex.com/table2/29> .
<http://ex.com/table1/1> <http://example.com/j1> <http://ex.com/table2/34> .
<http://ex.com/table1/1> <http://example.com/j1> <http://ex.com/table2/35> .
<http://ex.com/table1/12> <http://example.com/j1> <http://ex.com/table2/22> .
<http://ex.com/table1/13> <http://example.com/j1> <http://ex.com/table2/23> .
<http://ex.com/table1/14> <http://example.com/j1> <http://ex.com/table2/30> .
<http://ex.com/table1/18> <http://example.com/j1> <http://ex.com/table2/26> .
<http://ex.com/table1/2> <http://example.com/j1> <http://ex.com/table2/25> .
<http://ex.com/table1/2> <http://example.com/j1> <http://ex.com/table2/31> .
<http://ex.com/table1/2> <http://example.com/j1> <http://ex.com/table2/36> .
<http://ex.com/table1/2> <http://example.com/j1> <http://ex.com/table2/37> .
<http://ex.com/table1/2> <http://example.com/j1> <http://ex.com/table2/40> .
<http://ex.com/table1/3> <http://example.com/j1> <http://ex.com/table2/25> .
<http://ex.com/table1/3> <http://example.com/j1> <http://ex.com/table2/31> .
<http://ex.com/table1/3> <http://example.com/j1> <http://ex.com/table2/36> .
<http://ex.com/table1/3> <http://example.com/j1> <http://ex.com/table2/37> .
<http://ex.com/table1/3> <http://example.com/j1> <http://ex.com/table2/40> .
<http://ex.com/table1/4> <http://example.com/j1> <http://ex.com/table2/24> .
<http://ex.com/table1/9> <http://example.com/j1> <http://ex.com/table2/21> .
<http://ex.com/table1/9> <http://example.com/j1> <http://ex.com/table2/27> .
<http://ex.com/table1/9> <http://example.com/j1> <http://ex.com/table2/29> .
<http://ex.com/table1/9> <http://example.com/j1> <http://ex.com/table2/34> .
<http://ex.com/table1/9> <http://example.com/j1> <http://ex.com/table2/35> .
```

### Join duplicates 10 duplicates 50%

Duplicates resulted from a join
need to be removed by the system.

#### Input data

**data1**
```
id,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10
1,V_1-1,V_2-1,V_3-1,V_4-1,V_5-1,V_6-1,V_7-1,V_8-1,V_9-1,V_10-1
2,V_1-2,V_2-2,V_3-2,V_4-2,V_5-2,V_6-2,V_7-2,V_8-2,V_9-2,V_10-2
3,V_1-3,V_2-3,V_3-3,V_4-3,V_5-3,V_6-3,V_7-3,V_8-3,V_9-3,V_10-3
4,V_1-4,V_2-4,V_3-4,V_4-4,V_5-4,V_6-4,V_7-4,V_8-4,V_9-4,V_10-4
5,V_1-5,V_2-5,V_3-5,V_4-5,V_5-5,V_6-5,V_7-5,V_8-5,V_9-5,V_10-5
6,V_1-6,V_2-6,V_3-6,V_4-6,V_5-6,V_6-6,V_7-6,V_8-6,V_9-6,V_10-6
7,V_1-7,V_2-7,V_3-7,V_4-7,V_5-7,V_6-7,V_7-7,V_8-7,V_9-7,V_10-7
8,V_1-8,V_2-8,V_3-8,V_4-8,V_5-8,V_6-8,V_7-8,V_8-8,V_9-8,V_10-8
9,V_1-9,V_2-9,V_3-9,V_4-9,V_5-9,V_6-9,V_7-9,V_8-9,V_9-9,V_10-9
10,V_1-10,V_2-10,V_3-10,V_4-10,V_5-10,V_6-10,V_7-10,V_8-10,V_9-10,V_10-10
11,V_1-11,V_2-11,V_3-11,V_4-11,V_5-11,V_6-11,V_7-11,V_8-11,V_9-11,V_10-11
12,V_1-12,V_2-12,V_3-12,V_4-12,V_5-12,V_6-12,V_7-12,V_8-12,V_9-12,V_10-12
13,V_1-13,V_2-13,V_3-13,V_4-13,V_5-13,V_6-13,V_7-13,V_8-13,V_9-13,V_10-13
14,V_1-14,V_2-14,V_3-14,V_4-14,V_5-14,V_6-14,V_7-14,V_8-14,V_9-14,V_10-14
15,V_1-15,V_2-15,V_3-15,V_4-15,V_5-15,V_6-15,V_7-15,V_8-15,V_9-15,V_10-15
16,V_1-16,V_2-16,V_3-16,V_4-16,V_5-16,V_6-16,V_7-16,V_8-16,V_9-16,V_10-16
17,V_1-17,V_2-17,V_3-17,V_4-17,V_5-17,V_6-17,V_7-17,V_8-17,V_9-17,V_10-17
18,V_1-18,V_2-18,V_3-18,V_4-18,V_5-18,V_6-18,V_7-18,V_8-18,V_9-18,V_10-18
19,V_1-19,V_2-19,V_3-19,V_4-19,V_5-19,V_6-19,V_7-19,V_8-19,V_9-19,V_10-19
20,V_1-20,V_2-20,V_3-20,V_4-20,V_5-20,V_6-20,V_7-20,V_8-20,V_9-20,V_10-20
```
**data2**
```
id,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10
21,V_1-11,V_2-11,V_3-11,V_4-11,V_5-11,V_6-11,V_7-11,V_8-11,V_9-11,V_10-11
27,V_1-20,V_2-12,V_3-12,V_4-12,V_5-12,V_6-12,V_7-12,V_8-12,V_9-12,V_10-12
23,V_1-13,V_2-13,V_3-13,V_4-13,V_5-13,V_6-13,V_7-13,V_8-13,V_9-13,V_10-13
24,V_1-14,V_2-14,V_3-14,V_4-14,V_5-14,V_6-14,V_7-14,V_8-14,V_9-14,V_10-14
27,V_1-2,V_2-15,V_3-15,V_4-15,V_5-15,V_6-15,V_7-15,V_8-15,V_9-15,V_10-15
26,V_1-16,V_2-16,V_3-16,V_4-16,V_5-16,V_6-16,V_7-16,V_8-16,V_9-16,V_10-16
27,V_1-9,V_2-17,V_3-17,V_4-17,V_5-17,V_6-17,V_7-17,V_8-17,V_9-17,V_10-17
28,V_1-18,V_2-18,V_3-18,V_4-18,V_5-18,V_6-18,V_7-18,V_8-18,V_9-18,V_10-18
27,V_1-14,V_2-19,V_3-19,V_4-19,V_5-19,V_6-19,V_7-19,V_8-19,V_9-19,V_10-19
27,V_1-13,V_2-20,V_3-20,V_4-20,V_5-20,V_6-20,V_7-20,V_8-20,V_9-20,V_10-20
31,V_1-21,V_2-21,V_3-21,V_4-21,V_5-21,V_6-21,V_7-21,V_8-21,V_9-21,V_10-21
32,V_1-22,V_2-22,V_3-22,V_4-22,V_5-22,V_6-22,V_7-22,V_8-22,V_9-22,V_10-22
27,V_1-7,V_2-23,V_3-23,V_4-23,V_5-23,V_6-23,V_7-23,V_8-23,V_9-23,V_10-23
34,V_1-24,V_2-24,V_3-24,V_4-24,V_5-24,V_6-24,V_7-24,V_8-24,V_9-24,V_10-24
35,V_1-16,V_2-25,V_3-25,V_4-25,V_5-25,V_6-25,V_7-25,V_8-25,V_9-25,V_10-25
27,V_1-6,V_2-26,V_3-26,V_4-26,V_5-26,V_6-26,V_7-26,V_8-26,V_9-26,V_10-26
27,V_1-10,V_2-27,V_3-27,V_4-27,V_5-27,V_6-27,V_7-27,V_8-27,V_9-27,V_10-27
27,V_1-5,V_2-28,V_3-28,V_4-28,V_5-28,V_6-28,V_7-28,V_8-28,V_9-28,V_10-28
27,V_1-8,V_2-29,V_3-29,V_4-29,V_5-29,V_6-29,V_7-29,V_8-29,V_9-29,V_10-29
40,V_1-30,V_2-30,V_3-30,V_4-30,V_5-30,V_6-30,V_7-30,V_8-30,V_9-30,V_10-30
```

#### RML Mapping

```
@base <http://ex.com/> .
@prefix ex: <http://example.com/> .
@prefix rr: <http://www.w3.org/ns/r2rml#> .

<#TriplesMap1> a rr:TriplesMap ;
    rr:logicalTable [ a rr:LogicalTable ;
            rr:tableName "data1" ] ;
    rr:predicateObjectMap [ a rr:PredicateObjectMap ;
            rr:objectMap [ a rr:ReferenceObjectMap ;
                    rr:joinCondition [ a rr:JoinCondition ;
                            rr:child "p1" ;
                            rr:parent "p1" ] ;
                    rr:parentTriplesMap <#TriplesMap2> ] ;
            rr:predicateMap [ a rr:PredicateMap ;
                    rr:constant ex:j1 ] ] ;
    rr:subjectMap [ rr:template "http://ex.com/table1/{id}" ] .

<#TriplesMap2> a rr:TriplesMap ;
    rr:logicalTable [ a rr:LogicalTable ;
            rr:tableName "data2" ] ;
    rr:subjectMap [ rr:template "http://ex.com/table2/{id}" ] .
```

#### Output RDF

```
<http://ex.com/table1/10> <http://example.com/j1> <http://ex.com/table2/27> .
<http://ex.com/table1/11> <http://example.com/j1> <http://ex.com/table2/21> .
<http://ex.com/table1/13> <http://example.com/j1> <http://ex.com/table2/23> .
<http://ex.com/table1/13> <http://example.com/j1> <http://ex.com/table2/27> .
<http://ex.com/table1/14> <http://example.com/j1> <http://ex.com/table2/24> .
<http://ex.com/table1/14> <http://example.com/j1> <http://ex.com/table2/27> .
<http://ex.com/table1/16> <http://example.com/j1> <http://ex.com/table2/26> .
<http://ex.com/table1/16> <http://example.com/j1> <http://ex.com/table2/35> .
<http://ex.com/table1/18> <http://example.com/j1> <http://ex.com/table2/28> .
<http://ex.com/table1/2> <http://example.com/j1> <http://ex.com/table2/27> .
<http://ex.com/table1/20> <http://example.com/j1> <http://ex.com/table2/27> .
<http://ex.com/table1/5> <http://example.com/j1> <http://ex.com/table2/27> .
<http://ex.com/table1/6> <http://example.com/j1> <http://ex.com/table2/27> .
<http://ex.com/table1/7> <http://example.com/j1> <http://ex.com/table2/27> .
<http://ex.com/table1/8> <http://example.com/j1> <http://ex.com/table2/27> .
<http://ex.com/table1/9> <http://example.com/j1> <http://ex.com/table2/27> .
```

