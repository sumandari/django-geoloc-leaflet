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
- CREATE DATABASE djangogis;
- CREATE EXTENSION postgis;

create user and password
- \c djangogis
- CREATE USER admingis WITH PASSWORD 'qwerty123456'

---
create venv
- python3 -m venv venv

activate venv
- venv/bin/activate

install module
- pip install -r requirements.txt

run django
- python manage.py runserver

----
<a href="https://www.youtube.com/watch?v=zytRMB_S1tg
" target="_blank"><img src="http://img.youtube.com/vi/zytRMB_S1tg/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>