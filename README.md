Django Geolocation using POSTGIS

---
installation on macOS
- brew install psql
- brew install gdal
- brew install libgeoip

or using docker image -> kartoza postgis https://hub.docker.com/r/kartoza/postgis/ 

---
go to psql CLI:
- psql

create database postgis and create extension postgis
- postgres# CREATE DATABASE djangogis;
- postgres# CREATE EXTENSION postgis;

create user and password
- postgres# \c djangogis
- postgres# CREATE USER admingis WITH PASSWORD 'qwerty123456'

---
create venv
- python3 -m venv venv

activate venv
- venv/bin/activate

install module
- pip install -r requirements.txt

migration db
- python manage.py makemigrations
- python manage.py migrate

create superuser
- python manage.py createsuperuser

run django
- python manage.py runserver

---
run test

Create database superuser, alter the user’s role from the SQL shell
- postgres# ALTER ROLE admingis SUPERUSER

run test in terminal
- python manage.py test

----
<a href="https://www.youtube.com/watch?v=XDxX80O2b5Q
" target="_blank"><img src="http://img.youtube.com/vi/XDxX80O2b5Q/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>