#!/bin/bash

>&2 echo "-------- Waiting for postgres --------"
while ! nc db 5432 </dev/null; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "-------- Calling migrate --------"
python manage.py migrate

>&2 echo "-------- Starting the server --------"
python manage.py runserver 0:8000
