# pull official base image
FROM python:3.9.5
# set work directory
RUN mkdir /code
WORKDIR /code
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install dependencies
COPY requirements/base.txt /code
COPY requirements/dev.txt /code
COPY requirements/production.txt /code
# выполнить команду (как в терминале, с тем же синтаксисом) для установки пакетов из requirements.txt
RUN python -m pip install --upgrade pip
RUN pip3 install -r /code/base.txt
RUN pip3 install -r /code/dev.txt
RUN pip3 install -r /code/production.txt
# copy project
COPY ./entrypoint.sh .

COPY . .

ENTRYPOINT ["./entrypoint.sh"]