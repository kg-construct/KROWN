################################################################################
# Morph-KGC-Optimized
# https://github.com/oeg-upm/morph-kgc
################################################################################
FROM ubuntu:22.04

# Install latest updates and dependencies
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get update && apt-get install -y python3 python3-pip gcc libpq-dev wget

# Download Morph-KGC release
RUN pip3 install psycopg2 pymysql pymssql cryptography
COPY c3a7056447350c3a8c085169b05b6fc5442f2f06.zip /c3a7056447350c3a8c085169b05b6fc5442f2f06.zip
RUN pip3 install /c3a7056447350c3a8c085169b05b6fc5442f2f06.zip
COPY morphkgc-optimized /morphkgc-optimized
RUN chmod +x /morphkgc-optimized

# Expose gtfs-bench folders
RUN mkdir /data
RUN mkdir /mappings
RUN mkdir /results
RUN mkdir /configs

# https://stackoverflow.com/questions/50391941/eoferror-marshal-data-too-short
RUN find /usr/local/lib/ -name \*.pyc -delete

# Silent
CMD ["tail", "-f", "/dev/null"]
