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
or Statically (S) as a constant. Graph Maps can appear in a
Predicate Object Map (POM) and/or Subject Map (SM).

- [Mappings: 1TM + 5POM](./RMLMapper/postgresql/mappings_1_5)
- [Mappings: 10TM + 5POM](./RMLMapper/postgresql/mappings_10_5)
- [Mappings: 20TM + 5POM](./RMLMapper/postgresql/mappings_20_5)
- [Mappings: 30TM + 5POM](./RMLMapper/postgresql/mappings_30_5)
- [Mappings: 20TM + 1POM](./RMLMapper/postgresql/mappings_20_1)
- [Mappings: 20TM + 3POM](./RMLMapper/postgresql/mappings_20_3)
- [Mappings: 20TM + 10POM](./RMLMapper/postgresql/mappings_20_10)
- [Mappings: 1TM + 1POM + 1GM-POM static](./RMLMapper/postgresql/namedgraph_0SM-NG_1POM-NG_1TM_1POM_True)
- [Mappings: 1TM + 1POM + 1GM-POM dynamic](./RMLMapper/postgresql/namedgraph_0SM-NG_1POM-NG_1TM_1POM_False)
- [Mappings: 1TM + 1POM + 5GM-POM static](./RMLMapper/postgresql/namedgraph_0SM-NG_5POM-NG_1TM_1POM_True)
- [Mappings: 1TM + 1POM + 5GM-POM dynamic](./RMLMapper/postgresql/namedgraph_0SM-NG_5POM-NG_1TM_1POM_False)
- [Mappings: 1TM + 1POM + 10GM-POM static](./RMLMapper/postgresql/namedgraph_0SM-NG_10POM-NG_1TM_1POM_True)
- [Mappings: 1TM + 1POM + 10GM-POM dynamic](./RMLMapper/postgresql/namedgraph_0SM-NG_10POM-NG_1TM_1POM_False)
- [Mappings: 1TM + 1POM + 15GM-POM static](./RMLMapper/postgresql/namedgraph_0SM-NG_15POM-NG_1TM_1POM_True)
- [Mappings: 1TM + 1POM + 15GM-POM dynamic](./RMLMapper/postgresql/namedgraph_0SM-NG_15POM-NG_1TM_1POM_False)
- [Mappings: 1TM + 5POM + 1GM-POM static](./RMLMapper/postgresql/namedgraph_0SM-NG_1POM-NG_1TM_5POM_True)
- [Mappings: 1TM + 5POM + 1GM-POM dynamic](./RMLMapper/postgresql/namedgraph_0SM-NG_1POM-NG_1TM_5POM_False)
- [Mappings: 1TM + 10POM + 1GM-POM static](./RMLMapper/postgresql/namedgraph_0SM-NG_1POM-NG_1TM_10POM_True)
- [Mappings: 1TM + 10POM + 1GM-POM dynamic](./RMLMapper/postgresql/namedgraph_0SM-NG_1POM-NG_1TM_10POM_False)
- [Mappings: 1TM + 15POM + 1GM-POM static](./RMLMapper/postgresql/namedgraph_0SM-NG_1POM-NG_1TM_15POM_True)
- [Mappings: 1TM + 15POM + 1GM-POM dynamic](./RMLMapper/postgresql/namedgraph_0SM-NG_1POM-NG_1TM_15POM_False)
- [Mappings: 1TM + 10POM + 1GM-POM + 1GM-SM static](./RMLMapper/postgresql/namedgraph_1SM-NG_1POM-NG_1TM_10POM_True)
- [Mappings: 1TM + 10POM + 1GM-POM + 1GM-SM dynamic](./RMLMapper/postgresql/namedgraph_1SM-NG_1POM-NG_1TM_10POM_False)
- [Mappings: 1TM + 10POM + 5GM-POM + 5GM-SM static](./RMLMapper/postgresql/namedgraph_5SM-NG_5POM-NG_1TM_10POM_True)
- [Mappings: 1TM + 10POM + 5GM-POM + 5GM-SM dynamic](./RMLMapper/postgresql/namedgraph_5SM-NG_5POM-NG_1TM_10POM_False)
- [Mappings: 1TM + 10POM + 10GM-POM + 10GM-SM static](./RMLMapper/postgresql/namedgraph_10SM-NG_10POM-NG_1TM_10POM_True)
- [Mappings: 1TM + 10POM + 10GM-POM + 10GM-SM dynamic](./RMLMapper/postgresql/namedgraph_10SM-NG_10POM-NG_1TM_10POM_False)
- [Mappings: 1TM + 10POM + 15GM-POM + 15GM-SM static](./RMLMapper/postgresql/namedgraph_15SM-NG_15POM-NG_1TM_10POM_True)
- [Mappings: 1TM + 10POM + 15GM-POM + 15GM-SM dynamic](./RMLMapper/postgresql/namedgraph_15SM-NG_15POM-NG_1TM_10POM_False)
- [Mappings: 1TM + 20POM + 0GM-POM + 1GM-SM static](./RMLMapper/postgresql/namedgraph_1SM-NG_0POM-NG_1TM_20POM_True)
- [Mappings: 1TM + 20POM + 0GM-POM + 1GM-SM dynamic](./RMLMapper/postgresql/namedgraph_1SM-NG_0POM-NG_1TM_20POM_False)
- [Mappings: 1TM + 20POM + 0GM-POM + 5GM-SM static](./RMLMapper/postgresql/namedgraph_5SM-NG_0POM-NG_1TM_20POM_True)
- [Mappings: 1TM + 20POM + 0GM-POM + 5GM-SM dynamic](./RMLMapper/postgresql/namedgraph_5SM-NG_0POM-NG_1TM_20POM_False)
- [Mappings: 1TM + 20POM + 0GM-POM + 10GM-SM static](./RMLMapper/postgresql/namedgraph_10SM-NG_0POM-NG_1TM_20POM_True)
- [Mappings: 1TM + 20POM + 0GM-POM + 10GM-SM dynamic](./RMLMapper/postgresql/namedgraph_10SM-NG_0POM-NG_1TM_20POM_False)
- [Mappings: 1TM + 20POM + 0GM-POM + 15GM-SM static](./RMLMapper/postgresql/namedgraph_15SM-NG_0POM-NG_1TM_20POM_True)
- [Mappings: 1TM + 20POM + 0GM-POM + 15GM-SM dynamic](./RMLMapper/postgresql/namedgraph_15SM-NG_0POM-NG_1TM_20POM_False)

## Examples

### 10 TMs + 5 POM

The more TMs, the more RDF subjects are generated.

#### Input data

```
id,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20,p21,p22,p23,p24,p25,p26,p27,p28,p29,p30
1,V_1-1,V_2-1,V_3-1,V_4-1,V_5-1,V_6-1,V_7-1,V_8-1,V_9-1,V_10-1,V_11-1,V_12-1,V_13-1,V_14-1,V_15-1,V_16-1,V_17-1,V_18-1,V_19-1,V_20-1,V_21-1,V_22-1,V_23-1,V_24-1,V_25-1,V_26-1,V_27-1,V_28-1,V_29-1,V_30-1
2,V_1-2,V_2-2,V_3-2,V_4-2,V_5-2,V_6-2,V_7-2,V_8-2,V_9-2,V_10-2,V_11-2,V_12-2,V_13-2,V_14-2,V_15-2,V_16-2,V_17-2,V_18-2,V_19-2,V_20-2,V_21-2,V_22-2,V_23-2,V_24-2,V_25-2,V_26-2,V_27-2,V_28-2,V_29-2,V_30-2
3,V_1-3,V_2-3,V_3-3,V_4-3,V_5-3,V_6-3,V_7-3,V_8-3,V_9-3,V_10-3,V_11-3,V_12-3,V_13-3,V_14-3,V_15-3,V_16-3,V_17-3,V_18-3,V_19-3,V_20-3,V_21-3,V_22-3,V_23-3,V_24-3,V_25-3,V_26-3,V_27-3,V_28-3,V_29-3,V_30-3
4,V_1-4,V_2-4,V_3-4,V_4-4,V_5-4,V_6-4,V_7-4,V_8-4,V_9-4,V_10-4,V_11-4,V_12-4,V_13-4,V_14-4,V_15-4,V_16-4,V_17-4,V_18-4,V_19-4,V_20-4,V_21-4,V_22-4,V_23-4,V_24-4,V_25-4,V_26-4,V_27-4,V_28-4,V_29-4,V_30-4
5,V_1-5,V_2-5,V_3-5,V_4-5,V_5-5,V_6-5,V_7-5,V_8-5,V_9-5,V_10-5,V_11-5,V_12-5,V_13-5,V_14-5,V_15-5,V_16-5,V_17-5,V_18-5,V_19-5,V_20-5,V_21-5,V_22-5,V_23-5,V_24-5,V_25-5,V_26-5,V_27-5,V_28-5,V_29-5,V_30-5
6,V_1-6,V_2-6,V_3-6,V_4-6,V_5-6,V_6-6,V_7-6,V_8-6,V_9-6,V_10-6,V_11-6,V_12-6,V_13-6,V_14-6,V_15-6,V_16-6,V_17-6,V_18-6,V_19-6,V_20-6,V_21-6,V_22-6,V_23-6,V_24-6,V_25-6,V_26-6,V_27-6,V_28-6,V_29-6,V_30-6
7,V_1-7,V_2-7,V_3-7,V_4-7,V_5-7,V_6-7,V_7-7,V_8-7,V_9-7,V_10-7,V_11-7,V_12-7,V_13-7,V_14-7,V_15-7,V_16-7,V_17-7,V_18-7,V_19-7,V_20-7,V_21-7,V_22-7,V_23-7,V_24-7,V_25-7,V_26-7,V_27-7,V_28-7,V_29-7,V_30-7
8,V_1-8,V_2-8,V_3-8,V_4-8,V_5-8,V_6-8,V_7-8,V_8-8,V_9-8,V_10-8,V_11-8,V_12-8,V_13-8,V_14-8,V_15-8,V_16-8,V_17-8,V_18-8,V_19-8,V_20-8,V_21-8,V_22-8,V_23-8,V_24-8,V_25-8,V_26-8,V_27-8,V_28-8,V_29-8,V_30-8
9,V_1-9,V_2-9,V_3-9,V_4-9,V_5-9,V_6-9,V_7-9,V_8-9,V_9-9,V_10-9,V_11-9,V_12-9,V_13-9,V_14-9,V_15-9,V_16-9,V_17-9,V_18-9,V_19-9,V_20-9,V_21-9,V_22-9,V_23-9,V_24-9,V_25-9,V_26-9,V_27-9,V_28-9,V_29-9,V_30-9
10,V_1-10,V_2-10,V_3-10,V_4-10,V_5-10,V_6-10,V_7-10,V_8-10,V_9-10,V_10-10,V_11-10,V_12-10,V_13-10,V_14-10,V_15-10,V_16-10,V_17-10,V_18-10,V_19-10,V_20-10,V_21-10,V_22-10,V_23-10,V_24-10,V_25-10,V_26-10,V_27-10,V_28-10,V_29-10,V_30-10
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
                    rr:column "p3" ] ;
            rr:predicateMap [ a rr:PredicateMap ;
                    rr:constant ex:p3 ] ],
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
                    rr:column "p4" ] ;
            rr:predicateMap [ a rr:PredicateMap ;
                    rr:constant ex:p4 ] ] ;
    rr:subjectMap [ rr:template "http://ex.com/table/{p1}" ] .

<#TriplesMap10> a rr:TriplesMap ;
    rr:logicalTable [ a rr:LogicalTable ;
            rr:tableName "data" ] ;
    rr:predicateObjectMap [ a rr:PredicateObjectMap ;
            rr:objectMap [ a rr:ObjectMap ;
                    rr:column "p3" ] ;
            rr:predicateMap [ a rr:PredicateMap ;
                    rr:constant ex:p3 ] ],
        [ a rr:PredicateObjectMap ;
            rr:objectMap [ a rr:ObjectMap ;
                    rr:column "p2" ] ;
            rr:predicateMap [ a rr:PredicateMap ;
                    rr:constant ex:p2 ] ],
        [ a rr:PredicateObjectMap ;
            rr:objectMap [ a rr:ObjectMap ;
                    rr:column "p1" ] ;
            rr:predicateMap [ a rr:PredicateMap ;
                    rr:constant ex:p1 ] ],
        [ a rr:PredicateObjectMap ;
            rr:objectMap [ a rr:ObjectMap ;
                    rr:column "p4" ] ;
            rr:predicateMap [ a rr:PredicateMap ;
                    rr:constant ex:p4 ] ],
        [ a rr:PredicateObjectMap ;
            rr:objectMap [ a rr:ObjectMap ;
                    rr:column "p5" ] ;
            rr:predicateMap [ a rr:PredicateMap ;
                    rr:constant ex:p5 ] ] ;
    rr:subjectMap [ rr:template "http://ex.com/table/{p10}" ] .

<#TriplesMap2> a rr:TriplesMap ;
    rr:logicalTable [ a rr:LogicalTable ;
            rr:tableName "data" ] ;
    rr:predicateObjectMap [ a rr:PredicateObjectMap ;
            rr:objectMap [ a rr:ObjectMap ;
                    rr:column "p1" ] ;
            rr:predicateMap [ a rr:PredicateMap ;
                    rr:constant ex:p1 ] ],
        [ a rr:PredicateObjectMap ;
            rr:objectMap [ a rr:ObjectMap ;
                    rr:column "p4" ] ;
            rr:predicateMap [ a rr:PredicateMap ;
                    rr:constant ex:p4 ] ],
        [ a rr:PredicateObjectMap ;
            rr:objectMap [ a rr:ObjectMap ;
                    rr:column "p3" ] ;
            rr:predicateMap [ a rr:PredicateMap ;
                    rr:constant ex:p3 ] ],
        [ a rr:PredicateObjectMap ;
            rr:objectMap [ a rr:ObjectMap ;
                    rr:column "p2" ] ;
            rr:predicateMap [ a rr:PredicateMap ;
                    rr:constant ex:p2 ] ],
        [ a rr:PredicateObjectMap ;
            rr:objectMap [ a rr:ObjectMap ;
                    rr:column "p5" ] ;
            rr:predicateMap [ a rr:PredicateMap ;
                    rr:constant ex:p5 ] ] ;
    rr:subjectMap [ rr:template "http://ex.com/table/{p2}" ] .

<#TriplesMap3> a rr:TriplesMap ;
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
                    rr:column "p3" ] ;
            rr:predicateMap [ a rr:PredicateMap ;
                    rr:constant ex:p3 ] ],
        [ a rr:PredicateObjectMap ;
            rr:objectMap [ a rr:ObjectMap ;
                    rr:column "p2" ] ;
            rr:predicateMap [ a rr:PredicateMap ;
                    rr:constant ex:p2 ] ] ;
    rr:subjectMap [ rr:template "http://ex.com/table/{p3}" ] .

<#TriplesMap4> a rr:TriplesMap ;
    rr:logicalTable [ a rr:LogicalTable ;
            rr:tableName "data" ] ;
    rr:predicateObjectMap [ a rr:PredicateObjectMap ;
            rr:objectMap [ a rr:ObjectMap ;
                    rr:column "p4" ] ;
            rr:predicateMap [ a rr:PredicateMap ;
                    rr:constant ex:p4 ] ],
        [ a rr:PredicateObjectMap ;
            rr:objectMap [ a rr:ObjectMap ;
                    rr:column "p3" ] ;
            rr:predicateMap [ a rr:PredicateMap ;
                    rr:constant ex:p3 ] ],
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
                    rr:constant ex:p2 ] ] ;
    rr:subjectMap [ rr:template "http://ex.com/table/{p4}" ] .

<#TriplesMap5> a rr:TriplesMap ;
    rr:logicalTable [ a rr:LogicalTable ;
            rr:tableName "data" ] ;
    rr:predicateObjectMap [ a rr:PredicateObjectMap ;
            rr:objectMap [ a rr:ObjectMap ;
                    rr:column "p3" ] ;
            rr:predicateMap [ a rr:PredicateMap ;
                    rr:constant ex:p3 ] ],
        [ a rr:PredicateObjectMap ;
            rr:objectMap [ a rr:ObjectMap ;
                    rr:column "p1" ] ;
            rr:predicateMap [ a rr:PredicateMap ;
                    rr:constant ex:p1 ] ],
        [ a rr:PredicateObjectMap ;
            rr:objectMap [ a rr:ObjectMap ;
                    rr:column "p5" ] ;
            rr:predicateMap [ a rr:PredicateMap ;
                    rr:constant ex:p5 ] ],
        [ a rr:PredicateObjectMap ;
            rr:objectMap [ a rr:ObjectMap ;
                    rr:column "p4" ] ;
            rr:predicateMap [ a rr:PredicateMap ;
                    rr:constant ex:p4 ] ],
        [ a rr:PredicateObjectMap ;
            rr:objectMap [ a rr:ObjectMap ;
                    rr:column "p2" ] ;
            rr:predicateMap [ a rr:PredicateMap ;
                    rr:constant ex:p2 ] ] ;
    rr:subjectMap [ rr:template "http://ex.com/table/{p5}" ] .

<#TriplesMap6> a rr:TriplesMap ;
    rr:logicalTable [ a rr:LogicalTable ;
            rr:tableName "data" ] ;
    rr:predicateObjectMap [ a rr:PredicateObjectMap ;
            rr:objectMap [ a rr:ObjectMap ;
                    rr:column "p1" ] ;
            rr:predicateMap [ a rr:PredicateMap ;
                    rr:constant ex:p1 ] ],
        [ a rr:PredicateObjectMap ;
            rr:objectMap [ a rr:ObjectMap ;
                    rr:column "p3" ] ;
            rr:predicateMap [ a rr:PredicateMap ;
                    rr:constant ex:p3 ] ],
        [ a rr:PredicateObjectMap ;
            rr:objectMap [ a rr:ObjectMap ;
                    rr:column "p2" ] ;
            rr:predicateMap [ a rr:PredicateMap ;
                    rr:constant ex:p2 ] ],
        [ a rr:PredicateObjectMap ;
            rr:objectMap [ a rr:ObjectMap ;
                    rr:column "p5" ] ;
            rr:predicateMap [ a rr:PredicateMap ;
                    rr:constant ex:p5 ] ],
        [ a rr:PredicateObjectMap ;
            rr:objectMap [ a rr:ObjectMap ;
                    rr:column "p4" ] ;
            rr:predicateMap [ a rr:PredicateMap ;
                    rr:constant ex:p4 ] ] ;
    rr:subjectMap [ rr:template "http://ex.com/table/{p6}" ] .

<#TriplesMap7> a rr:TriplesMap ;
    rr:logicalTable [ a rr:LogicalTable ;
            rr:tableName "data" ] ;
    rr:predicateObjectMap [ a rr:PredicateObjectMap ;
            rr:objectMap [ a rr:ObjectMap ;
                    rr:column "p3" ] ;
            rr:predicateMap [ a rr:PredicateMap ;
                    rr:constant ex:p3 ] ],
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
                    rr:column "p5" ] ;
            rr:predicateMap [ a rr:PredicateMap ;
                    rr:constant ex:p5 ] ],
        [ a rr:PredicateObjectMap ;
            rr:objectMap [ a rr:ObjectMap ;
                    rr:column "p4" ] ;
            rr:predicateMap [ a rr:PredicateMap ;
                    rr:constant ex:p4 ] ] ;
    rr:subjectMap [ rr:template "http://ex.com/table/{p7}" ] .

<#TriplesMap8> a rr:TriplesMap ;
    rr:logicalTable [ a rr:LogicalTable ;
            rr:tableName "data" ] ;
    rr:predicateObjectMap [ a rr:PredicateObjectMap ;
            rr:objectMap [ a rr:ObjectMap ;
                    rr:column "p1" ] ;
            rr:predicateMap [ a rr:PredicateMap ;
                    rr:constant ex:p1 ] ],
        [ a rr:PredicateObjectMap ;
            rr:objectMap [ a rr:ObjectMap ;
                    rr:column "p4" ] ;
            rr:predicateMap [ a rr:PredicateMap ;
                    rr:constant ex:p4 ] ],
        [ a rr:PredicateObjectMap ;
            rr:objectMap [ a rr:ObjectMap ;
                    rr:column "p2" ] ;
            rr:predicateMap [ a rr:PredicateMap ;
                    rr:constant ex:p2 ] ],
        [ a rr:PredicateObjectMap ;
            rr:objectMap [ a rr:ObjectMap ;
                    rr:column "p3" ] ;
            rr:predicateMap [ a rr:PredicateMap ;
                    rr:constant ex:p3 ] ],
        [ a rr:PredicateObjectMap ;
            rr:objectMap [ a rr:ObjectMap ;
                    rr:column "p5" ] ;
            rr:predicateMap [ a rr:PredicateMap ;
                    rr:constant ex:p5 ] ] ;
    rr:subjectMap [ rr:template "http://ex.com/table/{p8}" ] .

<#TriplesMap9> a rr:TriplesMap ;
    rr:logicalTable [ a rr:LogicalTable ;
            rr:tableName "data" ] ;
    rr:predicateObjectMap [ a rr:PredicateObjectMap ;
            rr:objectMap [ a rr:ObjectMap ;
                    rr:column "p3" ] ;
            rr:predicateMap [ a rr:PredicateMap ;
                    rr:constant ex:p3 ] ],
        [ a rr:PredicateObjectMap ;
            rr:objectMap [ a rr:ObjectMap ;
                    rr:column "p4" ] ;
            rr:predicateMap [ a rr:PredicateMap ;
                    rr:constant ex:p4 ] ],
        [ a rr:PredicateObjectMap ;
            rr:objectMap [ a rr:ObjectMap ;
                    rr:column "p1" ] ;
            rr:predicateMap [ a rr:PredicateMap ;
                    rr:constant ex:p1 ] ],
        [ a rr:PredicateObjectMap ;
            rr:objectMap [ a rr:ObjectMap ;
                    rr:column "p5" ] ;
            rr:predicateMap [ a rr:PredicateMap ;
                    rr:constant ex:p5 ] ],
        [ a rr:PredicateObjectMap ;
            rr:objectMap [ a rr:ObjectMap ;
                    rr:column "p2" ] ;
            rr:predicateMap [ a rr:PredicateMap ;
                    rr:constant ex:p2 ] ] ;
    rr:subjectMap [ rr:template "http://ex.com/table/{p9}" ] .
```

#### Output RDF

```
<http://ex.com/table/V_1-1> <http://example.com/p1> "V_1-1" .
<http://ex.com/table/V_1-1> <http://example.com/p2> "V_2-1" .
<http://ex.com/table/V_1-1> <http://example.com/p3> "V_3-1" .
<http://ex.com/table/V_1-1> <http://example.com/p4> "V_4-1" .
<http://ex.com/table/V_1-1> <http://example.com/p5> "V_5-1" .
<http://ex.com/table/V_1-10> <http://example.com/p1> "V_1-10" .
<http://ex.com/table/V_1-10> <http://example.com/p2> "V_2-10" .
<http://ex.com/table/V_1-10> <http://example.com/p3> "V_3-10" .
<http://ex.com/table/V_1-10> <http://example.com/p4> "V_4-10" .
<http://ex.com/table/V_1-10> <http://example.com/p5> "V_5-10" .
<http://ex.com/table/V_1-2> <http://example.com/p1> "V_1-2" .
<http://ex.com/table/V_1-2> <http://example.com/p2> "V_2-2" .
<http://ex.com/table/V_1-2> <http://example.com/p3> "V_3-2" .
<http://ex.com/table/V_1-2> <http://example.com/p4> "V_4-2" .
<http://ex.com/table/V_1-2> <http://example.com/p5> "V_5-2" .
<http://ex.com/table/V_1-3> <http://example.com/p1> "V_1-3" .
<http://ex.com/table/V_1-3> <http://example.com/p2> "V_2-3" .
<http://ex.com/table/V_1-3> <http://example.com/p3> "V_3-3" .
<http://ex.com/table/V_1-3> <http://example.com/p4> "V_4-3" .
<http://ex.com/table/V_1-3> <http://example.com/p5> "V_5-3" .
<http://ex.com/table/V_1-4> <http://example.com/p1> "V_1-4" .
<http://ex.com/table/V_1-4> <http://example.com/p2> "V_2-4" .
<http://ex.com/table/V_1-4> <http://example.com/p3> "V_3-4" .
<http://ex.com/table/V_1-4> <http://example.com/p4> "V_4-4" .
<http://ex.com/table/V_1-4> <http://example.com/p5> "V_5-4" .
<http://ex.com/table/V_1-5> <http://example.com/p1> "V_1-5" .
<http://ex.com/table/V_1-5> <http://example.com/p2> "V_2-5" .
<http://ex.com/table/V_1-5> <http://example.com/p3> "V_3-5" .
<http://ex.com/table/V_1-5> <http://example.com/p4> "V_4-5" .
<http://ex.com/table/V_1-5> <http://example.com/p5> "V_5-5" .
<http://ex.com/table/V_1-6> <http://example.com/p1> "V_1-6" .
<http://ex.com/table/V_1-6> <http://example.com/p2> "V_2-6" .
<http://ex.com/table/V_1-6> <http://example.com/p3> "V_3-6" .
<http://ex.com/table/V_1-6> <http://example.com/p4> "V_4-6" .
<http://ex.com/table/V_1-6> <http://example.com/p5> "V_5-6" .
<http://ex.com/table/V_1-7> <http://example.com/p1> "V_1-7" .
<http://ex.com/table/V_1-7> <http://example.com/p2> "V_2-7" .
<http://ex.com/table/V_1-7> <http://example.com/p3> "V_3-7" .
<http://ex.com/table/V_1-7> <http://example.com/p4> "V_4-7" .
<http://ex.com/table/V_1-7> <http://example.com/p5> "V_5-7" .
<http://ex.com/table/V_1-8> <http://example.com/p1> "V_1-8" .
<http://ex.com/table/V_1-8> <http://example.com/p2> "V_2-8" .
<http://ex.com/table/V_1-8> <http://example.com/p3> "V_3-8" .
<http://ex.com/table/V_1-8> <http://example.com/p4> "V_4-8" .
<http://ex.com/table/V_1-8> <http://example.com/p5> "V_5-8" .
<http://ex.com/table/V_1-9> <http://example.com/p1> "V_1-9" .
<http://ex.com/table/V_1-9> <http://example.com/p2> "V_2-9" .
<http://ex.com/table/V_1-9> <http://example.com/p3> "V_3-9" .
<http://ex.com/table/V_1-9> <http://example.com/p4> "V_4-9" .
<http://ex.com/table/V_1-9> <http://example.com/p5> "V_5-9" .
<http://ex.com/table/V_10-1> <http://example.com/p1> "V_1-1" .
<http://ex.com/table/V_10-1> <http://example.com/p2> "V_2-1" .
<http://ex.com/table/V_10-1> <http://example.com/p3> "V_3-1" .
<http://ex.com/table/V_10-1> <http://example.com/p4> "V_4-1" .
<http://ex.com/table/V_10-1> <http://example.com/p5> "V_5-1" .
<http://ex.com/table/V_10-10> <http://example.com/p1> "V_1-10" .
<http://ex.com/table/V_10-10> <http://example.com/p2> "V_2-10" .
<http://ex.com/table/V_10-10> <http://example.com/p3> "V_3-10" .
<http://ex.com/table/V_10-10> <http://example.com/p4> "V_4-10" .
<http://ex.com/table/V_10-10> <http://example.com/p5> "V_5-10" .
<http://ex.com/table/V_10-2> <http://example.com/p1> "V_1-2" .
<http://ex.com/table/V_10-2> <http://example.com/p2> "V_2-2" .
<http://ex.com/table/V_10-2> <http://example.com/p3> "V_3-2" .
<http://ex.com/table/V_10-2> <http://example.com/p4> "V_4-2" .
<http://ex.com/table/V_10-2> <http://example.com/p5> "V_5-2" .
<http://ex.com/table/V_10-3> <http://example.com/p1> "V_1-3" .
<http://ex.com/table/V_10-3> <http://example.com/p2> "V_2-3" .
<http://ex.com/table/V_10-3> <http://example.com/p3> "V_3-3" .
<http://ex.com/table/V_10-3> <http://example.com/p4> "V_4-3" .
<http://ex.com/table/V_10-3> <http://example.com/p5> "V_5-3" .
<http://ex.com/table/V_10-4> <http://example.com/p1> "V_1-4" .
<http://ex.com/table/V_10-4> <http://example.com/p2> "V_2-4" .
<http://ex.com/table/V_10-4> <http://example.com/p3> "V_3-4" .
<http://ex.com/table/V_10-4> <http://example.com/p4> "V_4-4" .
<http://ex.com/table/V_10-4> <http://example.com/p5> "V_5-4" .
<http://ex.com/table/V_10-5> <http://example.com/p1> "V_1-5" .
<http://ex.com/table/V_10-5> <http://example.com/p2> "V_2-5" .
<http://ex.com/table/V_10-5> <http://example.com/p3> "V_3-5" .
<http://ex.com/table/V_10-5> <http://example.com/p4> "V_4-5" .
<http://ex.com/table/V_10-5> <http://example.com/p5> "V_5-5" .
<http://ex.com/table/V_10-6> <http://example.com/p1> "V_1-6" .
<http://ex.com/table/V_10-6> <http://example.com/p2> "V_2-6" .
<http://ex.com/table/V_10-6> <http://example.com/p3> "V_3-6" .
<http://ex.com/table/V_10-6> <http://example.com/p4> "V_4-6" .
<http://ex.com/table/V_10-6> <http://example.com/p5> "V_5-6" .
<http://ex.com/table/V_10-7> <http://example.com/p1> "V_1-7" .
<http://ex.com/table/V_10-7> <http://example.com/p2> "V_2-7" .
<http://ex.com/table/V_10-7> <http://example.com/p3> "V_3-7" .
<http://ex.com/table/V_10-7> <http://example.com/p4> "V_4-7" .
<http://ex.com/table/V_10-7> <http://example.com/p5> "V_5-7" .
<http://ex.com/table/V_10-8> <http://example.com/p1> "V_1-8" .
<http://ex.com/table/V_10-8> <http://example.com/p2> "V_2-8" .
<http://ex.com/table/V_10-8> <http://example.com/p3> "V_3-8" .
<http://ex.com/table/V_10-8> <http://example.com/p4> "V_4-8" .
<http://ex.com/table/V_10-8> <http://example.com/p5> "V_5-8" .
<http://ex.com/table/V_10-9> <http://example.com/p1> "V_1-9" .
<http://ex.com/table/V_10-9> <http://example.com/p2> "V_2-9" .
<http://ex.com/table/V_10-9> <http://example.com/p3> "V_3-9" .
<http://ex.com/table/V_10-9> <http://example.com/p4> "V_4-9" .
<http://ex.com/table/V_10-9> <http://example.com/p5> "V_5-9" .
<http://ex.com/table/V_2-1> <http://example.com/p1> "V_1-1" .
<http://ex.com/table/V_2-1> <http://example.com/p2> "V_2-1" .
<http://ex.com/table/V_2-1> <http://example.com/p3> "V_3-1" .
<http://ex.com/table/V_2-1> <http://example.com/p4> "V_4-1" .
<http://ex.com/table/V_2-1> <http://example.com/p5> "V_5-1" .
<http://ex.com/table/V_2-10> <http://example.com/p1> "V_1-10" .
<http://ex.com/table/V_2-10> <http://example.com/p2> "V_2-10" .
<http://ex.com/table/V_2-10> <http://example.com/p3> "V_3-10" .
<http://ex.com/table/V_2-10> <http://example.com/p4> "V_4-10" .
<http://ex.com/table/V_2-10> <http://example.com/p5> "V_5-10" .
<http://ex.com/table/V_2-2> <http://example.com/p1> "V_1-2" .
<http://ex.com/table/V_2-2> <http://example.com/p2> "V_2-2" .
<http://ex.com/table/V_2-2> <http://example.com/p3> "V_3-2" .
<http://ex.com/table/V_2-2> <http://example.com/p4> "V_4-2" .
<http://ex.com/table/V_2-2> <http://example.com/p5> "V_5-2" .
<http://ex.com/table/V_2-3> <http://example.com/p1> "V_1-3" .
<http://ex.com/table/V_2-3> <http://example.com/p2> "V_2-3" .
<http://ex.com/table/V_2-3> <http://example.com/p3> "V_3-3" .
<http://ex.com/table/V_2-3> <http://example.com/p4> "V_4-3" .
<http://ex.com/table/V_2-3> <http://example.com/p5> "V_5-3" .
<http://ex.com/table/V_2-4> <http://example.com/p1> "V_1-4" .
<http://ex.com/table/V_2-4> <http://example.com/p2> "V_2-4" .
<http://ex.com/table/V_2-4> <http://example.com/p3> "V_3-4" .
<http://ex.com/table/V_2-4> <http://example.com/p4> "V_4-4" .
<http://ex.com/table/V_2-4> <http://example.com/p5> "V_5-4" .
<http://ex.com/table/V_2-5> <http://example.com/p1> "V_1-5" .
<http://ex.com/table/V_2-5> <http://example.com/p2> "V_2-5" .
<http://ex.com/table/V_2-5> <http://example.com/p3> "V_3-5" .
<http://ex.com/table/V_2-5> <http://example.com/p4> "V_4-5" .
<http://ex.com/table/V_2-5> <http://example.com/p5> "V_5-5" .
<http://ex.com/table/V_2-6> <http://example.com/p1> "V_1-6" .
<http://ex.com/table/V_2-6> <http://example.com/p2> "V_2-6" .
<http://ex.com/table/V_2-6> <http://example.com/p3> "V_3-6" .
<http://ex.com/table/V_2-6> <http://example.com/p4> "V_4-6" .
<http://ex.com/table/V_2-6> <http://example.com/p5> "V_5-6" .
<http://ex.com/table/V_2-7> <http://example.com/p1> "V_1-7" .
<http://ex.com/table/V_2-7> <http://example.com/p2> "V_2-7" .
<http://ex.com/table/V_2-7> <http://example.com/p3> "V_3-7" .
<http://ex.com/table/V_2-7> <http://example.com/p4> "V_4-7" .
<http://ex.com/table/V_2-7> <http://example.com/p5> "V_5-7" .
<http://ex.com/table/V_2-8> <http://example.com/p1> "V_1-8" .
<http://ex.com/table/V_2-8> <http://example.com/p2> "V_2-8" .
<http://ex.com/table/V_2-8> <http://example.com/p3> "V_3-8" .
<http://ex.com/table/V_2-8> <http://example.com/p4> "V_4-8" .
<http://ex.com/table/V_2-8> <http://example.com/p5> "V_5-8" .
<http://ex.com/table/V_2-9> <http://example.com/p1> "V_1-9" .
<http://ex.com/table/V_2-9> <http://example.com/p2> "V_2-9" .
<http://ex.com/table/V_2-9> <http://example.com/p3> "V_3-9" .
<http://ex.com/table/V_2-9> <http://example.com/p4> "V_4-9" .
<http://ex.com/table/V_2-9> <http://example.com/p5> "V_5-9" .
<http://ex.com/table/V_3-1> <http://example.com/p1> "V_1-1" .
<http://ex.com/table/V_3-1> <http://example.com/p2> "V_2-1" .
<http://ex.com/table/V_3-1> <http://example.com/p3> "V_3-1" .
<http://ex.com/table/V_3-1> <http://example.com/p4> "V_4-1" .
<http://ex.com/table/V_3-1> <http://example.com/p5> "V_5-1" .
<http://ex.com/table/V_3-10> <http://example.com/p1> "V_1-10" .
<http://ex.com/table/V_3-10> <http://example.com/p2> "V_2-10" .
<http://ex.com/table/V_3-10> <http://example.com/p3> "V_3-10" .
<http://ex.com/table/V_3-10> <http://example.com/p4> "V_4-10" .
<http://ex.com/table/V_3-10> <http://example.com/p5> "V_5-10" .
<http://ex.com/table/V_3-2> <http://example.com/p1> "V_1-2" .
<http://ex.com/table/V_3-2> <http://example.com/p2> "V_2-2" .
<http://ex.com/table/V_3-2> <http://example.com/p3> "V_3-2" .
<http://ex.com/table/V_3-2> <http://example.com/p4> "V_4-2" .
<http://ex.com/table/V_3-2> <http://example.com/p5> "V_5-2" .
<http://ex.com/table/V_3-3> <http://example.com/p1> "V_1-3" .
<http://ex.com/table/V_3-3> <http://example.com/p2> "V_2-3" .
<http://ex.com/table/V_3-3> <http://example.com/p3> "V_3-3" .
<http://ex.com/table/V_3-3> <http://example.com/p4> "V_4-3" .
<http://ex.com/table/V_3-3> <http://example.com/p5> "V_5-3" .
<http://ex.com/table/V_3-4> <http://example.com/p1> "V_1-4" .
<http://ex.com/table/V_3-4> <http://example.com/p2> "V_2-4" .
<http://ex.com/table/V_3-4> <http://example.com/p3> "V_3-4" .
<http://ex.com/table/V_3-4> <http://example.com/p4> "V_4-4" .
<http://ex.com/table/V_3-4> <http://example.com/p5> "V_5-4" .
<http://ex.com/table/V_3-5> <http://example.com/p1> "V_1-5" .
<http://ex.com/table/V_3-5> <http://example.com/p2> "V_2-5" .
<http://ex.com/table/V_3-5> <http://example.com/p3> "V_3-5" .
<http://ex.com/table/V_3-5> <http://example.com/p4> "V_4-5" .
<http://ex.com/table/V_3-5> <http://example.com/p5> "V_5-5" .
<http://ex.com/table/V_3-6> <http://example.com/p1> "V_1-6" .
<http://ex.com/table/V_3-6> <http://example.com/p2> "V_2-6" .
<http://ex.com/table/V_3-6> <http://example.com/p3> "V_3-6" .
<http://ex.com/table/V_3-6> <http://example.com/p4> "V_4-6" .
<http://ex.com/table/V_3-6> <http://example.com/p5> "V_5-6" .
<http://ex.com/table/V_3-7> <http://example.com/p1> "V_1-7" .
<http://ex.com/table/V_3-7> <http://example.com/p2> "V_2-7" .
<http://ex.com/table/V_3-7> <http://example.com/p3> "V_3-7" .
<http://ex.com/table/V_3-7> <http://example.com/p4> "V_4-7" .
<http://ex.com/table/V_3-7> <http://example.com/p5> "V_5-7" .
<http://ex.com/table/V_3-8> <http://example.com/p1> "V_1-8" .
<http://ex.com/table/V_3-8> <http://example.com/p2> "V_2-8" .
<http://ex.com/table/V_3-8> <http://example.com/p3> "V_3-8" .
<http://ex.com/table/V_3-8> <http://example.com/p4> "V_4-8" .
<http://ex.com/table/V_3-8> <http://example.com/p5> "V_5-8" .
<http://ex.com/table/V_3-9> <http://example.com/p1> "V_1-9" .
<http://ex.com/table/V_3-9> <http://example.com/p2> "V_2-9" .
<http://ex.com/table/V_3-9> <http://example.com/p3> "V_3-9" .
<http://ex.com/table/V_3-9> <http://example.com/p4> "V_4-9" .
<http://ex.com/table/V_3-9> <http://example.com/p5> "V_5-9" .
<http://ex.com/table/V_4-1> <http://example.com/p1> "V_1-1" .
<http://ex.com/table/V_4-1> <http://example.com/p2> "V_2-1" .
<http://ex.com/table/V_4-1> <http://example.com/p3> "V_3-1" .
<http://ex.com/table/V_4-1> <http://example.com/p4> "V_4-1" .
<http://ex.com/table/V_4-1> <http://example.com/p5> "V_5-1" .
<http://ex.com/table/V_4-10> <http://example.com/p1> "V_1-10" .
<http://ex.com/table/V_4-10> <http://example.com/p2> "V_2-10" .
<http://ex.com/table/V_4-10> <http://example.com/p3> "V_3-10" .
<http://ex.com/table/V_4-10> <http://example.com/p4> "V_4-10" .
<http://ex.com/table/V_4-10> <http://example.com/p5> "V_5-10" .
<http://ex.com/table/V_4-2> <http://example.com/p1> "V_1-2" .
<http://ex.com/table/V_4-2> <http://example.com/p2> "V_2-2" .
<http://ex.com/table/V_4-2> <http://example.com/p3> "V_3-2" .
<http://ex.com/table/V_4-2> <http://example.com/p4> "V_4-2" .
<http://ex.com/table/V_4-2> <http://example.com/p5> "V_5-2" .
<http://ex.com/table/V_4-3> <http://example.com/p1> "V_1-3" .
<http://ex.com/table/V_4-3> <http://example.com/p2> "V_2-3" .
<http://ex.com/table/V_4-3> <http://example.com/p3> "V_3-3" .
<http://ex.com/table/V_4-3> <http://example.com/p4> "V_4-3" .
<http://ex.com/table/V_4-3> <http://example.com/p5> "V_5-3" .
<http://ex.com/table/V_4-4> <http://example.com/p1> "V_1-4" .
<http://ex.com/table/V_4-4> <http://example.com/p2> "V_2-4" .
<http://ex.com/table/V_4-4> <http://example.com/p3> "V_3-4" .
<http://ex.com/table/V_4-4> <http://example.com/p4> "V_4-4" .
<http://ex.com/table/V_4-4> <http://example.com/p5> "V_5-4" .
<http://ex.com/table/V_4-5> <http://example.com/p1> "V_1-5" .
<http://ex.com/table/V_4-5> <http://example.com/p2> "V_2-5" .
<http://ex.com/table/V_4-5> <http://example.com/p3> "V_3-5" .
<http://ex.com/table/V_4-5> <http://example.com/p4> "V_4-5" .
<http://ex.com/table/V_4-5> <http://example.com/p5> "V_5-5" .
<http://ex.com/table/V_4-6> <http://example.com/p1> "V_1-6" .
<http://ex.com/table/V_4-6> <http://example.com/p2> "V_2-6" .
<http://ex.com/table/V_4-6> <http://example.com/p3> "V_3-6" .
<http://ex.com/table/V_4-6> <http://example.com/p4> "V_4-6" .
<http://ex.com/table/V_4-6> <http://example.com/p5> "V_5-6" .
<http://ex.com/table/V_4-7> <http://example.com/p1> "V_1-7" .
<http://ex.com/table/V_4-7> <http://example.com/p2> "V_2-7" .
<http://ex.com/table/V_4-7> <http://example.com/p3> "V_3-7" .
<http://ex.com/table/V_4-7> <http://example.com/p4> "V_4-7" .
<http://ex.com/table/V_4-7> <http://example.com/p5> "V_5-7" .
<http://ex.com/table/V_4-8> <http://example.com/p1> "V_1-8" .
<http://ex.com/table/V_4-8> <http://example.com/p2> "V_2-8" .
<http://ex.com/table/V_4-8> <http://example.com/p3> "V_3-8" .
<http://ex.com/table/V_4-8> <http://example.com/p4> "V_4-8" .
<http://ex.com/table/V_4-8> <http://example.com/p5> "V_5-8" .
<http://ex.com/table/V_4-9> <http://example.com/p1> "V_1-9" .
<http://ex.com/table/V_4-9> <http://example.com/p2> "V_2-9" .
<http://ex.com/table/V_4-9> <http://example.com/p3> "V_3-9" .
<http://ex.com/table/V_4-9> <http://example.com/p4> "V_4-9" .
<http://ex.com/table/V_4-9> <http://example.com/p5> "V_5-9" .
<http://ex.com/table/V_5-1> <http://example.com/p1> "V_1-1" .
<http://ex.com/table/V_5-1> <http://example.com/p2> "V_2-1" .
<http://ex.com/table/V_5-1> <http://example.com/p3> "V_3-1" .
<http://ex.com/table/V_5-1> <http://example.com/p4> "V_4-1" .
<http://ex.com/table/V_5-1> <http://example.com/p5> "V_5-1" .
<http://ex.com/table/V_5-10> <http://example.com/p1> "V_1-10" .
<http://ex.com/table/V_5-10> <http://example.com/p2> "V_2-10" .
<http://ex.com/table/V_5-10> <http://example.com/p3> "V_3-10" .
<http://ex.com/table/V_5-10> <http://example.com/p4> "V_4-10" .
<http://ex.com/table/V_5-10> <http://example.com/p5> "V_5-10" .
<http://ex.com/table/V_5-2> <http://example.com/p1> "V_1-2" .
<http://ex.com/table/V_5-2> <http://example.com/p2> "V_2-2" .
<http://ex.com/table/V_5-2> <http://example.com/p3> "V_3-2" .
<http://ex.com/table/V_5-2> <http://example.com/p4> "V_4-2" .
<http://ex.com/table/V_5-2> <http://example.com/p5> "V_5-2" .
<http://ex.com/table/V_5-3> <http://example.com/p1> "V_1-3" .
<http://ex.com/table/V_5-3> <http://example.com/p2> "V_2-3" .
<http://ex.com/table/V_5-3> <http://example.com/p3> "V_3-3" .
<http://ex.com/table/V_5-3> <http://example.com/p4> "V_4-3" .
<http://ex.com/table/V_5-3> <http://example.com/p5> "V_5-3" .
<http://ex.com/table/V_5-4> <http://example.com/p1> "V_1-4" .
<http://ex.com/table/V_5-4> <http://example.com/p2> "V_2-4" .
<http://ex.com/table/V_5-4> <http://example.com/p3> "V_3-4" .
<http://ex.com/table/V_5-4> <http://example.com/p4> "V_4-4" .
<http://ex.com/table/V_5-4> <http://example.com/p5> "V_5-4" .
<http://ex.com/table/V_5-5> <http://example.com/p1> "V_1-5" .
<http://ex.com/table/V_5-5> <http://example.com/p2> "V_2-5" .
<http://ex.com/table/V_5-5> <http://example.com/p3> "V_3-5" .
<http://ex.com/table/V_5-5> <http://example.com/p4> "V_4-5" .
<http://ex.com/table/V_5-5> <http://example.com/p5> "V_5-5" .
<http://ex.com/table/V_5-6> <http://example.com/p1> "V_1-6" .
<http://ex.com/table/V_5-6> <http://example.com/p2> "V_2-6" .
<http://ex.com/table/V_5-6> <http://example.com/p3> "V_3-6" .
<http://ex.com/table/V_5-6> <http://example.com/p4> "V_4-6" .
<http://ex.com/table/V_5-6> <http://example.com/p5> "V_5-6" .
<http://ex.com/table/V_5-7> <http://example.com/p1> "V_1-7" .
<http://ex.com/table/V_5-7> <http://example.com/p2> "V_2-7" .
<http://ex.com/table/V_5-7> <http://example.com/p3> "V_3-7" .
<http://ex.com/table/V_5-7> <http://example.com/p4> "V_4-7" .
<http://ex.com/table/V_5-7> <http://example.com/p5> "V_5-7" .
<http://ex.com/table/V_5-8> <http://example.com/p1> "V_1-8" .
<http://ex.com/table/V_5-8> <http://example.com/p2> "V_2-8" .
<http://ex.com/table/V_5-8> <http://example.com/p3> "V_3-8" .
<http://ex.com/table/V_5-8> <http://example.com/p4> "V_4-8" .
<http://ex.com/table/V_5-8> <http://example.com/p5> "V_5-8" .
<http://ex.com/table/V_5-9> <http://example.com/p1> "V_1-9" .
<http://ex.com/table/V_5-9> <http://example.com/p2> "V_2-9" .
<http://ex.com/table/V_5-9> <http://example.com/p3> "V_3-9" .
<http://ex.com/table/V_5-9> <http://example.com/p4> "V_4-9" .
<http://ex.com/table/V_5-9> <http://example.com/p5> "V_5-9" .
<http://ex.com/table/V_6-1> <http://example.com/p1> "V_1-1" .
<http://ex.com/table/V_6-1> <http://example.com/p2> "V_2-1" .
<http://ex.com/table/V_6-1> <http://example.com/p3> "V_3-1" .
<http://ex.com/table/V_6-1> <http://example.com/p4> "V_4-1" .
<http://ex.com/table/V_6-1> <http://example.com/p5> "V_5-1" .
<http://ex.com/table/V_6-10> <http://example.com/p1> "V_1-10" .
<http://ex.com/table/V_6-10> <http://example.com/p2> "V_2-10" .
<http://ex.com/table/V_6-10> <http://example.com/p3> "V_3-10" .
<http://ex.com/table/V_6-10> <http://example.com/p4> "V_4-10" .
<http://ex.com/table/V_6-10> <http://example.com/p5> "V_5-10" .
<http://ex.com/table/V_6-2> <http://example.com/p1> "V_1-2" .
<http://ex.com/table/V_6-2> <http://example.com/p2> "V_2-2" .
<http://ex.com/table/V_6-2> <http://example.com/p3> "V_3-2" .
<http://ex.com/table/V_6-2> <http://example.com/p4> "V_4-2" .
<http://ex.com/table/V_6-2> <http://example.com/p5> "V_5-2" .
<http://ex.com/table/V_6-3> <http://example.com/p1> "V_1-3" .
<http://ex.com/table/V_6-3> <http://example.com/p2> "V_2-3" .
<http://ex.com/table/V_6-3> <http://example.com/p3> "V_3-3" .
<http://ex.com/table/V_6-3> <http://example.com/p4> "V_4-3" .
<http://ex.com/table/V_6-3> <http://example.com/p5> "V_5-3" .
<http://ex.com/table/V_6-4> <http://example.com/p1> "V_1-4" .
<http://ex.com/table/V_6-4> <http://example.com/p2> "V_2-4" .
<http://ex.com/table/V_6-4> <http://example.com/p3> "V_3-4" .
<http://ex.com/table/V_6-4> <http://example.com/p4> "V_4-4" .
<http://ex.com/table/V_6-4> <http://example.com/p5> "V_5-4" .
<http://ex.com/table/V_6-5> <http://example.com/p1> "V_1-5" .
<http://ex.com/table/V_6-5> <http://example.com/p2> "V_2-5" .
<http://ex.com/table/V_6-5> <http://example.com/p3> "V_3-5" .
<http://ex.com/table/V_6-5> <http://example.com/p4> "V_4-5" .
<http://ex.com/table/V_6-5> <http://example.com/p5> "V_5-5" .
<http://ex.com/table/V_6-6> <http://example.com/p1> "V_1-6" .
<http://ex.com/table/V_6-6> <http://example.com/p2> "V_2-6" .
<http://ex.com/table/V_6-6> <http://example.com/p3> "V_3-6" .
<http://ex.com/table/V_6-6> <http://example.com/p4> "V_4-6" .
<http://ex.com/table/V_6-6> <http://example.com/p5> "V_5-6" .
<http://ex.com/table/V_6-7> <http://example.com/p1> "V_1-7" .
<http://ex.com/table/V_6-7> <http://example.com/p2> "V_2-7" .
<http://ex.com/table/V_6-7> <http://example.com/p3> "V_3-7" .
<http://ex.com/table/V_6-7> <http://example.com/p4> "V_4-7" .
<http://ex.com/table/V_6-7> <http://example.com/p5> "V_5-7" .
<http://ex.com/table/V_6-8> <http://example.com/p1> "V_1-8" .
<http://ex.com/table/V_6-8> <http://example.com/p2> "V_2-8" .
<http://ex.com/table/V_6-8> <http://example.com/p3> "V_3-8" .
<http://ex.com/table/V_6-8> <http://example.com/p4> "V_4-8" .
<http://ex.com/table/V_6-8> <http://example.com/p5> "V_5-8" .
<http://ex.com/table/V_6-9> <http://example.com/p1> "V_1-9" .
<http://ex.com/table/V_6-9> <http://example.com/p2> "V_2-9" .
<http://ex.com/table/V_6-9> <http://example.com/p3> "V_3-9" .
<http://ex.com/table/V_6-9> <http://example.com/p4> "V_4-9" .
<http://ex.com/table/V_6-9> <http://example.com/p5> "V_5-9" .
<http://ex.com/table/V_7-1> <http://example.com/p1> "V_1-1" .
<http://ex.com/table/V_7-1> <http://example.com/p2> "V_2-1" .
<http://ex.com/table/V_7-1> <http://example.com/p3> "V_3-1" .
<http://ex.com/table/V_7-1> <http://example.com/p4> "V_4-1" .
<http://ex.com/table/V_7-1> <http://example.com/p5> "V_5-1" .
<http://ex.com/table/V_7-10> <http://example.com/p1> "V_1-10" .
<http://ex.com/table/V_7-10> <http://example.com/p2> "V_2-10" .
<http://ex.com/table/V_7-10> <http://example.com/p3> "V_3-10" .
<http://ex.com/table/V_7-10> <http://example.com/p4> "V_4-10" .
<http://ex.com/table/V_7-10> <http://example.com/p5> "V_5-10" .
<http://ex.com/table/V_7-2> <http://example.com/p1> "V_1-2" .
<http://ex.com/table/V_7-2> <http://example.com/p2> "V_2-2" .
<http://ex.com/table/V_7-2> <http://example.com/p3> "V_3-2" .
<http://ex.com/table/V_7-2> <http://example.com/p4> "V_4-2" .
<http://ex.com/table/V_7-2> <http://example.com/p5> "V_5-2" .
<http://ex.com/table/V_7-3> <http://example.com/p1> "V_1-3" .
<http://ex.com/table/V_7-3> <http://example.com/p2> "V_2-3" .
<http://ex.com/table/V_7-3> <http://example.com/p3> "V_3-3" .
<http://ex.com/table/V_7-3> <http://example.com/p4> "V_4-3" .
<http://ex.com/table/V_7-3> <http://example.com/p5> "V_5-3" .
<http://ex.com/table/V_7-4> <http://example.com/p1> "V_1-4" .
<http://ex.com/table/V_7-4> <http://example.com/p2> "V_2-4" .
<http://ex.com/table/V_7-4> <http://example.com/p3> "V_3-4" .
<http://ex.com/table/V_7-4> <http://example.com/p4> "V_4-4" .
<http://ex.com/table/V_7-4> <http://example.com/p5> "V_5-4" .
<http://ex.com/table/V_7-5> <http://example.com/p1> "V_1-5" .
<http://ex.com/table/V_7-5> <http://example.com/p2> "V_2-5" .
<http://ex.com/table/V_7-5> <http://example.com/p3> "V_3-5" .
<http://ex.com/table/V_7-5> <http://example.com/p4> "V_4-5" .
<http://ex.com/table/V_7-5> <http://example.com/p5> "V_5-5" .
<http://ex.com/table/V_7-6> <http://example.com/p1> "V_1-6" .
<http://ex.com/table/V_7-6> <http://example.com/p2> "V_2-6" .
<http://ex.com/table/V_7-6> <http://example.com/p3> "V_3-6" .
<http://ex.com/table/V_7-6> <http://example.com/p4> "V_4-6" .
<http://ex.com/table/V_7-6> <http://example.com/p5> "V_5-6" .
<http://ex.com/table/V_7-7> <http://example.com/p1> "V_1-7" .
<http://ex.com/table/V_7-7> <http://example.com/p2> "V_2-7" .
<http://ex.com/table/V_7-7> <http://example.com/p3> "V_3-7" .
<http://ex.com/table/V_7-7> <http://example.com/p4> "V_4-7" .
<http://ex.com/table/V_7-7> <http://example.com/p5> "V_5-7" .
<http://ex.com/table/V_7-8> <http://example.com/p1> "V_1-8" .
<http://ex.com/table/V_7-8> <http://example.com/p2> "V_2-8" .
<http://ex.com/table/V_7-8> <http://example.com/p3> "V_3-8" .
<http://ex.com/table/V_7-8> <http://example.com/p4> "V_4-8" .
<http://ex.com/table/V_7-8> <http://example.com/p5> "V_5-8" .
<http://ex.com/table/V_7-9> <http://example.com/p1> "V_1-9" .
<http://ex.com/table/V_7-9> <http://example.com/p2> "V_2-9" .
<http://ex.com/table/V_7-9> <http://example.com/p3> "V_3-9" .
<http://ex.com/table/V_7-9> <http://example.com/p4> "V_4-9" .
<http://ex.com/table/V_7-9> <http://example.com/p5> "V_5-9" .
<http://ex.com/table/V_8-1> <http://example.com/p1> "V_1-1" .
<http://ex.com/table/V_8-1> <http://example.com/p2> "V_2-1" .
<http://ex.com/table/V_8-1> <http://example.com/p3> "V_3-1" .
<http://ex.com/table/V_8-1> <http://example.com/p4> "V_4-1" .
<http://ex.com/table/V_8-1> <http://example.com/p5> "V_5-1" .
<http://ex.com/table/V_8-10> <http://example.com/p1> "V_1-10" .
<http://ex.com/table/V_8-10> <http://example.com/p2> "V_2-10" .
<http://ex.com/table/V_8-10> <http://example.com/p3> "V_3-10" .
<http://ex.com/table/V_8-10> <http://example.com/p4> "V_4-10" .
<http://ex.com/table/V_8-10> <http://example.com/p5> "V_5-10" .
<http://ex.com/table/V_8-2> <http://example.com/p1> "V_1-2" .
<http://ex.com/table/V_8-2> <http://example.com/p2> "V_2-2" .
<http://ex.com/table/V_8-2> <http://example.com/p3> "V_3-2" .
<http://ex.com/table/V_8-2> <http://example.com/p4> "V_4-2" .
<http://ex.com/table/V_8-2> <http://example.com/p5> "V_5-2" .
<http://ex.com/table/V_8-3> <http://example.com/p1> "V_1-3" .
<http://ex.com/table/V_8-3> <http://example.com/p2> "V_2-3" .
<http://ex.com/table/V_8-3> <http://example.com/p3> "V_3-3" .
<http://ex.com/table/V_8-3> <http://example.com/p4> "V_4-3" .
<http://ex.com/table/V_8-3> <http://example.com/p5> "V_5-3" .
<http://ex.com/table/V_8-4> <http://example.com/p1> "V_1-4" .
<http://ex.com/table/V_8-4> <http://example.com/p2> "V_2-4" .
<http://ex.com/table/V_8-4> <http://example.com/p3> "V_3-4" .
<http://ex.com/table/V_8-4> <http://example.com/p4> "V_4-4" .
<http://ex.com/table/V_8-4> <http://example.com/p5> "V_5-4" .
<http://ex.com/table/V_8-5> <http://example.com/p1> "V_1-5" .
<http://ex.com/table/V_8-5> <http://example.com/p2> "V_2-5" .
<http://ex.com/table/V_8-5> <http://example.com/p3> "V_3-5" .
<http://ex.com/table/V_8-5> <http://example.com/p4> "V_4-5" .
<http://ex.com/table/V_8-5> <http://example.com/p5> "V_5-5" .
<http://ex.com/table/V_8-6> <http://example.com/p1> "V_1-6" .
<http://ex.com/table/V_8-6> <http://example.com/p2> "V_2-6" .
<http://ex.com/table/V_8-6> <http://example.com/p3> "V_3-6" .
<http://ex.com/table/V_8-6> <http://example.com/p4> "V_4-6" .
<http://ex.com/table/V_8-6> <http://example.com/p5> "V_5-6" .
<http://ex.com/table/V_8-7> <http://example.com/p1> "V_1-7" .
<http://ex.com/table/V_8-7> <http://example.com/p2> "V_2-7" .
<http://ex.com/table/V_8-7> <http://example.com/p3> "V_3-7" .
<http://ex.com/table/V_8-7> <http://example.com/p4> "V_4-7" .
<http://ex.com/table/V_8-7> <http://example.com/p5> "V_5-7" .
<http://ex.com/table/V_8-8> <http://example.com/p1> "V_1-8" .
<http://ex.com/table/V_8-8> <http://example.com/p2> "V_2-8" .
<http://ex.com/table/V_8-8> <http://example.com/p3> "V_3-8" .
<http://ex.com/table/V_8-8> <http://example.com/p4> "V_4-8" .
<http://ex.com/table/V_8-8> <http://example.com/p5> "V_5-8" .
<http://ex.com/table/V_8-9> <http://example.com/p1> "V_1-9" .
<http://ex.com/table/V_8-9> <http://example.com/p2> "V_2-9" .
<http://ex.com/table/V_8-9> <http://example.com/p3> "V_3-9" .
<http://ex.com/table/V_8-9> <http://example.com/p4> "V_4-9" .
<http://ex.com/table/V_8-9> <http://example.com/p5> "V_5-9" .
<http://ex.com/table/V_9-1> <http://example.com/p1> "V_1-1" .
<http://ex.com/table/V_9-1> <http://example.com/p2> "V_2-1" .
<http://ex.com/table/V_9-1> <http://example.com/p3> "V_3-1" .
<http://ex.com/table/V_9-1> <http://example.com/p4> "V_4-1" .
<http://ex.com/table/V_9-1> <http://example.com/p5> "V_5-1" .
<http://ex.com/table/V_9-10> <http://example.com/p1> "V_1-10" .
<http://ex.com/table/V_9-10> <http://example.com/p2> "V_2-10" .
<http://ex.com/table/V_9-10> <http://example.com/p3> "V_3-10" .
<http://ex.com/table/V_9-10> <http://example.com/p4> "V_4-10" .
<http://ex.com/table/V_9-10> <http://example.com/p5> "V_5-10" .
<http://ex.com/table/V_9-2> <http://example.com/p1> "V_1-2" .
<http://ex.com/table/V_9-2> <http://example.com/p2> "V_2-2" .
<http://ex.com/table/V_9-2> <http://example.com/p3> "V_3-2" .
<http://ex.com/table/V_9-2> <http://example.com/p4> "V_4-2" .
<http://ex.com/table/V_9-2> <http://example.com/p5> "V_5-2" .
<http://ex.com/table/V_9-3> <http://example.com/p1> "V_1-3" .
<http://ex.com/table/V_9-3> <http://example.com/p2> "V_2-3" .
<http://ex.com/table/V_9-3> <http://example.com/p3> "V_3-3" .
<http://ex.com/table/V_9-3> <http://example.com/p4> "V_4-3" .
<http://ex.com/table/V_9-3> <http://example.com/p5> "V_5-3" .
<http://ex.com/table/V_9-4> <http://example.com/p1> "V_1-4" .
<http://ex.com/table/V_9-4> <http://example.com/p2> "V_2-4" .
<http://ex.com/table/V_9-4> <http://example.com/p3> "V_3-4" .
<http://ex.com/table/V_9-4> <http://example.com/p4> "V_4-4" .
<http://ex.com/table/V_9-4> <http://example.com/p5> "V_5-4" .
<http://ex.com/table/V_9-5> <http://example.com/p1> "V_1-5" .
<http://ex.com/table/V_9-5> <http://example.com/p2> "V_2-5" .
<http://ex.com/table/V_9-5> <http://example.com/p3> "V_3-5" .
<http://ex.com/table/V_9-5> <http://example.com/p4> "V_4-5" .
<http://ex.com/table/V_9-5> <http://example.com/p5> "V_5-5" .
<http://ex.com/table/V_9-6> <http://example.com/p1> "V_1-6" .
<http://ex.com/table/V_9-6> <http://example.com/p2> "V_2-6" .
<http://ex.com/table/V_9-6> <http://example.com/p3> "V_3-6" .
<http://ex.com/table/V_9-6> <http://example.com/p4> "V_4-6" .
<http://ex.com/table/V_9-6> <http://example.com/p5> "V_5-6" .
<http://ex.com/table/V_9-7> <http://example.com/p1> "V_1-7" .
<http://ex.com/table/V_9-7> <http://example.com/p2> "V_2-7" .
<http://ex.com/table/V_9-7> <http://example.com/p3> "V_3-7" .
<http://ex.com/table/V_9-7> <http://example.com/p4> "V_4-7" .
<http://ex.com/table/V_9-7> <http://example.com/p5> "V_5-7" .
<http://ex.com/table/V_9-8> <http://example.com/p1> "V_1-8" .
<http://ex.com/table/V_9-8> <http://example.com/p2> "V_2-8" .
<http://ex.com/table/V_9-8> <http://example.com/p3> "V_3-8" .
<http://ex.com/table/V_9-8> <http://example.com/p4> "V_4-8" .
<http://ex.com/table/V_9-8> <http://example.com/p5> "V_5-8" .
<http://ex.com/table/V_9-9> <http://example.com/p1> "V_1-9" .
<http://ex.com/table/V_9-9> <http://example.com/p2> "V_2-9" .
<http://ex.com/table/V_9-9> <http://example.com/p3> "V_3-9" .
<http://ex.com/table/V_9-9> <http://example.com/p4> "V_4-9" .
<http://ex.com/table/V_9-9> <http://example.com/p5> "V_5-9" .
```

### 1 TM + 5 POMs

The more POMs, the more RDF predicates and objects are generated per RDF subject.

#### Input data

```
id,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20,p21,p22,p23,p24,p25,p26,p27,p28,p29,p30
1,V_1-1,V_2-1,V_3-1,V_4-1,V_5-1,V_6-1,V_7-1,V_8-1,V_9-1,V_10-1,V_11-1,V_12-1,V_13-1,V_14-1,V_15-1,V_16-1,V_17-1,V_18-1,V_19-1,V_20-1,V_21-1,V_22-1,V_23-1,V_24-1,V_25-1,V_26-1,V_27-1,V_28-1,V_29-1,V_30-1
2,V_1-2,V_2-2,V_3-2,V_4-2,V_5-2,V_6-2,V_7-2,V_8-2,V_9-2,V_10-2,V_11-2,V_12-2,V_13-2,V_14-2,V_15-2,V_16-2,V_17-2,V_18-2,V_19-2,V_20-2,V_21-2,V_22-2,V_23-2,V_24-2,V_25-2,V_26-2,V_27-2,V_28-2,V_29-2,V_30-2
3,V_1-3,V_2-3,V_3-3,V_4-3,V_5-3,V_6-3,V_7-3,V_8-3,V_9-3,V_10-3,V_11-3,V_12-3,V_13-3,V_14-3,V_15-3,V_16-3,V_17-3,V_18-3,V_19-3,V_20-3,V_21-3,V_22-3,V_23-3,V_24-3,V_25-3,V_26-3,V_27-3,V_28-3,V_29-3,V_30-3
4,V_1-4,V_2-4,V_3-4,V_4-4,V_5-4,V_6-4,V_7-4,V_8-4,V_9-4,V_10-4,V_11-4,V_12-4,V_13-4,V_14-4,V_15-4,V_16-4,V_17-4,V_18-4,V_19-4,V_20-4,V_21-4,V_22-4,V_23-4,V_24-4,V_25-4,V_26-4,V_27-4,V_28-4,V_29-4,V_30-4
5,V_1-5,V_2-5,V_3-5,V_4-5,V_5-5,V_6-5,V_7-5,V_8-5,V_9-5,V_10-5,V_11-5,V_12-5,V_13-5,V_14-5,V_15-5,V_16-5,V_17-5,V_18-5,V_19-5,V_20-5,V_21-5,V_22-5,V_23-5,V_24-5,V_25-5,V_26-5,V_27-5,V_28-5,V_29-5,V_30-5
6,V_1-6,V_2-6,V_3-6,V_4-6,V_5-6,V_6-6,V_7-6,V_8-6,V_9-6,V_10-6,V_11-6,V_12-6,V_13-6,V_14-6,V_15-6,V_16-6,V_17-6,V_18-6,V_19-6,V_20-6,V_21-6,V_22-6,V_23-6,V_24-6,V_25-6,V_26-6,V_27-6,V_28-6,V_29-6,V_30-6
7,V_1-7,V_2-7,V_3-7,V_4-7,V_5-7,V_6-7,V_7-7,V_8-7,V_9-7,V_10-7,V_11-7,V_12-7,V_13-7,V_14-7,V_15-7,V_16-7,V_17-7,V_18-7,V_19-7,V_20-7,V_21-7,V_22-7,V_23-7,V_24-7,V_25-7,V_26-7,V_27-7,V_28-7,V_29-7,V_30-7
8,V_1-8,V_2-8,V_3-8,V_4-8,V_5-8,V_6-8,V_7-8,V_8-8,V_9-8,V_10-8,V_11-8,V_12-8,V_13-8,V_14-8,V_15-8,V_16-8,V_17-8,V_18-8,V_19-8,V_20-8,V_21-8,V_22-8,V_23-8,V_24-8,V_25-8,V_26-8,V_27-8,V_28-8,V_29-8,V_30-8
9,V_1-9,V_2-9,V_3-9,V_4-9,V_5-9,V_6-9,V_7-9,V_8-9,V_9-9,V_10-9,V_11-9,V_12-9,V_13-9,V_14-9,V_15-9,V_16-9,V_17-9,V_18-9,V_19-9,V_20-9,V_21-9,V_22-9,V_23-9,V_24-9,V_25-9,V_26-9,V_27-9,V_28-9,V_29-9,V_30-9
10,V_1-10,V_2-10,V_3-10,V_4-10,V_5-10,V_6-10,V_7-10,V_8-10,V_9-10,V_10-10,V_11-10,V_12-10,V_13-10,V_14-10,V_15-10,V_16-10,V_17-10,V_18-10,V_19-10,V_20-10,V_21-10,V_22-10,V_23-10,V_24-10,V_25-10,V_26-10,V_27-10,V_28-10,V_29-10,V_30-10
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
                    rr:column "p2" ] ;
            rr:predicateMap [ a rr:PredicateMap ;
                    rr:constant ex:p2 ] ],
        [ a rr:PredicateObjectMap ;
            rr:objectMap [ a rr:ObjectMap ;
                    rr:column "p1" ] ;
            rr:predicateMap [ a rr:PredicateMap ;
                    rr:constant ex:p1 ] ],
        [ a rr:PredicateObjectMap ;
            rr:objectMap [ a rr:ObjectMap ;
                    rr:column "p3" ] ;
            rr:predicateMap [ a rr:PredicateMap ;
                    rr:constant ex:p3 ] ] ;
    rr:subjectMap [ rr:template "http://ex.com/table/{p1}" ] .
```

#### Output RDF

```
<http://ex.com/table/V_1-1> <http://example.com/p1> "V_1-1" .
<http://ex.com/table/V_1-1> <http://example.com/p2> "V_2-1" .
<http://ex.com/table/V_1-1> <http://example.com/p3> "V_3-1" .
<http://ex.com/table/V_1-1> <http://example.com/p4> "V_4-1" .
<http://ex.com/table/V_1-1> <http://example.com/p5> "V_5-1" .
<http://ex.com/table/V_1-10> <http://example.com/p1> "V_1-10" .
<http://ex.com/table/V_1-10> <http://example.com/p2> "V_2-10" .
<http://ex.com/table/V_1-10> <http://example.com/p3> "V_3-10" .
<http://ex.com/table/V_1-10> <http://example.com/p4> "V_4-10" .
<http://ex.com/table/V_1-10> <http://example.com/p5> "V_5-10" .
<http://ex.com/table/V_1-2> <http://example.com/p1> "V_1-2" .
<http://ex.com/table/V_1-2> <http://example.com/p2> "V_2-2" .
<http://ex.com/table/V_1-2> <http://example.com/p3> "V_3-2" .
<http://ex.com/table/V_1-2> <http://example.com/p4> "V_4-2" .
<http://ex.com/table/V_1-2> <http://example.com/p5> "V_5-2" .
<http://ex.com/table/V_1-3> <http://example.com/p1> "V_1-3" .
<http://ex.com/table/V_1-3> <http://example.com/p2> "V_2-3" .
<http://ex.com/table/V_1-3> <http://example.com/p3> "V_3-3" .
<http://ex.com/table/V_1-3> <http://example.com/p4> "V_4-3" .
<http://ex.com/table/V_1-3> <http://example.com/p5> "V_5-3" .
<http://ex.com/table/V_1-4> <http://example.com/p1> "V_1-4" .
<http://ex.com/table/V_1-4> <http://example.com/p2> "V_2-4" .
<http://ex.com/table/V_1-4> <http://example.com/p3> "V_3-4" .
<http://ex.com/table/V_1-4> <http://example.com/p4> "V_4-4" .
<http://ex.com/table/V_1-4> <http://example.com/p5> "V_5-4" .
<http://ex.com/table/V_1-5> <http://example.com/p1> "V_1-5" .
<http://ex.com/table/V_1-5> <http://example.com/p2> "V_2-5" .
<http://ex.com/table/V_1-5> <http://example.com/p3> "V_3-5" .
<http://ex.com/table/V_1-5> <http://example.com/p4> "V_4-5" .
<http://ex.com/table/V_1-5> <http://example.com/p5> "V_5-5" .
<http://ex.com/table/V_1-6> <http://example.com/p1> "V_1-6" .
<http://ex.com/table/V_1-6> <http://example.com/p2> "V_2-6" .
<http://ex.com/table/V_1-6> <http://example.com/p3> "V_3-6" .
<http://ex.com/table/V_1-6> <http://example.com/p4> "V_4-6" .
<http://ex.com/table/V_1-6> <http://example.com/p5> "V_5-6" .
<http://ex.com/table/V_1-7> <http://example.com/p1> "V_1-7" .
<http://ex.com/table/V_1-7> <http://example.com/p2> "V_2-7" .
<http://ex.com/table/V_1-7> <http://example.com/p3> "V_3-7" .
<http://ex.com/table/V_1-7> <http://example.com/p4> "V_4-7" .
<http://ex.com/table/V_1-7> <http://example.com/p5> "V_5-7" .
<http://ex.com/table/V_1-8> <http://example.com/p1> "V_1-8" .
<http://ex.com/table/V_1-8> <http://example.com/p2> "V_2-8" .
<http://ex.com/table/V_1-8> <http://example.com/p3> "V_3-8" .
<http://ex.com/table/V_1-8> <http://example.com/p4> "V_4-8" .
<http://ex.com/table/V_1-8> <http://example.com/p5> "V_5-8" .
<http://ex.com/table/V_1-9> <http://example.com/p1> "V_1-9" .
<http://ex.com/table/V_1-9> <http://example.com/p2> "V_2-9" .
<http://ex.com/table/V_1-9> <http://example.com/p3> "V_3-9" .
<http://ex.com/table/V_1-9> <http://example.com/p4> "V_4-9" .
<http://ex.com/table/V_1-9> <http://example.com/p5> "V_5-9" .
```

### 1 TM + 1 POM + 1 static GM

The more GMs, the more NGs are generated. If multiple NGs are specified,
RDF triples will be duplicated and added to all NGs.

#### Input data

```
id,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20
1,V_1-1,V_2-1,V_3-1,V_4-1,V_5-1,V_6-1,V_7-1,V_8-1,V_9-1,V_10-1,V_11-1,V_12-1,V_13-1,V_14-1,V_15-1,V_16-1,V_17-1,V_18-1,V_19-1,V_20-1
2,V_1-2,V_2-2,V_3-2,V_4-2,V_5-2,V_6-2,V_7-2,V_8-2,V_9-2,V_10-2,V_11-2,V_12-2,V_13-2,V_14-2,V_15-2,V_16-2,V_17-2,V_18-2,V_19-2,V_20-2
3,V_1-3,V_2-3,V_3-3,V_4-3,V_5-3,V_6-3,V_7-3,V_8-3,V_9-3,V_10-3,V_11-3,V_12-3,V_13-3,V_14-3,V_15-3,V_16-3,V_17-3,V_18-3,V_19-3,V_20-3
4,V_1-4,V_2-4,V_3-4,V_4-4,V_5-4,V_6-4,V_7-4,V_8-4,V_9-4,V_10-4,V_11-4,V_12-4,V_13-4,V_14-4,V_15-4,V_16-4,V_17-4,V_18-4,V_19-4,V_20-4
5,V_1-5,V_2-5,V_3-5,V_4-5,V_5-5,V_6-5,V_7-5,V_8-5,V_9-5,V_10-5,V_11-5,V_12-5,V_13-5,V_14-5,V_15-5,V_16-5,V_17-5,V_18-5,V_19-5,V_20-5
6,V_1-6,V_2-6,V_3-6,V_4-6,V_5-6,V_6-6,V_7-6,V_8-6,V_9-6,V_10-6,V_11-6,V_12-6,V_13-6,V_14-6,V_15-6,V_16-6,V_17-6,V_18-6,V_19-6,V_20-6
7,V_1-7,V_2-7,V_3-7,V_4-7,V_5-7,V_6-7,V_7-7,V_8-7,V_9-7,V_10-7,V_11-7,V_12-7,V_13-7,V_14-7,V_15-7,V_16-7,V_17-7,V_18-7,V_19-7,V_20-7
8,V_1-8,V_2-8,V_3-8,V_4-8,V_5-8,V_6-8,V_7-8,V_8-8,V_9-8,V_10-8,V_11-8,V_12-8,V_13-8,V_14-8,V_15-8,V_16-8,V_17-8,V_18-8,V_19-8,V_20-8
9,V_1-9,V_2-9,V_3-9,V_4-9,V_5-9,V_6-9,V_7-9,V_8-9,V_9-9,V_10-9,V_11-9,V_12-9,V_13-9,V_14-9,V_15-9,V_16-9,V_17-9,V_18-9,V_19-9,V_20-9
10,V_1-10,V_2-10,V_3-10,V_4-10,V_5-10,V_6-10,V_7-10,V_8-10,V_9-10,V_10-10,V_11-10,V_12-10,V_13-10,V_14-10,V_15-10,V_16-10,V_17-10,V_18-10,V_19-10,V_20-10
11,V_1-11,V_2-11,V_3-11,V_4-11,V_5-11,V_6-11,V_7-11,V_8-11,V_9-11,V_10-11,V_11-11,V_12-11,V_13-11,V_14-11,V_15-11,V_16-11,V_17-11,V_18-11,V_19-11,V_20-11
12,V_1-12,V_2-12,V_3-12,V_4-12,V_5-12,V_6-12,V_7-12,V_8-12,V_9-12,V_10-12,V_11-12,V_12-12,V_13-12,V_14-12,V_15-12,V_16-12,V_17-12,V_18-12,V_19-12,V_20-12
13,V_1-13,V_2-13,V_3-13,V_4-13,V_5-13,V_6-13,V_7-13,V_8-13,V_9-13,V_10-13,V_11-13,V_12-13,V_13-13,V_14-13,V_15-13,V_16-13,V_17-13,V_18-13,V_19-13,V_20-13
14,V_1-14,V_2-14,V_3-14,V_4-14,V_5-14,V_6-14,V_7-14,V_8-14,V_9-14,V_10-14,V_11-14,V_12-14,V_13-14,V_14-14,V_15-14,V_16-14,V_17-14,V_18-14,V_19-14,V_20-14
15,V_1-15,V_2-15,V_3-15,V_4-15,V_5-15,V_6-15,V_7-15,V_8-15,V_9-15,V_10-15,V_11-15,V_12-15,V_13-15,V_14-15,V_15-15,V_16-15,V_17-15,V_18-15,V_19-15,V_20-15
16,V_1-16,V_2-16,V_3-16,V_4-16,V_5-16,V_6-16,V_7-16,V_8-16,V_9-16,V_10-16,V_11-16,V_12-16,V_13-16,V_14-16,V_15-16,V_16-16,V_17-16,V_18-16,V_19-16,V_20-16
17,V_1-17,V_2-17,V_3-17,V_4-17,V_5-17,V_6-17,V_7-17,V_8-17,V_9-17,V_10-17,V_11-17,V_12-17,V_13-17,V_14-17,V_15-17,V_16-17,V_17-17,V_18-17,V_19-17,V_20-17
18,V_1-18,V_2-18,V_3-18,V_4-18,V_5-18,V_6-18,V_7-18,V_8-18,V_9-18,V_10-18,V_11-18,V_12-18,V_13-18,V_14-18,V_15-18,V_16-18,V_17-18,V_18-18,V_19-18,V_20-18
19,V_1-19,V_2-19,V_3-19,V_4-19,V_5-19,V_6-19,V_7-19,V_8-19,V_9-19,V_10-19,V_11-19,V_12-19,V_13-19,V_14-19,V_15-19,V_16-19,V_17-19,V_18-19,V_19-19,V_20-19
20,V_1-20,V_2-20,V_3-20,V_4-20,V_5-20,V_6-20,V_7-20,V_8-20,V_9-20,V_10-20,V_11-20,V_12-20,V_13-20,V_14-20,V_15-20,V_16-20,V_17-20,V_18-20,V_19-20,V_20-20
21,V_1-21,V_2-21,V_3-21,V_4-21,V_5-21,V_6-21,V_7-21,V_8-21,V_9-21,V_10-21,V_11-21,V_12-21,V_13-21,V_14-21,V_15-21,V_16-21,V_17-21,V_18-21,V_19-21,V_20-21
22,V_1-22,V_2-22,V_3-22,V_4-22,V_5-22,V_6-22,V_7-22,V_8-22,V_9-22,V_10-22,V_11-22,V_12-22,V_13-22,V_14-22,V_15-22,V_16-22,V_17-22,V_18-22,V_19-22,V_20-22
23,V_1-23,V_2-23,V_3-23,V_4-23,V_5-23,V_6-23,V_7-23,V_8-23,V_9-23,V_10-23,V_11-23,V_12-23,V_13-23,V_14-23,V_15-23,V_16-23,V_17-23,V_18-23,V_19-23,V_20-23
24,V_1-24,V_2-24,V_3-24,V_4-24,V_5-24,V_6-24,V_7-24,V_8-24,V_9-24,V_10-24,V_11-24,V_12-24,V_13-24,V_14-24,V_15-24,V_16-24,V_17-24,V_18-24,V_19-24,V_20-24
25,V_1-25,V_2-25,V_3-25,V_4-25,V_5-25,V_6-25,V_7-25,V_8-25,V_9-25,V_10-25,V_11-25,V_12-25,V_13-25,V_14-25,V_15-25,V_16-25,V_17-25,V_18-25,V_19-25,V_20-25
26,V_1-26,V_2-26,V_3-26,V_4-26,V_5-26,V_6-26,V_7-26,V_8-26,V_9-26,V_10-26,V_11-26,V_12-26,V_13-26,V_14-26,V_15-26,V_16-26,V_17-26,V_18-26,V_19-26,V_20-26
27,V_1-27,V_2-27,V_3-27,V_4-27,V_5-27,V_6-27,V_7-27,V_8-27,V_9-27,V_10-27,V_11-27,V_12-27,V_13-27,V_14-27,V_15-27,V_16-27,V_17-27,V_18-27,V_19-27,V_20-27
28,V_1-28,V_2-28,V_3-28,V_4-28,V_5-28,V_6-28,V_7-28,V_8-28,V_9-28,V_10-28,V_11-28,V_12-28,V_13-28,V_14-28,V_15-28,V_16-28,V_17-28,V_18-28,V_19-28,V_20-28
29,V_1-29,V_2-29,V_3-29,V_4-29,V_5-29,V_6-29,V_7-29,V_8-29,V_9-29,V_10-29,V_11-29,V_12-29,V_13-29,V_14-29,V_15-29,V_16-29,V_17-29,V_18-29,V_19-29,V_20-29
30,V_1-30,V_2-30,V_3-30,V_4-30,V_5-30,V_6-30,V_7-30,V_8-30,V_9-30,V_10-30,V_11-30,V_12-30,V_13-30,V_14-30,V_15-30,V_16-30,V_17-30,V_18-30,V_19-30,V_20-30
31,V_1-31,V_2-31,V_3-31,V_4-31,V_5-31,V_6-31,V_7-31,V_8-31,V_9-31,V_10-31,V_11-31,V_12-31,V_13-31,V_14-31,V_15-31,V_16-31,V_17-31,V_18-31,V_19-31,V_20-31
32,V_1-32,V_2-32,V_3-32,V_4-32,V_5-32,V_6-32,V_7-32,V_8-32,V_9-32,V_10-32,V_11-32,V_12-32,V_13-32,V_14-32,V_15-32,V_16-32,V_17-32,V_18-32,V_19-32,V_20-32
33,V_1-33,V_2-33,V_3-33,V_4-33,V_5-33,V_6-33,V_7-33,V_8-33,V_9-33,V_10-33,V_11-33,V_12-33,V_13-33,V_14-33,V_15-33,V_16-33,V_17-33,V_18-33,V_19-33,V_20-33
34,V_1-34,V_2-34,V_3-34,V_4-34,V_5-34,V_6-34,V_7-34,V_8-34,V_9-34,V_10-34,V_11-34,V_12-34,V_13-34,V_14-34,V_15-34,V_16-34,V_17-34,V_18-34,V_19-34,V_20-34
35,V_1-35,V_2-35,V_3-35,V_4-35,V_5-35,V_6-35,V_7-35,V_8-35,V_9-35,V_10-35,V_11-35,V_12-35,V_13-35,V_14-35,V_15-35,V_16-35,V_17-35,V_18-35,V_19-35,V_20-35
36,V_1-36,V_2-36,V_3-36,V_4-36,V_5-36,V_6-36,V_7-36,V_8-36,V_9-36,V_10-36,V_11-36,V_12-36,V_13-36,V_14-36,V_15-36,V_16-36,V_17-36,V_18-36,V_19-36,V_20-36
37,V_1-37,V_2-37,V_3-37,V_4-37,V_5-37,V_6-37,V_7-37,V_8-37,V_9-37,V_10-37,V_11-37,V_12-37,V_13-37,V_14-37,V_15-37,V_16-37,V_17-37,V_18-37,V_19-37,V_20-37
38,V_1-38,V_2-38,V_3-38,V_4-38,V_5-38,V_6-38,V_7-38,V_8-38,V_9-38,V_10-38,V_11-38,V_12-38,V_13-38,V_14-38,V_15-38,V_16-38,V_17-38,V_18-38,V_19-38,V_20-38
39,V_1-39,V_2-39,V_3-39,V_4-39,V_5-39,V_6-39,V_7-39,V_8-39,V_9-39,V_10-39,V_11-39,V_12-39,V_13-39,V_14-39,V_15-39,V_16-39,V_17-39,V_18-39,V_19-39,V_20-39
40,V_1-40,V_2-40,V_3-40,V_4-40,V_5-40,V_6-40,V_7-40,V_8-40,V_9-40,V_10-40,V_11-40,V_12-40,V_13-40,V_14-40,V_15-40,V_16-40,V_17-40,V_18-40,V_19-40,V_20-40
41,V_1-41,V_2-41,V_3-41,V_4-41,V_5-41,V_6-41,V_7-41,V_8-41,V_9-41,V_10-41,V_11-41,V_12-41,V_13-41,V_14-41,V_15-41,V_16-41,V_17-41,V_18-41,V_19-41,V_20-41
42,V_1-42,V_2-42,V_3-42,V_4-42,V_5-42,V_6-42,V_7-42,V_8-42,V_9-42,V_10-42,V_11-42,V_12-42,V_13-42,V_14-42,V_15-42,V_16-42,V_17-42,V_18-42,V_19-42,V_20-42
43,V_1-43,V_2-43,V_3-43,V_4-43,V_5-43,V_6-43,V_7-43,V_8-43,V_9-43,V_10-43,V_11-43,V_12-43,V_13-43,V_14-43,V_15-43,V_16-43,V_17-43,V_18-43,V_19-43,V_20-43
44,V_1-44,V_2-44,V_3-44,V_4-44,V_5-44,V_6-44,V_7-44,V_8-44,V_9-44,V_10-44,V_11-44,V_12-44,V_13-44,V_14-44,V_15-44,V_16-44,V_17-44,V_18-44,V_19-44,V_20-44
45,V_1-45,V_2-45,V_3-45,V_4-45,V_5-45,V_6-45,V_7-45,V_8-45,V_9-45,V_10-45,V_11-45,V_12-45,V_13-45,V_14-45,V_15-45,V_16-45,V_17-45,V_18-45,V_19-45,V_20-45
46,V_1-46,V_2-46,V_3-46,V_4-46,V_5-46,V_6-46,V_7-46,V_8-46,V_9-46,V_10-46,V_11-46,V_12-46,V_13-46,V_14-46,V_15-46,V_16-46,V_17-46,V_18-46,V_19-46,V_20-46
47,V_1-47,V_2-47,V_3-47,V_4-47,V_5-47,V_6-47,V_7-47,V_8-47,V_9-47,V_10-47,V_11-47,V_12-47,V_13-47,V_14-47,V_15-47,V_16-47,V_17-47,V_18-47,V_19-47,V_20-47
48,V_1-48,V_2-48,V_3-48,V_4-48,V_5-48,V_6-48,V_7-48,V_8-48,V_9-48,V_10-48,V_11-48,V_12-48,V_13-48,V_14-48,V_15-48,V_16-48,V_17-48,V_18-48,V_19-48,V_20-48
49,V_1-49,V_2-49,V_3-49,V_4-49,V_5-49,V_6-49,V_7-49,V_8-49,V_9-49,V_10-49,V_11-49,V_12-49,V_13-49,V_14-49,V_15-49,V_16-49,V_17-49,V_18-49,V_19-49,V_20-49
50,V_1-50,V_2-50,V_3-50,V_4-50,V_5-50,V_6-50,V_7-50,V_8-50,V_9-50,V_10-50,V_11-50,V_12-50,V_13-50,V_14-50,V_15-50,V_16-50,V_17-50,V_18-50,V_19-50,V_20-50
51,V_1-51,V_2-51,V_3-51,V_4-51,V_5-51,V_6-51,V_7-51,V_8-51,V_9-51,V_10-51,V_11-51,V_12-51,V_13-51,V_14-51,V_15-51,V_16-51,V_17-51,V_18-51,V_19-51,V_20-51
52,V_1-52,V_2-52,V_3-52,V_4-52,V_5-52,V_6-52,V_7-52,V_8-52,V_9-52,V_10-52,V_11-52,V_12-52,V_13-52,V_14-52,V_15-52,V_16-52,V_17-52,V_18-52,V_19-52,V_20-52
53,V_1-53,V_2-53,V_3-53,V_4-53,V_5-53,V_6-53,V_7-53,V_8-53,V_9-53,V_10-53,V_11-53,V_12-53,V_13-53,V_14-53,V_15-53,V_16-53,V_17-53,V_18-53,V_19-53,V_20-53
54,V_1-54,V_2-54,V_3-54,V_4-54,V_5-54,V_6-54,V_7-54,V_8-54,V_9-54,V_10-54,V_11-54,V_12-54,V_13-54,V_14-54,V_15-54,V_16-54,V_17-54,V_18-54,V_19-54,V_20-54
55,V_1-55,V_2-55,V_3-55,V_4-55,V_5-55,V_6-55,V_7-55,V_8-55,V_9-55,V_10-55,V_11-55,V_12-55,V_13-55,V_14-55,V_15-55,V_16-55,V_17-55,V_18-55,V_19-55,V_20-55
56,V_1-56,V_2-56,V_3-56,V_4-56,V_5-56,V_6-56,V_7-56,V_8-56,V_9-56,V_10-56,V_11-56,V_12-56,V_13-56,V_14-56,V_15-56,V_16-56,V_17-56,V_18-56,V_19-56,V_20-56
57,V_1-57,V_2-57,V_3-57,V_4-57,V_5-57,V_6-57,V_7-57,V_8-57,V_9-57,V_10-57,V_11-57,V_12-57,V_13-57,V_14-57,V_15-57,V_16-57,V_17-57,V_18-57,V_19-57,V_20-57
58,V_1-58,V_2-58,V_3-58,V_4-58,V_5-58,V_6-58,V_7-58,V_8-58,V_9-58,V_10-58,V_11-58,V_12-58,V_13-58,V_14-58,V_15-58,V_16-58,V_17-58,V_18-58,V_19-58,V_20-58
59,V_1-59,V_2-59,V_3-59,V_4-59,V_5-59,V_6-59,V_7-59,V_8-59,V_9-59,V_10-59,V_11-59,V_12-59,V_13-59,V_14-59,V_15-59,V_16-59,V_17-59,V_18-59,V_19-59,V_20-59
60,V_1-60,V_2-60,V_3-60,V_4-60,V_5-60,V_6-60,V_7-60,V_8-60,V_9-60,V_10-60,V_11-60,V_12-60,V_13-60,V_14-60,V_15-60,V_16-60,V_17-60,V_18-60,V_19-60,V_20-60
61,V_1-61,V_2-61,V_3-61,V_4-61,V_5-61,V_6-61,V_7-61,V_8-61,V_9-61,V_10-61,V_11-61,V_12-61,V_13-61,V_14-61,V_15-61,V_16-61,V_17-61,V_18-61,V_19-61,V_20-61
62,V_1-62,V_2-62,V_3-62,V_4-62,V_5-62,V_6-62,V_7-62,V_8-62,V_9-62,V_10-62,V_11-62,V_12-62,V_13-62,V_14-62,V_15-62,V_16-62,V_17-62,V_18-62,V_19-62,V_20-62
63,V_1-63,V_2-63,V_3-63,V_4-63,V_5-63,V_6-63,V_7-63,V_8-63,V_9-63,V_10-63,V_11-63,V_12-63,V_13-63,V_14-63,V_15-63,V_16-63,V_17-63,V_18-63,V_19-63,V_20-63
64,V_1-64,V_2-64,V_3-64,V_4-64,V_5-64,V_6-64,V_7-64,V_8-64,V_9-64,V_10-64,V_11-64,V_12-64,V_13-64,V_14-64,V_15-64,V_16-64,V_17-64,V_18-64,V_19-64,V_20-64
65,V_1-65,V_2-65,V_3-65,V_4-65,V_5-65,V_6-65,V_7-65,V_8-65,V_9-65,V_10-65,V_11-65,V_12-65,V_13-65,V_14-65,V_15-65,V_16-65,V_17-65,V_18-65,V_19-65,V_20-65
66,V_1-66,V_2-66,V_3-66,V_4-66,V_5-66,V_6-66,V_7-66,V_8-66,V_9-66,V_10-66,V_11-66,V_12-66,V_13-66,V_14-66,V_15-66,V_16-66,V_17-66,V_18-66,V_19-66,V_20-66
67,V_1-67,V_2-67,V_3-67,V_4-67,V_5-67,V_6-67,V_7-67,V_8-67,V_9-67,V_10-67,V_11-67,V_12-67,V_13-67,V_14-67,V_15-67,V_16-67,V_17-67,V_18-67,V_19-67,V_20-67
68,V_1-68,V_2-68,V_3-68,V_4-68,V_5-68,V_6-68,V_7-68,V_8-68,V_9-68,V_10-68,V_11-68,V_12-68,V_13-68,V_14-68,V_15-68,V_16-68,V_17-68,V_18-68,V_19-68,V_20-68
69,V_1-69,V_2-69,V_3-69,V_4-69,V_5-69,V_6-69,V_7-69,V_8-69,V_9-69,V_10-69,V_11-69,V_12-69,V_13-69,V_14-69,V_15-69,V_16-69,V_17-69,V_18-69,V_19-69,V_20-69
70,V_1-70,V_2-70,V_3-70,V_4-70,V_5-70,V_6-70,V_7-70,V_8-70,V_9-70,V_10-70,V_11-70,V_12-70,V_13-70,V_14-70,V_15-70,V_16-70,V_17-70,V_18-70,V_19-70,V_20-70
71,V_1-71,V_2-71,V_3-71,V_4-71,V_5-71,V_6-71,V_7-71,V_8-71,V_9-71,V_10-71,V_11-71,V_12-71,V_13-71,V_14-71,V_15-71,V_16-71,V_17-71,V_18-71,V_19-71,V_20-71
72,V_1-72,V_2-72,V_3-72,V_4-72,V_5-72,V_6-72,V_7-72,V_8-72,V_9-72,V_10-72,V_11-72,V_12-72,V_13-72,V_14-72,V_15-72,V_16-72,V_17-72,V_18-72,V_19-72,V_20-72
73,V_1-73,V_2-73,V_3-73,V_4-73,V_5-73,V_6-73,V_7-73,V_8-73,V_9-73,V_10-73,V_11-73,V_12-73,V_13-73,V_14-73,V_15-73,V_16-73,V_17-73,V_18-73,V_19-73,V_20-73
74,V_1-74,V_2-74,V_3-74,V_4-74,V_5-74,V_6-74,V_7-74,V_8-74,V_9-74,V_10-74,V_11-74,V_12-74,V_13-74,V_14-74,V_15-74,V_16-74,V_17-74,V_18-74,V_19-74,V_20-74
75,V_1-75,V_2-75,V_3-75,V_4-75,V_5-75,V_6-75,V_7-75,V_8-75,V_9-75,V_10-75,V_11-75,V_12-75,V_13-75,V_14-75,V_15-75,V_16-75,V_17-75,V_18-75,V_19-75,V_20-75
76,V_1-76,V_2-76,V_3-76,V_4-76,V_5-76,V_6-76,V_7-76,V_8-76,V_9-76,V_10-76,V_11-76,V_12-76,V_13-76,V_14-76,V_15-76,V_16-76,V_17-76,V_18-76,V_19-76,V_20-76
77,V_1-77,V_2-77,V_3-77,V_4-77,V_5-77,V_6-77,V_7-77,V_8-77,V_9-77,V_10-77,V_11-77,V_12-77,V_13-77,V_14-77,V_15-77,V_16-77,V_17-77,V_18-77,V_19-77,V_20-77
78,V_1-78,V_2-78,V_3-78,V_4-78,V_5-78,V_6-78,V_7-78,V_8-78,V_9-78,V_10-78,V_11-78,V_12-78,V_13-78,V_14-78,V_15-78,V_16-78,V_17-78,V_18-78,V_19-78,V_20-78
79,V_1-79,V_2-79,V_3-79,V_4-79,V_5-79,V_6-79,V_7-79,V_8-79,V_9-79,V_10-79,V_11-79,V_12-79,V_13-79,V_14-79,V_15-79,V_16-79,V_17-79,V_18-79,V_19-79,V_20-79
80,V_1-80,V_2-80,V_3-80,V_4-80,V_5-80,V_6-80,V_7-80,V_8-80,V_9-80,V_10-80,V_11-80,V_12-80,V_13-80,V_14-80,V_15-80,V_16-80,V_17-80,V_18-80,V_19-80,V_20-80
81,V_1-81,V_2-81,V_3-81,V_4-81,V_5-81,V_6-81,V_7-81,V_8-81,V_9-81,V_10-81,V_11-81,V_12-81,V_13-81,V_14-81,V_15-81,V_16-81,V_17-81,V_18-81,V_19-81,V_20-81
82,V_1-82,V_2-82,V_3-82,V_4-82,V_5-82,V_6-82,V_7-82,V_8-82,V_9-82,V_10-82,V_11-82,V_12-82,V_13-82,V_14-82,V_15-82,V_16-82,V_17-82,V_18-82,V_19-82,V_20-82
83,V_1-83,V_2-83,V_3-83,V_4-83,V_5-83,V_6-83,V_7-83,V_8-83,V_9-83,V_10-83,V_11-83,V_12-83,V_13-83,V_14-83,V_15-83,V_16-83,V_17-83,V_18-83,V_19-83,V_20-83
84,V_1-84,V_2-84,V_3-84,V_4-84,V_5-84,V_6-84,V_7-84,V_8-84,V_9-84,V_10-84,V_11-84,V_12-84,V_13-84,V_14-84,V_15-84,V_16-84,V_17-84,V_18-84,V_19-84,V_20-84
85,V_1-85,V_2-85,V_3-85,V_4-85,V_5-85,V_6-85,V_7-85,V_8-85,V_9-85,V_10-85,V_11-85,V_12-85,V_13-85,V_14-85,V_15-85,V_16-85,V_17-85,V_18-85,V_19-85,V_20-85
86,V_1-86,V_2-86,V_3-86,V_4-86,V_5-86,V_6-86,V_7-86,V_8-86,V_9-86,V_10-86,V_11-86,V_12-86,V_13-86,V_14-86,V_15-86,V_16-86,V_17-86,V_18-86,V_19-86,V_20-86
87,V_1-87,V_2-87,V_3-87,V_4-87,V_5-87,V_6-87,V_7-87,V_8-87,V_9-87,V_10-87,V_11-87,V_12-87,V_13-87,V_14-87,V_15-87,V_16-87,V_17-87,V_18-87,V_19-87,V_20-87
88,V_1-88,V_2-88,V_3-88,V_4-88,V_5-88,V_6-88,V_7-88,V_8-88,V_9-88,V_10-88,V_11-88,V_12-88,V_13-88,V_14-88,V_15-88,V_16-88,V_17-88,V_18-88,V_19-88,V_20-88
89,V_1-89,V_2-89,V_3-89,V_4-89,V_5-89,V_6-89,V_7-89,V_8-89,V_9-89,V_10-89,V_11-89,V_12-89,V_13-89,V_14-89,V_15-89,V_16-89,V_17-89,V_18-89,V_19-89,V_20-89
90,V_1-90,V_2-90,V_3-90,V_4-90,V_5-90,V_6-90,V_7-90,V_8-90,V_9-90,V_10-90,V_11-90,V_12-90,V_13-90,V_14-90,V_15-90,V_16-90,V_17-90,V_18-90,V_19-90,V_20-90
91,V_1-91,V_2-91,V_3-91,V_4-91,V_5-91,V_6-91,V_7-91,V_8-91,V_9-91,V_10-91,V_11-91,V_12-91,V_13-91,V_14-91,V_15-91,V_16-91,V_17-91,V_18-91,V_19-91,V_20-91
92,V_1-92,V_2-92,V_3-92,V_4-92,V_5-92,V_6-92,V_7-92,V_8-92,V_9-92,V_10-92,V_11-92,V_12-92,V_13-92,V_14-92,V_15-92,V_16-92,V_17-92,V_18-92,V_19-92,V_20-92
93,V_1-93,V_2-93,V_3-93,V_4-93,V_5-93,V_6-93,V_7-93,V_8-93,V_9-93,V_10-93,V_11-93,V_12-93,V_13-93,V_14-93,V_15-93,V_16-93,V_17-93,V_18-93,V_19-93,V_20-93
94,V_1-94,V_2-94,V_3-94,V_4-94,V_5-94,V_6-94,V_7-94,V_8-94,V_9-94,V_10-94,V_11-94,V_12-94,V_13-94,V_14-94,V_15-94,V_16-94,V_17-94,V_18-94,V_19-94,V_20-94
95,V_1-95,V_2-95,V_3-95,V_4-95,V_5-95,V_6-95,V_7-95,V_8-95,V_9-95,V_10-95,V_11-95,V_12-95,V_13-95,V_14-95,V_15-95,V_16-95,V_17-95,V_18-95,V_19-95,V_20-95
96,V_1-96,V_2-96,V_3-96,V_4-96,V_5-96,V_6-96,V_7-96,V_8-96,V_9-96,V_10-96,V_11-96,V_12-96,V_13-96,V_14-96,V_15-96,V_16-96,V_17-96,V_18-96,V_19-96,V_20-96
97,V_1-97,V_2-97,V_3-97,V_4-97,V_5-97,V_6-97,V_7-97,V_8-97,V_9-97,V_10-97,V_11-97,V_12-97,V_13-97,V_14-97,V_15-97,V_16-97,V_17-97,V_18-97,V_19-97,V_20-97
98,V_1-98,V_2-98,V_3-98,V_4-98,V_5-98,V_6-98,V_7-98,V_8-98,V_9-98,V_10-98,V_11-98,V_12-98,V_13-98,V_14-98,V_15-98,V_16-98,V_17-98,V_18-98,V_19-98,V_20-98
99,V_1-99,V_2-99,V_3-99,V_4-99,V_5-99,V_6-99,V_7-99,V_8-99,V_9-99,V_10-99,V_11-99,V_12-99,V_13-99,V_14-99,V_15-99,V_16-99,V_17-99,V_18-99,V_19-99,V_20-99
100,V_1-100,V_2-100,V_3-100,V_4-100,V_5-100,V_6-100,V_7-100,V_8-100,V_9-100,V_10-100,V_11-100,V_12-100,V_13-100,V_14-100,V_15-100,V_16-100,V_17-100,V_18-100,V_19-100,V_20-100
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
            rr:graph <http://example.org/graph1> ;
            rr:objectMap [ a rr:ObjectMap ;
                    rr:column "p1" ] ;
            rr:predicateMap [ a rr:PredicateMap ;
                    rr:constant ex:p1 ] ] ;
    rr:subjectMap [ rr:template "http://ex.com/table/{p1}" ] .
```

#### Output RDF

```
<http://ex.com/table/V_1-1> <http://example.com/p1> "V_1-1" <http://example.org/graph1>.
<http://ex.com/table/V_1-2> <http://example.com/p1> "V_1-2" <http://example.org/graph1>.
<http://ex.com/table/V_1-3> <http://example.com/p1> "V_1-3" <http://example.org/graph1>.
<http://ex.com/table/V_1-4> <http://example.com/p1> "V_1-4" <http://example.org/graph1>.
<http://ex.com/table/V_1-5> <http://example.com/p1> "V_1-5" <http://example.org/graph1>.
<http://ex.com/table/V_1-6> <http://example.com/p1> "V_1-6" <http://example.org/graph1>.
<http://ex.com/table/V_1-7> <http://example.com/p1> "V_1-7" <http://example.org/graph1>.
<http://ex.com/table/V_1-8> <http://example.com/p1> "V_1-8" <http://example.org/graph1>.
<http://ex.com/table/V_1-9> <http://example.com/p1> "V_1-9" <http://example.org/graph1>.
<http://ex.com/table/V_1-10> <http://example.com/p1> "V_1-10" <http://example.org/graph1>.
<http://ex.com/table/V_1-11> <http://example.com/p1> "V_1-11" <http://example.org/graph1>.
<http://ex.com/table/V_1-12> <http://example.com/p1> "V_1-12" <http://example.org/graph1>.
<http://ex.com/table/V_1-13> <http://example.com/p1> "V_1-13" <http://example.org/graph1>.
<http://ex.com/table/V_1-14> <http://example.com/p1> "V_1-14" <http://example.org/graph1>.
<http://ex.com/table/V_1-15> <http://example.com/p1> "V_1-15" <http://example.org/graph1>.
<http://ex.com/table/V_1-16> <http://example.com/p1> "V_1-16" <http://example.org/graph1>.
<http://ex.com/table/V_1-17> <http://example.com/p1> "V_1-17" <http://example.org/graph1>.
<http://ex.com/table/V_1-18> <http://example.com/p1> "V_1-18" <http://example.org/graph1>.
<http://ex.com/table/V_1-19> <http://example.com/p1> "V_1-19" <http://example.org/graph1>.
<http://ex.com/table/V_1-20> <http://example.com/p1> "V_1-20" <http://example.org/graph1>.
<http://ex.com/table/V_1-21> <http://example.com/p1> "V_1-21" <http://example.org/graph1>.
<http://ex.com/table/V_1-22> <http://example.com/p1> "V_1-22" <http://example.org/graph1>.
<http://ex.com/table/V_1-23> <http://example.com/p1> "V_1-23" <http://example.org/graph1>.
<http://ex.com/table/V_1-24> <http://example.com/p1> "V_1-24" <http://example.org/graph1>.
<http://ex.com/table/V_1-25> <http://example.com/p1> "V_1-25" <http://example.org/graph1>.
<http://ex.com/table/V_1-26> <http://example.com/p1> "V_1-26" <http://example.org/graph1>.
<http://ex.com/table/V_1-27> <http://example.com/p1> "V_1-27" <http://example.org/graph1>.
<http://ex.com/table/V_1-28> <http://example.com/p1> "V_1-28" <http://example.org/graph1>.
<http://ex.com/table/V_1-29> <http://example.com/p1> "V_1-29" <http://example.org/graph1>.
<http://ex.com/table/V_1-30> <http://example.com/p1> "V_1-30" <http://example.org/graph1>.
<http://ex.com/table/V_1-31> <http://example.com/p1> "V_1-31" <http://example.org/graph1>.
<http://ex.com/table/V_1-32> <http://example.com/p1> "V_1-32" <http://example.org/graph1>.
<http://ex.com/table/V_1-33> <http://example.com/p1> "V_1-33" <http://example.org/graph1>.
<http://ex.com/table/V_1-34> <http://example.com/p1> "V_1-34" <http://example.org/graph1>.
<http://ex.com/table/V_1-35> <http://example.com/p1> "V_1-35" <http://example.org/graph1>.
<http://ex.com/table/V_1-36> <http://example.com/p1> "V_1-36" <http://example.org/graph1>.
<http://ex.com/table/V_1-37> <http://example.com/p1> "V_1-37" <http://example.org/graph1>.
<http://ex.com/table/V_1-38> <http://example.com/p1> "V_1-38" <http://example.org/graph1>.
<http://ex.com/table/V_1-39> <http://example.com/p1> "V_1-39" <http://example.org/graph1>.
<http://ex.com/table/V_1-40> <http://example.com/p1> "V_1-40" <http://example.org/graph1>.
<http://ex.com/table/V_1-41> <http://example.com/p1> "V_1-41" <http://example.org/graph1>.
<http://ex.com/table/V_1-42> <http://example.com/p1> "V_1-42" <http://example.org/graph1>.
<http://ex.com/table/V_1-43> <http://example.com/p1> "V_1-43" <http://example.org/graph1>.
<http://ex.com/table/V_1-44> <http://example.com/p1> "V_1-44" <http://example.org/graph1>.
<http://ex.com/table/V_1-45> <http://example.com/p1> "V_1-45" <http://example.org/graph1>.
<http://ex.com/table/V_1-46> <http://example.com/p1> "V_1-46" <http://example.org/graph1>.
<http://ex.com/table/V_1-47> <http://example.com/p1> "V_1-47" <http://example.org/graph1>.
<http://ex.com/table/V_1-48> <http://example.com/p1> "V_1-48" <http://example.org/graph1>.
<http://ex.com/table/V_1-49> <http://example.com/p1> "V_1-49" <http://example.org/graph1>.
<http://ex.com/table/V_1-50> <http://example.com/p1> "V_1-50" <http://example.org/graph1>.
<http://ex.com/table/V_1-51> <http://example.com/p1> "V_1-51" <http://example.org/graph1>.
<http://ex.com/table/V_1-52> <http://example.com/p1> "V_1-52" <http://example.org/graph1>.
<http://ex.com/table/V_1-53> <http://example.com/p1> "V_1-53" <http://example.org/graph1>.
<http://ex.com/table/V_1-54> <http://example.com/p1> "V_1-54" <http://example.org/graph1>.
<http://ex.com/table/V_1-55> <http://example.com/p1> "V_1-55" <http://example.org/graph1>.
<http://ex.com/table/V_1-56> <http://example.com/p1> "V_1-56" <http://example.org/graph1>.
<http://ex.com/table/V_1-57> <http://example.com/p1> "V_1-57" <http://example.org/graph1>.
<http://ex.com/table/V_1-58> <http://example.com/p1> "V_1-58" <http://example.org/graph1>.
<http://ex.com/table/V_1-59> <http://example.com/p1> "V_1-59" <http://example.org/graph1>.
<http://ex.com/table/V_1-60> <http://example.com/p1> "V_1-60" <http://example.org/graph1>.
<http://ex.com/table/V_1-61> <http://example.com/p1> "V_1-61" <http://example.org/graph1>.
<http://ex.com/table/V_1-62> <http://example.com/p1> "V_1-62" <http://example.org/graph1>.
<http://ex.com/table/V_1-63> <http://example.com/p1> "V_1-63" <http://example.org/graph1>.
<http://ex.com/table/V_1-64> <http://example.com/p1> "V_1-64" <http://example.org/graph1>.
<http://ex.com/table/V_1-65> <http://example.com/p1> "V_1-65" <http://example.org/graph1>.
<http://ex.com/table/V_1-66> <http://example.com/p1> "V_1-66" <http://example.org/graph1>.
<http://ex.com/table/V_1-67> <http://example.com/p1> "V_1-67" <http://example.org/graph1>.
<http://ex.com/table/V_1-68> <http://example.com/p1> "V_1-68" <http://example.org/graph1>.
<http://ex.com/table/V_1-69> <http://example.com/p1> "V_1-69" <http://example.org/graph1>.
<http://ex.com/table/V_1-70> <http://example.com/p1> "V_1-70" <http://example.org/graph1>.
<http://ex.com/table/V_1-71> <http://example.com/p1> "V_1-71" <http://example.org/graph1>.
<http://ex.com/table/V_1-72> <http://example.com/p1> "V_1-72" <http://example.org/graph1>.
<http://ex.com/table/V_1-73> <http://example.com/p1> "V_1-73" <http://example.org/graph1>.
<http://ex.com/table/V_1-74> <http://example.com/p1> "V_1-74" <http://example.org/graph1>.
<http://ex.com/table/V_1-75> <http://example.com/p1> "V_1-75" <http://example.org/graph1>.
<http://ex.com/table/V_1-76> <http://example.com/p1> "V_1-76" <http://example.org/graph1>.
<http://ex.com/table/V_1-77> <http://example.com/p1> "V_1-77" <http://example.org/graph1>.
<http://ex.com/table/V_1-78> <http://example.com/p1> "V_1-78" <http://example.org/graph1>.
<http://ex.com/table/V_1-79> <http://example.com/p1> "V_1-79" <http://example.org/graph1>.
<http://ex.com/table/V_1-80> <http://example.com/p1> "V_1-80" <http://example.org/graph1>.
<http://ex.com/table/V_1-81> <http://example.com/p1> "V_1-81" <http://example.org/graph1>.
<http://ex.com/table/V_1-82> <http://example.com/p1> "V_1-82" <http://example.org/graph1>.
<http://ex.com/table/V_1-83> <http://example.com/p1> "V_1-83" <http://example.org/graph1>.
<http://ex.com/table/V_1-84> <http://example.com/p1> "V_1-84" <http://example.org/graph1>.
<http://ex.com/table/V_1-85> <http://example.com/p1> "V_1-85" <http://example.org/graph1>.
<http://ex.com/table/V_1-86> <http://example.com/p1> "V_1-86" <http://example.org/graph1>.
<http://ex.com/table/V_1-87> <http://example.com/p1> "V_1-87" <http://example.org/graph1>.
<http://ex.com/table/V_1-88> <http://example.com/p1> "V_1-88" <http://example.org/graph1>.
<http://ex.com/table/V_1-89> <http://example.com/p1> "V_1-89" <http://example.org/graph1>.
<http://ex.com/table/V_1-90> <http://example.com/p1> "V_1-90" <http://example.org/graph1>.
<http://ex.com/table/V_1-91> <http://example.com/p1> "V_1-91" <http://example.org/graph1>.
<http://ex.com/table/V_1-92> <http://example.com/p1> "V_1-92" <http://example.org/graph1>.
<http://ex.com/table/V_1-93> <http://example.com/p1> "V_1-93" <http://example.org/graph1>.
<http://ex.com/table/V_1-94> <http://example.com/p1> "V_1-94" <http://example.org/graph1>.
<http://ex.com/table/V_1-95> <http://example.com/p1> "V_1-95" <http://example.org/graph1>.
<http://ex.com/table/V_1-96> <http://example.com/p1> "V_1-96" <http://example.org/graph1>.
<http://ex.com/table/V_1-97> <http://example.com/p1> "V_1-97" <http://example.org/graph1>.
<http://ex.com/table/V_1-98> <http://example.com/p1> "V_1-98" <http://example.org/graph1>.
<http://ex.com/table/V_1-99> <http://example.com/p1> "V_1-99" <http://example.org/graph1>.
<http://ex.com/table/V_1-100> <http://example.com/p1> "V_1-100" <http://example.org/graph1>.
```

### 1 TM + 1 POM + 1 dynamic GM

The more GMs, the more NGs are generated. If multiple NGs are specified,
RDF triples will be duplicated and added to all NGs.

#### Input data

```
id,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20
1,V_1-1,V_2-1,V_3-1,V_4-1,V_5-1,V_6-1,V_7-1,V_8-1,V_9-1,V_10-1,V_11-1,V_12-1,V_13-1,V_14-1,V_15-1,V_16-1,V_17-1,V_18-1,V_19-1,V_20-1
2,V_1-2,V_2-2,V_3-2,V_4-2,V_5-2,V_6-2,V_7-2,V_8-2,V_9-2,V_10-2,V_11-2,V_12-2,V_13-2,V_14-2,V_15-2,V_16-2,V_17-2,V_18-2,V_19-2,V_20-2
3,V_1-3,V_2-3,V_3-3,V_4-3,V_5-3,V_6-3,V_7-3,V_8-3,V_9-3,V_10-3,V_11-3,V_12-3,V_13-3,V_14-3,V_15-3,V_16-3,V_17-3,V_18-3,V_19-3,V_20-3
4,V_1-4,V_2-4,V_3-4,V_4-4,V_5-4,V_6-4,V_7-4,V_8-4,V_9-4,V_10-4,V_11-4,V_12-4,V_13-4,V_14-4,V_15-4,V_16-4,V_17-4,V_18-4,V_19-4,V_20-4
5,V_1-5,V_2-5,V_3-5,V_4-5,V_5-5,V_6-5,V_7-5,V_8-5,V_9-5,V_10-5,V_11-5,V_12-5,V_13-5,V_14-5,V_15-5,V_16-5,V_17-5,V_18-5,V_19-5,V_20-5
6,V_1-6,V_2-6,V_3-6,V_4-6,V_5-6,V_6-6,V_7-6,V_8-6,V_9-6,V_10-6,V_11-6,V_12-6,V_13-6,V_14-6,V_15-6,V_16-6,V_17-6,V_18-6,V_19-6,V_20-6
7,V_1-7,V_2-7,V_3-7,V_4-7,V_5-7,V_6-7,V_7-7,V_8-7,V_9-7,V_10-7,V_11-7,V_12-7,V_13-7,V_14-7,V_15-7,V_16-7,V_17-7,V_18-7,V_19-7,V_20-7
8,V_1-8,V_2-8,V_3-8,V_4-8,V_5-8,V_6-8,V_7-8,V_8-8,V_9-8,V_10-8,V_11-8,V_12-8,V_13-8,V_14-8,V_15-8,V_16-8,V_17-8,V_18-8,V_19-8,V_20-8
9,V_1-9,V_2-9,V_3-9,V_4-9,V_5-9,V_6-9,V_7-9,V_8-9,V_9-9,V_10-9,V_11-9,V_12-9,V_13-9,V_14-9,V_15-9,V_16-9,V_17-9,V_18-9,V_19-9,V_20-9
10,V_1-10,V_2-10,V_3-10,V_4-10,V_5-10,V_6-10,V_7-10,V_8-10,V_9-10,V_10-10,V_11-10,V_12-10,V_13-10,V_14-10,V_15-10,V_16-10,V_17-10,V_18-10,V_19-10,V_20-10
11,V_1-11,V_2-11,V_3-11,V_4-11,V_5-11,V_6-11,V_7-11,V_8-11,V_9-11,V_10-11,V_11-11,V_12-11,V_13-11,V_14-11,V_15-11,V_16-11,V_17-11,V_18-11,V_19-11,V_20-11
12,V_1-12,V_2-12,V_3-12,V_4-12,V_5-12,V_6-12,V_7-12,V_8-12,V_9-12,V_10-12,V_11-12,V_12-12,V_13-12,V_14-12,V_15-12,V_16-12,V_17-12,V_18-12,V_19-12,V_20-12
13,V_1-13,V_2-13,V_3-13,V_4-13,V_5-13,V_6-13,V_7-13,V_8-13,V_9-13,V_10-13,V_11-13,V_12-13,V_13-13,V_14-13,V_15-13,V_16-13,V_17-13,V_18-13,V_19-13,V_20-13
14,V_1-14,V_2-14,V_3-14,V_4-14,V_5-14,V_6-14,V_7-14,V_8-14,V_9-14,V_10-14,V_11-14,V_12-14,V_13-14,V_14-14,V_15-14,V_16-14,V_17-14,V_18-14,V_19-14,V_20-14
15,V_1-15,V_2-15,V_3-15,V_4-15,V_5-15,V_6-15,V_7-15,V_8-15,V_9-15,V_10-15,V_11-15,V_12-15,V_13-15,V_14-15,V_15-15,V_16-15,V_17-15,V_18-15,V_19-15,V_20-15
16,V_1-16,V_2-16,V_3-16,V_4-16,V_5-16,V_6-16,V_7-16,V_8-16,V_9-16,V_10-16,V_11-16,V_12-16,V_13-16,V_14-16,V_15-16,V_16-16,V_17-16,V_18-16,V_19-16,V_20-16
17,V_1-17,V_2-17,V_3-17,V_4-17,V_5-17,V_6-17,V_7-17,V_8-17,V_9-17,V_10-17,V_11-17,V_12-17,V_13-17,V_14-17,V_15-17,V_16-17,V_17-17,V_18-17,V_19-17,V_20-17
18,V_1-18,V_2-18,V_3-18,V_4-18,V_5-18,V_6-18,V_7-18,V_8-18,V_9-18,V_10-18,V_11-18,V_12-18,V_13-18,V_14-18,V_15-18,V_16-18,V_17-18,V_18-18,V_19-18,V_20-18
19,V_1-19,V_2-19,V_3-19,V_4-19,V_5-19,V_6-19,V_7-19,V_8-19,V_9-19,V_10-19,V_11-19,V_12-19,V_13-19,V_14-19,V_15-19,V_16-19,V_17-19,V_18-19,V_19-19,V_20-19
20,V_1-20,V_2-20,V_3-20,V_4-20,V_5-20,V_6-20,V_7-20,V_8-20,V_9-20,V_10-20,V_11-20,V_12-20,V_13-20,V_14-20,V_15-20,V_16-20,V_17-20,V_18-20,V_19-20,V_20-20
21,V_1-21,V_2-21,V_3-21,V_4-21,V_5-21,V_6-21,V_7-21,V_8-21,V_9-21,V_10-21,V_11-21,V_12-21,V_13-21,V_14-21,V_15-21,V_16-21,V_17-21,V_18-21,V_19-21,V_20-21
22,V_1-22,V_2-22,V_3-22,V_4-22,V_5-22,V_6-22,V_7-22,V_8-22,V_9-22,V_10-22,V_11-22,V_12-22,V_13-22,V_14-22,V_15-22,V_16-22,V_17-22,V_18-22,V_19-22,V_20-22
23,V_1-23,V_2-23,V_3-23,V_4-23,V_5-23,V_6-23,V_7-23,V_8-23,V_9-23,V_10-23,V_11-23,V_12-23,V_13-23,V_14-23,V_15-23,V_16-23,V_17-23,V_18-23,V_19-23,V_20-23
24,V_1-24,V_2-24,V_3-24,V_4-24,V_5-24,V_6-24,V_7-24,V_8-24,V_9-24,V_10-24,V_11-24,V_12-24,V_13-24,V_14-24,V_15-24,V_16-24,V_17-24,V_18-24,V_19-24,V_20-24
25,V_1-25,V_2-25,V_3-25,V_4-25,V_5-25,V_6-25,V_7-25,V_8-25,V_9-25,V_10-25,V_11-25,V_12-25,V_13-25,V_14-25,V_15-25,V_16-25,V_17-25,V_18-25,V_19-25,V_20-25
26,V_1-26,V_2-26,V_3-26,V_4-26,V_5-26,V_6-26,V_7-26,V_8-26,V_9-26,V_10-26,V_11-26,V_12-26,V_13-26,V_14-26,V_15-26,V_16-26,V_17-26,V_18-26,V_19-26,V_20-26
27,V_1-27,V_2-27,V_3-27,V_4-27,V_5-27,V_6-27,V_7-27,V_8-27,V_9-27,V_10-27,V_11-27,V_12-27,V_13-27,V_14-27,V_15-27,V_16-27,V_17-27,V_18-27,V_19-27,V_20-27
28,V_1-28,V_2-28,V_3-28,V_4-28,V_5-28,V_6-28,V_7-28,V_8-28,V_9-28,V_10-28,V_11-28,V_12-28,V_13-28,V_14-28,V_15-28,V_16-28,V_17-28,V_18-28,V_19-28,V_20-28
29,V_1-29,V_2-29,V_3-29,V_4-29,V_5-29,V_6-29,V_7-29,V_8-29,V_9-29,V_10-29,V_11-29,V_12-29,V_13-29,V_14-29,V_15-29,V_16-29,V_17-29,V_18-29,V_19-29,V_20-29
30,V_1-30,V_2-30,V_3-30,V_4-30,V_5-30,V_6-30,V_7-30,V_8-30,V_9-30,V_10-30,V_11-30,V_12-30,V_13-30,V_14-30,V_15-30,V_16-30,V_17-30,V_18-30,V_19-30,V_20-30
31,V_1-31,V_2-31,V_3-31,V_4-31,V_5-31,V_6-31,V_7-31,V_8-31,V_9-31,V_10-31,V_11-31,V_12-31,V_13-31,V_14-31,V_15-31,V_16-31,V_17-31,V_18-31,V_19-31,V_20-31
32,V_1-32,V_2-32,V_3-32,V_4-32,V_5-32,V_6-32,V_7-32,V_8-32,V_9-32,V_10-32,V_11-32,V_12-32,V_13-32,V_14-32,V_15-32,V_16-32,V_17-32,V_18-32,V_19-32,V_20-32
33,V_1-33,V_2-33,V_3-33,V_4-33,V_5-33,V_6-33,V_7-33,V_8-33,V_9-33,V_10-33,V_11-33,V_12-33,V_13-33,V_14-33,V_15-33,V_16-33,V_17-33,V_18-33,V_19-33,V_20-33
34,V_1-34,V_2-34,V_3-34,V_4-34,V_5-34,V_6-34,V_7-34,V_8-34,V_9-34,V_10-34,V_11-34,V_12-34,V_13-34,V_14-34,V_15-34,V_16-34,V_17-34,V_18-34,V_19-34,V_20-34
35,V_1-35,V_2-35,V_3-35,V_4-35,V_5-35,V_6-35,V_7-35,V_8-35,V_9-35,V_10-35,V_11-35,V_12-35,V_13-35,V_14-35,V_15-35,V_16-35,V_17-35,V_18-35,V_19-35,V_20-35
36,V_1-36,V_2-36,V_3-36,V_4-36,V_5-36,V_6-36,V_7-36,V_8-36,V_9-36,V_10-36,V_11-36,V_12-36,V_13-36,V_14-36,V_15-36,V_16-36,V_17-36,V_18-36,V_19-36,V_20-36
37,V_1-37,V_2-37,V_3-37,V_4-37,V_5-37,V_6-37,V_7-37,V_8-37,V_9-37,V_10-37,V_11-37,V_12-37,V_13-37,V_14-37,V_15-37,V_16-37,V_17-37,V_18-37,V_19-37,V_20-37
38,V_1-38,V_2-38,V_3-38,V_4-38,V_5-38,V_6-38,V_7-38,V_8-38,V_9-38,V_10-38,V_11-38,V_12-38,V_13-38,V_14-38,V_15-38,V_16-38,V_17-38,V_18-38,V_19-38,V_20-38
39,V_1-39,V_2-39,V_3-39,V_4-39,V_5-39,V_6-39,V_7-39,V_8-39,V_9-39,V_10-39,V_11-39,V_12-39,V_13-39,V_14-39,V_15-39,V_16-39,V_17-39,V_18-39,V_19-39,V_20-39
40,V_1-40,V_2-40,V_3-40,V_4-40,V_5-40,V_6-40,V_7-40,V_8-40,V_9-40,V_10-40,V_11-40,V_12-40,V_13-40,V_14-40,V_15-40,V_16-40,V_17-40,V_18-40,V_19-40,V_20-40
41,V_1-41,V_2-41,V_3-41,V_4-41,V_5-41,V_6-41,V_7-41,V_8-41,V_9-41,V_10-41,V_11-41,V_12-41,V_13-41,V_14-41,V_15-41,V_16-41,V_17-41,V_18-41,V_19-41,V_20-41
42,V_1-42,V_2-42,V_3-42,V_4-42,V_5-42,V_6-42,V_7-42,V_8-42,V_9-42,V_10-42,V_11-42,V_12-42,V_13-42,V_14-42,V_15-42,V_16-42,V_17-42,V_18-42,V_19-42,V_20-42
43,V_1-43,V_2-43,V_3-43,V_4-43,V_5-43,V_6-43,V_7-43,V_8-43,V_9-43,V_10-43,V_11-43,V_12-43,V_13-43,V_14-43,V_15-43,V_16-43,V_17-43,V_18-43,V_19-43,V_20-43
44,V_1-44,V_2-44,V_3-44,V_4-44,V_5-44,V_6-44,V_7-44,V_8-44,V_9-44,V_10-44,V_11-44,V_12-44,V_13-44,V_14-44,V_15-44,V_16-44,V_17-44,V_18-44,V_19-44,V_20-44
45,V_1-45,V_2-45,V_3-45,V_4-45,V_5-45,V_6-45,V_7-45,V_8-45,V_9-45,V_10-45,V_11-45,V_12-45,V_13-45,V_14-45,V_15-45,V_16-45,V_17-45,V_18-45,V_19-45,V_20-45
46,V_1-46,V_2-46,V_3-46,V_4-46,V_5-46,V_6-46,V_7-46,V_8-46,V_9-46,V_10-46,V_11-46,V_12-46,V_13-46,V_14-46,V_15-46,V_16-46,V_17-46,V_18-46,V_19-46,V_20-46
47,V_1-47,V_2-47,V_3-47,V_4-47,V_5-47,V_6-47,V_7-47,V_8-47,V_9-47,V_10-47,V_11-47,V_12-47,V_13-47,V_14-47,V_15-47,V_16-47,V_17-47,V_18-47,V_19-47,V_20-47
48,V_1-48,V_2-48,V_3-48,V_4-48,V_5-48,V_6-48,V_7-48,V_8-48,V_9-48,V_10-48,V_11-48,V_12-48,V_13-48,V_14-48,V_15-48,V_16-48,V_17-48,V_18-48,V_19-48,V_20-48
49,V_1-49,V_2-49,V_3-49,V_4-49,V_5-49,V_6-49,V_7-49,V_8-49,V_9-49,V_10-49,V_11-49,V_12-49,V_13-49,V_14-49,V_15-49,V_16-49,V_17-49,V_18-49,V_19-49,V_20-49
50,V_1-50,V_2-50,V_3-50,V_4-50,V_5-50,V_6-50,V_7-50,V_8-50,V_9-50,V_10-50,V_11-50,V_12-50,V_13-50,V_14-50,V_15-50,V_16-50,V_17-50,V_18-50,V_19-50,V_20-50
51,V_1-51,V_2-51,V_3-51,V_4-51,V_5-51,V_6-51,V_7-51,V_8-51,V_9-51,V_10-51,V_11-51,V_12-51,V_13-51,V_14-51,V_15-51,V_16-51,V_17-51,V_18-51,V_19-51,V_20-51
52,V_1-52,V_2-52,V_3-52,V_4-52,V_5-52,V_6-52,V_7-52,V_8-52,V_9-52,V_10-52,V_11-52,V_12-52,V_13-52,V_14-52,V_15-52,V_16-52,V_17-52,V_18-52,V_19-52,V_20-52
53,V_1-53,V_2-53,V_3-53,V_4-53,V_5-53,V_6-53,V_7-53,V_8-53,V_9-53,V_10-53,V_11-53,V_12-53,V_13-53,V_14-53,V_15-53,V_16-53,V_17-53,V_18-53,V_19-53,V_20-53
54,V_1-54,V_2-54,V_3-54,V_4-54,V_5-54,V_6-54,V_7-54,V_8-54,V_9-54,V_10-54,V_11-54,V_12-54,V_13-54,V_14-54,V_15-54,V_16-54,V_17-54,V_18-54,V_19-54,V_20-54
55,V_1-55,V_2-55,V_3-55,V_4-55,V_5-55,V_6-55,V_7-55,V_8-55,V_9-55,V_10-55,V_11-55,V_12-55,V_13-55,V_14-55,V_15-55,V_16-55,V_17-55,V_18-55,V_19-55,V_20-55
56,V_1-56,V_2-56,V_3-56,V_4-56,V_5-56,V_6-56,V_7-56,V_8-56,V_9-56,V_10-56,V_11-56,V_12-56,V_13-56,V_14-56,V_15-56,V_16-56,V_17-56,V_18-56,V_19-56,V_20-56
57,V_1-57,V_2-57,V_3-57,V_4-57,V_5-57,V_6-57,V_7-57,V_8-57,V_9-57,V_10-57,V_11-57,V_12-57,V_13-57,V_14-57,V_15-57,V_16-57,V_17-57,V_18-57,V_19-57,V_20-57
58,V_1-58,V_2-58,V_3-58,V_4-58,V_5-58,V_6-58,V_7-58,V_8-58,V_9-58,V_10-58,V_11-58,V_12-58,V_13-58,V_14-58,V_15-58,V_16-58,V_17-58,V_18-58,V_19-58,V_20-58
59,V_1-59,V_2-59,V_3-59,V_4-59,V_5-59,V_6-59,V_7-59,V_8-59,V_9-59,V_10-59,V_11-59,V_12-59,V_13-59,V_14-59,V_15-59,V_16-59,V_17-59,V_18-59,V_19-59,V_20-59
60,V_1-60,V_2-60,V_3-60,V_4-60,V_5-60,V_6-60,V_7-60,V_8-60,V_9-60,V_10-60,V_11-60,V_12-60,V_13-60,V_14-60,V_15-60,V_16-60,V_17-60,V_18-60,V_19-60,V_20-60
61,V_1-61,V_2-61,V_3-61,V_4-61,V_5-61,V_6-61,V_7-61,V_8-61,V_9-61,V_10-61,V_11-61,V_12-61,V_13-61,V_14-61,V_15-61,V_16-61,V_17-61,V_18-61,V_19-61,V_20-61
62,V_1-62,V_2-62,V_3-62,V_4-62,V_5-62,V_6-62,V_7-62,V_8-62,V_9-62,V_10-62,V_11-62,V_12-62,V_13-62,V_14-62,V_15-62,V_16-62,V_17-62,V_18-62,V_19-62,V_20-62
63,V_1-63,V_2-63,V_3-63,V_4-63,V_5-63,V_6-63,V_7-63,V_8-63,V_9-63,V_10-63,V_11-63,V_12-63,V_13-63,V_14-63,V_15-63,V_16-63,V_17-63,V_18-63,V_19-63,V_20-63
64,V_1-64,V_2-64,V_3-64,V_4-64,V_5-64,V_6-64,V_7-64,V_8-64,V_9-64,V_10-64,V_11-64,V_12-64,V_13-64,V_14-64,V_15-64,V_16-64,V_17-64,V_18-64,V_19-64,V_20-64
65,V_1-65,V_2-65,V_3-65,V_4-65,V_5-65,V_6-65,V_7-65,V_8-65,V_9-65,V_10-65,V_11-65,V_12-65,V_13-65,V_14-65,V_15-65,V_16-65,V_17-65,V_18-65,V_19-65,V_20-65
66,V_1-66,V_2-66,V_3-66,V_4-66,V_5-66,V_6-66,V_7-66,V_8-66,V_9-66,V_10-66,V_11-66,V_12-66,V_13-66,V_14-66,V_15-66,V_16-66,V_17-66,V_18-66,V_19-66,V_20-66
67,V_1-67,V_2-67,V_3-67,V_4-67,V_5-67,V_6-67,V_7-67,V_8-67,V_9-67,V_10-67,V_11-67,V_12-67,V_13-67,V_14-67,V_15-67,V_16-67,V_17-67,V_18-67,V_19-67,V_20-67
68,V_1-68,V_2-68,V_3-68,V_4-68,V_5-68,V_6-68,V_7-68,V_8-68,V_9-68,V_10-68,V_11-68,V_12-68,V_13-68,V_14-68,V_15-68,V_16-68,V_17-68,V_18-68,V_19-68,V_20-68
69,V_1-69,V_2-69,V_3-69,V_4-69,V_5-69,V_6-69,V_7-69,V_8-69,V_9-69,V_10-69,V_11-69,V_12-69,V_13-69,V_14-69,V_15-69,V_16-69,V_17-69,V_18-69,V_19-69,V_20-69
70,V_1-70,V_2-70,V_3-70,V_4-70,V_5-70,V_6-70,V_7-70,V_8-70,V_9-70,V_10-70,V_11-70,V_12-70,V_13-70,V_14-70,V_15-70,V_16-70,V_17-70,V_18-70,V_19-70,V_20-70
71,V_1-71,V_2-71,V_3-71,V_4-71,V_5-71,V_6-71,V_7-71,V_8-71,V_9-71,V_10-71,V_11-71,V_12-71,V_13-71,V_14-71,V_15-71,V_16-71,V_17-71,V_18-71,V_19-71,V_20-71
72,V_1-72,V_2-72,V_3-72,V_4-72,V_5-72,V_6-72,V_7-72,V_8-72,V_9-72,V_10-72,V_11-72,V_12-72,V_13-72,V_14-72,V_15-72,V_16-72,V_17-72,V_18-72,V_19-72,V_20-72
73,V_1-73,V_2-73,V_3-73,V_4-73,V_5-73,V_6-73,V_7-73,V_8-73,V_9-73,V_10-73,V_11-73,V_12-73,V_13-73,V_14-73,V_15-73,V_16-73,V_17-73,V_18-73,V_19-73,V_20-73
74,V_1-74,V_2-74,V_3-74,V_4-74,V_5-74,V_6-74,V_7-74,V_8-74,V_9-74,V_10-74,V_11-74,V_12-74,V_13-74,V_14-74,V_15-74,V_16-74,V_17-74,V_18-74,V_19-74,V_20-74
75,V_1-75,V_2-75,V_3-75,V_4-75,V_5-75,V_6-75,V_7-75,V_8-75,V_9-75,V_10-75,V_11-75,V_12-75,V_13-75,V_14-75,V_15-75,V_16-75,V_17-75,V_18-75,V_19-75,V_20-75
76,V_1-76,V_2-76,V_3-76,V_4-76,V_5-76,V_6-76,V_7-76,V_8-76,V_9-76,V_10-76,V_11-76,V_12-76,V_13-76,V_14-76,V_15-76,V_16-76,V_17-76,V_18-76,V_19-76,V_20-76
77,V_1-77,V_2-77,V_3-77,V_4-77,V_5-77,V_6-77,V_7-77,V_8-77,V_9-77,V_10-77,V_11-77,V_12-77,V_13-77,V_14-77,V_15-77,V_16-77,V_17-77,V_18-77,V_19-77,V_20-77
78,V_1-78,V_2-78,V_3-78,V_4-78,V_5-78,V_6-78,V_7-78,V_8-78,V_9-78,V_10-78,V_11-78,V_12-78,V_13-78,V_14-78,V_15-78,V_16-78,V_17-78,V_18-78,V_19-78,V_20-78
79,V_1-79,V_2-79,V_3-79,V_4-79,V_5-79,V_6-79,V_7-79,V_8-79,V_9-79,V_10-79,V_11-79,V_12-79,V_13-79,V_14-79,V_15-79,V_16-79,V_17-79,V_18-79,V_19-79,V_20-79
80,V_1-80,V_2-80,V_3-80,V_4-80,V_5-80,V_6-80,V_7-80,V_8-80,V_9-80,V_10-80,V_11-80,V_12-80,V_13-80,V_14-80,V_15-80,V_16-80,V_17-80,V_18-80,V_19-80,V_20-80
81,V_1-81,V_2-81,V_3-81,V_4-81,V_5-81,V_6-81,V_7-81,V_8-81,V_9-81,V_10-81,V_11-81,V_12-81,V_13-81,V_14-81,V_15-81,V_16-81,V_17-81,V_18-81,V_19-81,V_20-81
82,V_1-82,V_2-82,V_3-82,V_4-82,V_5-82,V_6-82,V_7-82,V_8-82,V_9-82,V_10-82,V_11-82,V_12-82,V_13-82,V_14-82,V_15-82,V_16-82,V_17-82,V_18-82,V_19-82,V_20-82
83,V_1-83,V_2-83,V_3-83,V_4-83,V_5-83,V_6-83,V_7-83,V_8-83,V_9-83,V_10-83,V_11-83,V_12-83,V_13-83,V_14-83,V_15-83,V_16-83,V_17-83,V_18-83,V_19-83,V_20-83
84,V_1-84,V_2-84,V_3-84,V_4-84,V_5-84,V_6-84,V_7-84,V_8-84,V_9-84,V_10-84,V_11-84,V_12-84,V_13-84,V_14-84,V_15-84,V_16-84,V_17-84,V_18-84,V_19-84,V_20-84
85,V_1-85,V_2-85,V_3-85,V_4-85,V_5-85,V_6-85,V_7-85,V_8-85,V_9-85,V_10-85,V_11-85,V_12-85,V_13-85,V_14-85,V_15-85,V_16-85,V_17-85,V_18-85,V_19-85,V_20-85
86,V_1-86,V_2-86,V_3-86,V_4-86,V_5-86,V_6-86,V_7-86,V_8-86,V_9-86,V_10-86,V_11-86,V_12-86,V_13-86,V_14-86,V_15-86,V_16-86,V_17-86,V_18-86,V_19-86,V_20-86
87,V_1-87,V_2-87,V_3-87,V_4-87,V_5-87,V_6-87,V_7-87,V_8-87,V_9-87,V_10-87,V_11-87,V_12-87,V_13-87,V_14-87,V_15-87,V_16-87,V_17-87,V_18-87,V_19-87,V_20-87
88,V_1-88,V_2-88,V_3-88,V_4-88,V_5-88,V_6-88,V_7-88,V_8-88,V_9-88,V_10-88,V_11-88,V_12-88,V_13-88,V_14-88,V_15-88,V_16-88,V_17-88,V_18-88,V_19-88,V_20-88
89,V_1-89,V_2-89,V_3-89,V_4-89,V_5-89,V_6-89,V_7-89,V_8-89,V_9-89,V_10-89,V_11-89,V_12-89,V_13-89,V_14-89,V_15-89,V_16-89,V_17-89,V_18-89,V_19-89,V_20-89
90,V_1-90,V_2-90,V_3-90,V_4-90,V_5-90,V_6-90,V_7-90,V_8-90,V_9-90,V_10-90,V_11-90,V_12-90,V_13-90,V_14-90,V_15-90,V_16-90,V_17-90,V_18-90,V_19-90,V_20-90
91,V_1-91,V_2-91,V_3-91,V_4-91,V_5-91,V_6-91,V_7-91,V_8-91,V_9-91,V_10-91,V_11-91,V_12-91,V_13-91,V_14-91,V_15-91,V_16-91,V_17-91,V_18-91,V_19-91,V_20-91
92,V_1-92,V_2-92,V_3-92,V_4-92,V_5-92,V_6-92,V_7-92,V_8-92,V_9-92,V_10-92,V_11-92,V_12-92,V_13-92,V_14-92,V_15-92,V_16-92,V_17-92,V_18-92,V_19-92,V_20-92
93,V_1-93,V_2-93,V_3-93,V_4-93,V_5-93,V_6-93,V_7-93,V_8-93,V_9-93,V_10-93,V_11-93,V_12-93,V_13-93,V_14-93,V_15-93,V_16-93,V_17-93,V_18-93,V_19-93,V_20-93
94,V_1-94,V_2-94,V_3-94,V_4-94,V_5-94,V_6-94,V_7-94,V_8-94,V_9-94,V_10-94,V_11-94,V_12-94,V_13-94,V_14-94,V_15-94,V_16-94,V_17-94,V_18-94,V_19-94,V_20-94
95,V_1-95,V_2-95,V_3-95,V_4-95,V_5-95,V_6-95,V_7-95,V_8-95,V_9-95,V_10-95,V_11-95,V_12-95,V_13-95,V_14-95,V_15-95,V_16-95,V_17-95,V_18-95,V_19-95,V_20-95
96,V_1-96,V_2-96,V_3-96,V_4-96,V_5-96,V_6-96,V_7-96,V_8-96,V_9-96,V_10-96,V_11-96,V_12-96,V_13-96,V_14-96,V_15-96,V_16-96,V_17-96,V_18-96,V_19-96,V_20-96
97,V_1-97,V_2-97,V_3-97,V_4-97,V_5-97,V_6-97,V_7-97,V_8-97,V_9-97,V_10-97,V_11-97,V_12-97,V_13-97,V_14-97,V_15-97,V_16-97,V_17-97,V_18-97,V_19-97,V_20-97
98,V_1-98,V_2-98,V_3-98,V_4-98,V_5-98,V_6-98,V_7-98,V_8-98,V_9-98,V_10-98,V_11-98,V_12-98,V_13-98,V_14-98,V_15-98,V_16-98,V_17-98,V_18-98,V_19-98,V_20-98
99,V_1-99,V_2-99,V_3-99,V_4-99,V_5-99,V_6-99,V_7-99,V_8-99,V_9-99,V_10-99,V_11-99,V_12-99,V_13-99,V_14-99,V_15-99,V_16-99,V_17-99,V_18-99,V_19-99,V_20-99
100,V_1-100,V_2-100,V_3-100,V_4-100,V_5-100,V_6-100,V_7-100,V_8-100,V_9-100,V_10-100,V_11-100,V_12-100,V_13-100,V_14-100,V_15-100,V_16-100,V_17-100,V_18-100,V_19-100,V_20-100
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
            rr:graphMap [ rr:template "http://example.org/graph{p1}" ] ;
            rr:objectMap [ a rr:ObjectMap ;
                    rr:column "p1" ] ;
            rr:predicateMap [ a rr:PredicateMap ;
                    rr:constant ex:p1 ] ] ;
    rr:subjectMap [ rr:template "http://ex.com/table/{p1}" ] .
```

#### Output RDF

```
<http://ex.com/table/V_1-1> <http://example.com/p1> "V_1-1" <http://example.org/graphV_1-1>.
<http://ex.com/table/V_1-2> <http://example.com/p1> "V_1-2" <http://example.org/graphV_1-2>.
<http://ex.com/table/V_1-3> <http://example.com/p1> "V_1-3" <http://example.org/graphV_1-3>.
<http://ex.com/table/V_1-4> <http://example.com/p1> "V_1-4" <http://example.org/graphV_1-4>.
<http://ex.com/table/V_1-5> <http://example.com/p1> "V_1-5" <http://example.org/graphV_1-5>.
<http://ex.com/table/V_1-6> <http://example.com/p1> "V_1-6" <http://example.org/graphV_1-6>.
<http://ex.com/table/V_1-7> <http://example.com/p1> "V_1-7" <http://example.org/graphV_1-7>.
<http://ex.com/table/V_1-8> <http://example.com/p1> "V_1-8" <http://example.org/graphV_1-8>.
<http://ex.com/table/V_1-9> <http://example.com/p1> "V_1-9" <http://example.org/graphV_1-9>.
<http://ex.com/table/V_1-10> <http://example.com/p1> "V_1-10" <http://example.org/graphV_1-10>.
<http://ex.com/table/V_1-11> <http://example.com/p1> "V_1-11" <http://example.org/graphV_1-11>.
<http://ex.com/table/V_1-12> <http://example.com/p1> "V_1-12" <http://example.org/graphV_1-12>.
<http://ex.com/table/V_1-13> <http://example.com/p1> "V_1-13" <http://example.org/graphV_1-13>.
<http://ex.com/table/V_1-14> <http://example.com/p1> "V_1-14" <http://example.org/graphV_1-14>.
<http://ex.com/table/V_1-15> <http://example.com/p1> "V_1-15" <http://example.org/graphV_1-15>.
<http://ex.com/table/V_1-16> <http://example.com/p1> "V_1-16" <http://example.org/graphV_1-16>.
<http://ex.com/table/V_1-17> <http://example.com/p1> "V_1-17" <http://example.org/graphV_1-17>.
<http://ex.com/table/V_1-18> <http://example.com/p1> "V_1-18" <http://example.org/graphV_1-18>.
<http://ex.com/table/V_1-19> <http://example.com/p1> "V_1-19" <http://example.org/graphV_1-19>.
<http://ex.com/table/V_1-20> <http://example.com/p1> "V_1-20" <http://example.org/graphV_1-20>.
<http://ex.com/table/V_1-21> <http://example.com/p1> "V_1-21" <http://example.org/graphV_1-21>.
<http://ex.com/table/V_1-22> <http://example.com/p1> "V_1-22" <http://example.org/graphV_1-22>.
<http://ex.com/table/V_1-23> <http://example.com/p1> "V_1-23" <http://example.org/graphV_1-23>.
<http://ex.com/table/V_1-24> <http://example.com/p1> "V_1-24" <http://example.org/graphV_1-24>.
<http://ex.com/table/V_1-25> <http://example.com/p1> "V_1-25" <http://example.org/graphV_1-25>.
<http://ex.com/table/V_1-26> <http://example.com/p1> "V_1-26" <http://example.org/graphV_1-26>.
<http://ex.com/table/V_1-27> <http://example.com/p1> "V_1-27" <http://example.org/graphV_1-27>.
<http://ex.com/table/V_1-28> <http://example.com/p1> "V_1-28" <http://example.org/graphV_1-28>.
<http://ex.com/table/V_1-29> <http://example.com/p1> "V_1-29" <http://example.org/graphV_1-29>.
<http://ex.com/table/V_1-30> <http://example.com/p1> "V_1-30" <http://example.org/graphV_1-30>.
<http://ex.com/table/V_1-31> <http://example.com/p1> "V_1-31" <http://example.org/graphV_1-31>.
<http://ex.com/table/V_1-32> <http://example.com/p1> "V_1-32" <http://example.org/graphV_1-32>.
<http://ex.com/table/V_1-33> <http://example.com/p1> "V_1-33" <http://example.org/graphV_1-33>.
<http://ex.com/table/V_1-34> <http://example.com/p1> "V_1-34" <http://example.org/graphV_1-34>.
<http://ex.com/table/V_1-35> <http://example.com/p1> "V_1-35" <http://example.org/graphV_1-35>.
<http://ex.com/table/V_1-36> <http://example.com/p1> "V_1-36" <http://example.org/graphV_1-36>.
<http://ex.com/table/V_1-37> <http://example.com/p1> "V_1-37" <http://example.org/graphV_1-37>.
<http://ex.com/table/V_1-38> <http://example.com/p1> "V_1-38" <http://example.org/graphV_1-38>.
<http://ex.com/table/V_1-39> <http://example.com/p1> "V_1-39" <http://example.org/graphV_1-39>.
<http://ex.com/table/V_1-40> <http://example.com/p1> "V_1-40" <http://example.org/graphV_1-40>.
<http://ex.com/table/V_1-41> <http://example.com/p1> "V_1-41" <http://example.org/graphV_1-41>.
<http://ex.com/table/V_1-42> <http://example.com/p1> "V_1-42" <http://example.org/graphV_1-42>.
<http://ex.com/table/V_1-43> <http://example.com/p1> "V_1-43" <http://example.org/graphV_1-43>.
<http://ex.com/table/V_1-44> <http://example.com/p1> "V_1-44" <http://example.org/graphV_1-44>.
<http://ex.com/table/V_1-45> <http://example.com/p1> "V_1-45" <http://example.org/graphV_1-45>.
<http://ex.com/table/V_1-46> <http://example.com/p1> "V_1-46" <http://example.org/graphV_1-46>.
<http://ex.com/table/V_1-47> <http://example.com/p1> "V_1-47" <http://example.org/graphV_1-47>.
<http://ex.com/table/V_1-48> <http://example.com/p1> "V_1-48" <http://example.org/graphV_1-48>.
<http://ex.com/table/V_1-49> <http://example.com/p1> "V_1-49" <http://example.org/graphV_1-49>.
<http://ex.com/table/V_1-50> <http://example.com/p1> "V_1-50" <http://example.org/graphV_1-50>.
<http://ex.com/table/V_1-51> <http://example.com/p1> "V_1-51" <http://example.org/graphV_1-51>.
<http://ex.com/table/V_1-52> <http://example.com/p1> "V_1-52" <http://example.org/graphV_1-52>.
<http://ex.com/table/V_1-53> <http://example.com/p1> "V_1-53" <http://example.org/graphV_1-53>.
<http://ex.com/table/V_1-54> <http://example.com/p1> "V_1-54" <http://example.org/graphV_1-54>.
<http://ex.com/table/V_1-55> <http://example.com/p1> "V_1-55" <http://example.org/graphV_1-55>.
<http://ex.com/table/V_1-56> <http://example.com/p1> "V_1-56" <http://example.org/graphV_1-56>.
<http://ex.com/table/V_1-57> <http://example.com/p1> "V_1-57" <http://example.org/graphV_1-57>.
<http://ex.com/table/V_1-58> <http://example.com/p1> "V_1-58" <http://example.org/graphV_1-58>.
<http://ex.com/table/V_1-59> <http://example.com/p1> "V_1-59" <http://example.org/graphV_1-59>.
<http://ex.com/table/V_1-60> <http://example.com/p1> "V_1-60" <http://example.org/graphV_1-60>.
<http://ex.com/table/V_1-61> <http://example.com/p1> "V_1-61" <http://example.org/graphV_1-61>.
<http://ex.com/table/V_1-62> <http://example.com/p1> "V_1-62" <http://example.org/graphV_1-62>.
<http://ex.com/table/V_1-63> <http://example.com/p1> "V_1-63" <http://example.org/graphV_1-63>.
<http://ex.com/table/V_1-64> <http://example.com/p1> "V_1-64" <http://example.org/graphV_1-64>.
<http://ex.com/table/V_1-65> <http://example.com/p1> "V_1-65" <http://example.org/graphV_1-65>.
<http://ex.com/table/V_1-66> <http://example.com/p1> "V_1-66" <http://example.org/graphV_1-66>.
<http://ex.com/table/V_1-67> <http://example.com/p1> "V_1-67" <http://example.org/graphV_1-67>.
<http://ex.com/table/V_1-68> <http://example.com/p1> "V_1-68" <http://example.org/graphV_1-68>.
<http://ex.com/table/V_1-69> <http://example.com/p1> "V_1-69" <http://example.org/graphV_1-69>.
<http://ex.com/table/V_1-70> <http://example.com/p1> "V_1-70" <http://example.org/graphV_1-70>.
<http://ex.com/table/V_1-71> <http://example.com/p1> "V_1-71" <http://example.org/graphV_1-71>.
<http://ex.com/table/V_1-72> <http://example.com/p1> "V_1-72" <http://example.org/graphV_1-72>.
<http://ex.com/table/V_1-73> <http://example.com/p1> "V_1-73" <http://example.org/graphV_1-73>.
<http://ex.com/table/V_1-74> <http://example.com/p1> "V_1-74" <http://example.org/graphV_1-74>.
<http://ex.com/table/V_1-75> <http://example.com/p1> "V_1-75" <http://example.org/graphV_1-75>.
<http://ex.com/table/V_1-76> <http://example.com/p1> "V_1-76" <http://example.org/graphV_1-76>.
<http://ex.com/table/V_1-77> <http://example.com/p1> "V_1-77" <http://example.org/graphV_1-77>.
<http://ex.com/table/V_1-78> <http://example.com/p1> "V_1-78" <http://example.org/graphV_1-78>.
<http://ex.com/table/V_1-79> <http://example.com/p1> "V_1-79" <http://example.org/graphV_1-79>.
<http://ex.com/table/V_1-80> <http://example.com/p1> "V_1-80" <http://example.org/graphV_1-80>.
<http://ex.com/table/V_1-81> <http://example.com/p1> "V_1-81" <http://example.org/graphV_1-81>.
<http://ex.com/table/V_1-82> <http://example.com/p1> "V_1-82" <http://example.org/graphV_1-82>.
<http://ex.com/table/V_1-83> <http://example.com/p1> "V_1-83" <http://example.org/graphV_1-83>.
<http://ex.com/table/V_1-84> <http://example.com/p1> "V_1-84" <http://example.org/graphV_1-84>.
<http://ex.com/table/V_1-85> <http://example.com/p1> "V_1-85" <http://example.org/graphV_1-85>.
<http://ex.com/table/V_1-86> <http://example.com/p1> "V_1-86" <http://example.org/graphV_1-86>.
<http://ex.com/table/V_1-87> <http://example.com/p1> "V_1-87" <http://example.org/graphV_1-87>.
<http://ex.com/table/V_1-88> <http://example.com/p1> "V_1-88" <http://example.org/graphV_1-88>.
<http://ex.com/table/V_1-89> <http://example.com/p1> "V_1-89" <http://example.org/graphV_1-89>.
<http://ex.com/table/V_1-90> <http://example.com/p1> "V_1-90" <http://example.org/graphV_1-90>.
<http://ex.com/table/V_1-91> <http://example.com/p1> "V_1-91" <http://example.org/graphV_1-91>.
<http://ex.com/table/V_1-92> <http://example.com/p1> "V_1-92" <http://example.org/graphV_1-92>.
<http://ex.com/table/V_1-93> <http://example.com/p1> "V_1-93" <http://example.org/graphV_1-93>.
<http://ex.com/table/V_1-94> <http://example.com/p1> "V_1-94" <http://example.org/graphV_1-94>.
<http://ex.com/table/V_1-95> <http://example.com/p1> "V_1-95" <http://example.org/graphV_1-95>.
<http://ex.com/table/V_1-96> <http://example.com/p1> "V_1-96" <http://example.org/graphV_1-96>.
<http://ex.com/table/V_1-97> <http://example.com/p1> "V_1-97" <http://example.org/graphV_1-97>.
<http://ex.com/table/V_1-98> <http://example.com/p1> "V_1-98" <http://example.org/graphV_1-98>.
<http://ex.com/table/V_1-99> <http://example.com/p1> "V_1-99" <http://example.org/graphV_1-99>.
<http://ex.com/table/V_1-100> <http://example.com/p1> "V_1-100" <http://example.org/graphV_1-100>.
```
