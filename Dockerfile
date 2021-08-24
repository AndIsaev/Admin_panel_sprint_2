# pull official base image
FROM python:3.9.5
# set work directory
WORKDIR /usr/src/app
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install dependencies
RUN pip install --upgrade pip
RUN pip3 install -r /code/base.txt
RUN pip3 install -r /code/dev.txt
RUN pip3 install -r /code/production.txt
# copy project
COPY . .