FROM python:latest

RUN mkdir /automation
RUN apt-get update && apt-get -y install vim

COPY ./api_udemy_course /automation/api_udemy_course
COPY ./setup.py /automation
COPY ./pyproject.toml /automation
COPY ./requirements.txt /automation
COPY ./env_docker.sh /automation

WORKDIR /automation
RUN pip install -r requirements.txt