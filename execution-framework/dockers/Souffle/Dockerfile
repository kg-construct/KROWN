################################################################################
#souffle
################################################################################
FROM ubuntu:22.04

# Install latest updates and dependencies
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install bash
RUN apt-get install -y bash python3 python3-pip gcc libpq-dev \
	git bison build-essential clang cmake doxygen flex g++ \
	libffi-dev libncurses5-dev libsqlite3-dev make mcpp \
	sqlite zlib1g-dev

# Download Souffle release
RUN mkdir souffle 
RUN git clone https://github.com/souffle-lang/souffle.git /souffle
#COPY functors.cpp /souffle/functors.cpp
WORKDIR /souffle

RUN cmake -S . -B build -DCMAKE_INSTALL_PREFIX=.
RUN cmake --build build -j8 --target install

# Expose folders
RUN mkdir /data
RUN mkdir /mappings
RUN mkdir /results
RUN mkdir /configs
RUN PATH=$PATH:/souffle/bin

# Silent
CMD ["tail", "-f", "/dev/null"]
