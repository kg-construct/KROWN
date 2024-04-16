#!/bin/sh
set -e
#
# Build script for all Docker containers.
#
# Copyright (c) by ANONYMOUS (2022)
# License: GPLv3
#

MYSQL_VERSION='8.0'
POSTGRESQL_VERSION='14.5'
VIRTUOSO_VERSION='7.2.7'
FUSEKI_VERSION='4.6.1'
MORPHKGC_VERSION='2.2.0'
MORPHRDB_VERSION='3.12.5'
ONTOP_VERSION='5.0.0'
RMLMAPPER_VERSION='6.0.0'
RMLMAPPER_BUILD='363'
SDMRDFIZER_VERSION='4.6.6.5'
YARRRML_VERSION='1.3.6'
RMLSTREAMER_VERSION='2.5.0'

# MySQL
echo "*** Building MySQL $MYSQL_VERSION ... ***"
cd MySQL
docker build --build-arg MYSQL_VERSION=$MYSQL_VERSION \
    -t kgconstruct/mysql:v$MYSQL_VERSION .
docker push kgconstruct/mysql:v$MYSQL_VERSION
cd ..

# PostgreSQL
echo "*** Building PostgreSQL $POSTGRESQL_VERSION ... ***"
cd PostgreSQL
docker build --build-arg POSTGRESQL_VERSION=$POSTGRESQL_VERSION \
    -t kgconstruct/postgresql:v$POSTGRESQL_VERSION .
docker push kgconstruct/postgresql:v$POSTGRESQL_VERSION
cd ..

# Virtuoso
echo "*** Building Virtuoso $VIRTUOSO_VERSION ... ***"
cd Virtuoso
docker build --build-arg VIRTUOSO_VERSION=$VIRTUOSO_VERSION \
    -t kgconstruct/virtuoso:v$VIRTUOSO_VERSION .
docker push kgconstruct/virtuoso:v$VIRTUOSO_VERSION
cd ..
# Fuseki
echo "*** Building Fuseki $FUSEKI_VERSION ... ***"
cd Fuseki
docker build --build-arg JENA_VERSION=$FUSEKI_VERSION \
    -t kgconstruct/fuseki:v$FUSEKI_VERSION .
docker push kgconstruct/fuseki:v$FUSEKI_VERSION
cd ..

# Morph-KGC
echo "*** Building Morph-KGC $MORPHKGC_VERSION ... ***"
cd Morph-KGC
docker build --build-arg MORPHKGC_VERSION=$MORPHKGC_VERSION \
    -t kgconstruct/morph-kgc:v$MORPHKGC_VERSION .
docker push kgconstruct/morph-kgc:v$MORPHKGC_VERSION
cd ..

# Morph-KGC-Optimized
echo "*** Building Morph-KGC-Optimized $MORPHKGC_VERSION ... ***"
cd Morph-KGC-Optimized
docker build --build-arg MORPHKGC_VERSION=$MORPHKGC_VERSION \
    -t kgconstruct/morph-kgc-optimized:v$MORPHKGC_VERSION .
docker push kgconstruct/morph-kgc-optimized:v$MORPHKGC_VERSION
cd ..

# Morph-RDB
echo "*** Building Morph-RDB $MORPHRDB_VERSION ... ***"
cd Morph-RDB
docker build --build-arg MORPHRDB_VERSION=$MORPHRDB_VERSION \
    -t kgconstruct/morph-rdb:v$MORPHRDB_VERSION .
docker push kgconstruct/morph-rdb:v$MORPHRDB_VERSION
cd ..

# Ontop
echo "*** Building Ontop $ONTOP_VERSION ... ***"
cd Ontop
docker build \
    --build-arg ONTOP_VERSION=$ONTOP_VERSION \
    -t kgconstruct/ontop:v$ONTOP_VERSION .
docker push kgconstruct/ontop:v$ONTOP_VERSION
cd ..

# RMLMapper
echo "*** Building RMLMapper $RMLMAPPER_VERSION r$RMLMAPPER_BUILD ... ***"
cd RMLMapper
docker build --build-arg RMLMAPPER_VERSION=$RMLMAPPER_VERSION \
    --build-arg RMLMAPPER_BUILD=$RMLMAPPER_BUILD \
    -t kgconstruct/rmlmapper:v$RMLMAPPER_VERSION .
docker push kgconstruct/rmlmapper:v$RMLMAPPER_VERSION
cd ..

# SDM-RDFizer
echo "*** Building SDM-RDFizer $SDMRDFIZER_VERSION ... ***"
cd SDM-RDFizer
docker build --build-arg SDMRDFIZER_VERSION=$SDMRDFIZER_VERSION \
    -t kgconstruct/sdm-rdfizer:v$SDMRDFIZER_VERSION .
docker push kgconstruct/sdm-rdfizer:v$SDMRDFIZER_VERSION
cd ..

# YARRRML
echo "*** Building YARRML $YARRRML_VERSION ... ***"
cd YARRRML
docker build --build-arg YARRRML_VERSION=$YARRRML_VERSION \
    -t kgconstruct/yarrrml:v$YARRRML_VERSION .
docker push kgconstruct/yarrrml:v$YARRRML_VERSION
cd ..

# RMLStreamer
echo "*** Building RMLStreamer $RMLSTREAMER_VERSION ... ***"
cd RMLStreamer
docker build --build-arg RMLSTREAMER_VERSION=$RMLSTREAMER_VERSION \
    --build-arg USER_ID="$(id -u)" \
    --build-arg GROUP_ID="$(id -g)" \
    -t kgconstruct/rmlstreamer:v$RMLSTREAMER_VERSION .
docker push kgconstruct/rmlstreamer:v$RMLSTREAMER_VERSION
cd ..
