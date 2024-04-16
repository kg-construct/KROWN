################################################################################
# RMLStreamer
# https://github.com/RMLio/RMLStreamer
################################################################################
FROM ubuntu:22.04
# Configure the RMLStreamer version to use
ARG RMLSTREAMER_VERSION
ARG USER_ID
ARG GROUP_ID

# Install latest updates and dependencies
RUN apt update
RUN apt upgrade -y
RUN apt update && apt install -y openjdk-11-jdk less vim wget unzip

RUN addgroup --gid $GROUP_ID user
RUN adduser --disabled-password --gecos '' --uid $USER_ID --gid $GROUP_ID user

# Download RMLStreamer release
RUN mkdir rmlstreamer && wget -O /rmlstreamer/rmlstreamer.jar https://github.com/RMLio/RMLStreamer/releases/download/v${RMLSTREAMER_VERSION}/RMLStreamer-v${RMLSTREAMER_VERSION}-standalone.jar

# Expose data folder
RUN mkdir /data

USER user

# Silent
CMD ["tail", "-f", "/dev/null"]
