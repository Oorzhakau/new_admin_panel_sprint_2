# Реализация API для кинотеатра

Цель проекта: создать API, возвращающий список фильмов в формате, описанном в openapi-файле, и позволяющий получить информацию об одном фильме.

Проверить результат работы API можно при помощи Postman. Запустите сервер на 127.0.0.1:8000 и воспользуйтесь тестами из файла `movies API.postman_collection.json`. В тестах предполагается, что в вашем API установлена пагинация и выводится по 50 элементов на странице.

## Установка:
1. Клонируйте репозиторий на локальную машину.
   ```https://github.com/Oorzhakau/new_admin_panel_sprint_2.git```
2. Установите виртуальное окружение в папке проекта.
```
cd django_api/app/
python -m venv venv
```
3. Активируйте виртуальное окружение.
   ```source venv\Scripts\activate```
4. Установите зависимости.
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```
5. Создать файл .env на основе .env_example в директории `app/config/` и указать значение переменных окружения 
(для соединения с базой postgres укажите корректный хост, порт, базу, пользвателя и пароль):
```
# === Database Postgres ===

POSTGRES_DB_ENGINE=django.db.backends.postgresql
POSTGRES_DB=movies_database
POSTGRES_USER=app
POSTGRES_PASSWORD=123qwe
POSTGRES_DB_HOST=127.0.0.1
POSTGRES_DB_PORT=5432
POSTGRES_DB_SCHEMA=content

# === Django ===

DJ_SECRET_KEY=django-insecure-asdasd123

DJ_DEBUG=True
```
6. Запустите проект: `python3 manage.py runserver`.