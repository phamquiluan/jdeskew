FROM ubuntu:20.04
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install --no-install-recommends -y python3 python3-dev python3-pip ffmpeg \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

RUN pip install -U pip

WORKDIR /code
COPY . .
RUN pip install .[dev]
