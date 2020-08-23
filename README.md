# Django-Geoloc with docker-compose

## Prerequisites
- Git
- Docker

## Stacks
- docker compose
- python3
      - django
      - django-bootstrap
      - django-geojson
      - django-leaflet
      - gunicorn
- nginx
- postGIS

## Download and use source code from github
Clone code to your local machine and go to the directory
```
$ git clone https://github.com/sumandari/django-geoloc-leaflet.git
$ cd django-geoloc-leaflet
```

if you want to running with your native system (without docker), checkout git tag

```
$ git checkout tags/v0.0
```

---
### Development environment

Build and spin up docker-compose

```
$ docker-compose up -d --build
```

### Production environment

1. Build and spin up docker-compose using additional Compose file with -f option
2. Migrate database
3. Collect staticfiles

```
$ docker-compose -f docker-compose.prod.yml up -d --build
$ docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
$ docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
```

4. Create superuser to access admin page
```
$ docker-compose -f docker-compose.prod.yml exec web python manage.py createsuperuser
```

test your web, open [http://localhost:1337](http://localhost:1337) in your web browser

if your web doesn't work (OMG!), check the log from container

```
$ docker-compose -f docker-compose.prod.yml logs
```

explore running web container
```
$ docker-compose -f docker-compose.prod.yml exec web sh 
```

----
<a href="https://www.youtube.com/watch?v=XDxX80O2b5Q
" target="_blank"><img src="http://img.youtube.com/vi/XDxX80O2b5Q/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>