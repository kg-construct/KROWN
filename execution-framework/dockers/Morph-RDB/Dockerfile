################################################################################
# Morph-RDB
# https://github.com/oeg-upm/morph-rdb
################################################################################
FROM ubuntu:22.04

# Install latest updated and dependencies
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y openjdk-8-jdk less vim git maven

# Build Morph-RDB
RUN mkdir /morphrdb
COPY . /morphrdb
RUN cd /morphrdb && mvn clean install
RUN cp -r /morphrdb/morph-rdb-dist/target/*.jar /
RUN cp -r /morphrdb/morph-examples/dependency /
RUN cp -r /morphrdb/run-docker.sh /

# Silent
CMD ["tail", "-f", "/dev/null"]
