#!/usr/bin/env bash

python3 manage.py migrate
python3 manage.py makemigrations movies
python3 manage.py migrate --fake movies 0001
python3 manage.py create_admin
python3 manage.py loaddata movies/fixtures/movies.json
