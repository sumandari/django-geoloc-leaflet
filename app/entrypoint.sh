#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
        sleep 0.1
    done

    echo "PostgreSQL started"
fi

#python manage.py flush --no-input
python manage.py migrate
# run manually after the containers spin up, like so
# $ docker-compose exec web python manage.py flush --no-input
# $ docker-compose exec web python manage,py migrate

exec "$@"
