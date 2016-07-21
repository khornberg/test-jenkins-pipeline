FROM jenkins:latest
USER root
RUN apt-get update && apt-get install -y python && apt-get clean
RUN apt-get update && apt-get install -y curl && apt-get clean

RUN curl https://bootstrap.pypa.io/get-pip.py | python

RUN pip install virtualenv
