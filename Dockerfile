FROM python:3.9-buster

RUN apt update
RUN apt install -y protobuf-compiler
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY run.py /src/
COPY datasets /src/datasets
