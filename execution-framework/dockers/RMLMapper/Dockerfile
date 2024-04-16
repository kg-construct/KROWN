################################################################################
# RMLMapper
# https://github.com/RMLio/rmlmapper-java
################################################################################
FROM ubuntu:22.04
# Configure the RMLMapper version to use
ARG RMLMAPPER_VERSION
ARG RMLMAPPER_BUILD

# Install latest updates and dependencies
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y openjdk-8-jdk less vim wget unzip

# Download RMLMapper release
RUN mkdir rmlmapper && wget -O rmlmapper/rmlmapper.jar https://github.com/RMLio/rmlmapper-java/releases/download/v${RMLMAPPER_VERSION}/rmlmapper-${RMLMAPPER_VERSION}-r${RMLMAPPER_BUILD}-all.jar

# Expose data folder
RUN mkdir /data

# Silent
CMD ["tail", "-f", "/dev/null"]
