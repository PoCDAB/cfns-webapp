# pull official base image
FROM python:3.9.6-alpine3.13

# set work directory
WORKDIR /usr/src/cfnsapp

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONIOENCODING=UTF-8

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-client \
        postgresql-dev \
        gcc \
        python3-dev \
        musl-dev \
    && apk add --no-cache \
               --upgrade \
               --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing \
        geos \
        proj \
        gdal \
        binutils
 
 # setup python virtual envirment
RUN pip install pipenv
COPY Pipfile Pipfile.lock ./
RUN pipenv install

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

# docker image build -t python .
# docker container run -p 8000:8000 python

## INITIAL START: ##
# docker-compose up -d
# docker exec -it web python manage.py migrate
# docker exec -it web python manage.py createsuperuser