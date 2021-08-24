# создать образ на основе базового слоя python (там будет ОС и интерпретатор Python)
FROM python:3.9.5

# создать директорию /code
RUN mkdir /code
WORKDIR /code

ENV PYTHONUNBUFFERED 1
# скопировать файл requirements.txt из директории, в которой лежит докерфайл, в директорию /code
COPY requirements/base.txt /code
COPY requirements/dev.txt /code
COPY requirements/production.txt /code
# выполнить команду (как в терминале, с тем же синтаксисом) для установки пакетов из requirements.txt
RUN python -m pip install --upgrade pip
RUN pip3 install -r /code/base.txt
RUN pip3 install -r /code/dev.txt
RUN pip3 install -r /code/production.txt
COPY . /code
RUN ["chmod", "+x", "./entrypoint.sh"]
ENTRYPOINT ["./entrypoint.sh"]
# скопировать всё содержимое директории, в которой лежит докерфайл, в директорию /code



# при старте контейнера выполнить runserver 
