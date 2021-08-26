# Installation

- clone project:
```
git@github.com:AndIsaev/Admin_panel_sprint_2.git
```
- create new database postgresql in your host

- create file .env with parametrs your database in movies_admin:

```
DB_ENGINE=django.db.backends.postgresql_psycopg2
DB_NAME=db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=some_password
DB_HOST=host.docker.internal (if you use macos) or 'localhost'
DB_PORT=5432
SECRET_KEY= 'your secret key' 
```

- run command:
```
docker compose up 
```

- create superuser:
```
docker-compose exec web python manage.py collectstatic --noinput --clear
```

- load static
```
docker-compose run --entrypoint="/bin/bash -c" web "python manage.py createsuperuser"
```

- go to url in your browser:
```
http://localhost/admin/
```


# Техническое задание

В качестве второго задания предлагаем расширить проект «Панель администратора»: запустить приложение через WSGI/ASGI, настроить отдачу статических файлов через Nginx и подготовить инфраструктуру для работы с Docker. Для этого перенесите в репозиторий код, который вы написали в первом спринте, и выполните задания из папки `tasks`.

## Используемые технологии

- Приложение запускается под управлением сервера WSGI/ASGI.
- Для отдачи [статических файлов](https://nginx.org/ru/docs/beginners_guide.html#static) используется **Nginx.**
- Виртуализация осуществляется в **Docker.**

## Основные компоненты системы

1. **Cервер WSGI/ASGI** — сервер с запущенным приложением.
2. **Nginx** — прокси-сервер, который является точкой входа для web-приложения.
3. **PostgreSQL** — реляционное хранилище данных. 
4. **ETL** — механизм обновления данных между PostgreSQL и ES.

## Схема сервиса

![all](images/all.png)

## Требования к проекту

1. Приложение должно быть запущено через WSGI/ASGI.
2. Все компоненты системы находятся в Docker.
3. Отдача статических файлов осуществляется за счёт Nginx.

## Рекомендации к проекту

1. Для работы с WSGI/ASGI-сервером база данных использует специального юзера.
2. Для взаимодействия между контейнерами используйте docker compose.
