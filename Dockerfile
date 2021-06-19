FROM python:3.9-buster

RUN apt update
RUN apt install -y protobuf-compiler

WORKDIR /src

# other libraries
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY run.py ./
COPY datasets ./datasets
