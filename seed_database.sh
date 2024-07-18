#!/bin/bash

rm db.sqlite3
rm -rf ./pittyapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations pittyapi
python3 manage.py migrate pittyapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens

