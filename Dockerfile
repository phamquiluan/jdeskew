FROM ubuntu:20.04
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install --no-install-recommends -y python3.8 python3.8-dev python3-pip ffmpeg=7:4.2.4-1ubuntu0.1\
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

RUN pip install pip==22.0.3

WORKDIR /code
COPY . .
RUN pip install .[dev]
