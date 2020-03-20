Django Geolocation using POSTGIS

---
installation
- brew install psql
- brew install gdal
- brew install libgeoip

or using docker image -> kartoza postgis https://hub.docker.com/r/kartoza/postgis/ 

--
create database postgis and create extension postgis

--
- create venv
python3 -m venv venv

- activate venv
. venv/bin/activate

- install module
pip install -r requirements.txt