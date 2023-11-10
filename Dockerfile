#
# Ubuntu Dockerfile
#
# https://github.com/dockerfile/ubuntu
#

# Pull base image.
FROM ubuntu:22.04

# Install.
RUN \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y build-essential && \
  apt-get install -y software-properties-common && \
  apt-get install -y byobu curl git htop man unzip vim wget && \
  apt-get install -y python3 && \
  apt-get install -y net-tools && \
  rm -rf /var/lib/apt/lists/*


# Set environment variables.
ENV HOME /root

# Define working directory.
WORKDIR /root

COPY . . 
# Define default command.
CMD ["bash"]


