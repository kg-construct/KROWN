################################################################################
# Ontop
# https://github.com/ontop/ontop
################################################################################
FROM ubuntu:22.04
# Configure the Ontop version to use
ARG ONTOP_VERSION

# Install latest updates and dependencies
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y openjdk-11-jdk less vim wget unzip

# Download Ontop release
RUN wget -O ontop.zip https://github.com/ontop/ontop/releases/download/ontop-${ONTOP_VERSION}/ontop-cli-${ONTOP_VERSION}.zip
RUN unzip ontop.zip -d /ontop
COPY mysql-connector.jar /ontop/jdbc/
COPY postgresql-connector.jar /ontop/jdbc/

# Expose gtfs-bench folders
RUN mkdir /data
RUN mkdir /mappings
RUN mkdir /results
RUN mkdir /configs

# Silent
CMD ["tail", "-f", "/dev/null"]
