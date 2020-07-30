# Django-Geoloc with docker-compose

## Requirement
- Docker

if you want to running with your native system (without docker), checkout git to commit sha

```
$ git checkout 706ee03
```

---
#### Build containers with docker-compose build
```
$ docker-compose -f docker-compose.prod.yml build
```

##### Run the containers with dicker-compose up
```
$ docker-compose -f docker-compose.prod.yml up -d
```

#### migrate model to database from running web container
```
$ docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
```

#### collect staticfiles from running web container
```
$ docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --noinput
```

#### collect staticfiles from running web container
```
$ docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --noinput
```

#### create superuser to access admin page
```
$ docker-compose -f docker-compose.prod.yml exec web python manage.py createsuperuser
```

test your web, open [http://localhost:1337](http://localhost:1337) in your web browser

if your web doesn't work (OMG!), check the log from container

```
$ docker-compose -f docker-compose.prod.yml logs
```

----
<a href="https://www.youtube.com/watch?v=XDxX80O2b5Q
" target="_blank"><img src="http://img.youtube.com/vi/XDxX80O2b5Q/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>