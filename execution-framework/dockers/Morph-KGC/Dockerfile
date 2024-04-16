################################################################################
# Morph-KGC
# https://github.com/oeg-upm/morph-kgc
################################################################################
FROM ubuntu:22.04

# Install latest updates and dependencies
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y python3 python3-pip gcc libpq-dev

# Download Morph-KGC release
RUN pip3 install morph-kgc psycopg2 pymysql pymssql cryptography

# Expose gtfs-bench folders
RUN mkdir /data
RUN mkdir /mappings
RUN mkdir /results
RUN mkdir /configs

# https://stackoverflow.com/questions/50391941/eoferror-marshal-data-too-short
RUN find /usr/local/lib/ -name \*.pyc -delete

# Silent
CMD ["tail", "-f", "/dev/null"]
