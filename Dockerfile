FROM ubuntu:20.04
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install --no-install-recommends -y python3.8 python3.8-dev python3-pip ffmpeg\
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

RUN pip install pip==22.0.3

# Copy source code
WORKDIR /app
COPY . /app/

RUN pip install .[dev]
EXPOSE 80
ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
