FROM python:3.7.7-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev \
    && apk add --no-cache \
       --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing \
       --repository http://dl-cdn.alpinelinux.org/alpine/edge/main \
       gdal gdal-dev geos-dev \
    && apk add geoip

COPY ./requirements.txt .
RUN pip install --upgrade pip \
    && pip install -r requirements.txt \
    && pip install gunicorn
  
COPY . .

# collect static files
# RUN python manage.py collectstatic --noinput

RUN ["chmod", "+x", "entrypoint.sh"]
# RUN ["chmod", "+x", "wait-for-postgres.sh"]
ENTRYPOINT ["sh","entrypoint.sh"]
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
