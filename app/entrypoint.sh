#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then 
    echo "waiting for postgresdb..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
        sleep 0.1
    done

    echo "PostgresSQL started"
fi

python manage.py migrate

exec gunicorn -w 2 django_geoloc.wsgi:application --bind 0.0.0.0:8000