FROM ubuntu:20.04
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get install -y python3 python3-dev python3-pip ffmpeg
RUN pip install -U pip

WORKDIR /code
COPY . .
RUN pip install .[dev]
