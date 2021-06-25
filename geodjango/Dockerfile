# pull official base image
FROM python:alpine
#FROM ubuntu:20.04

RUN apk update && apk upgrade \
    && apk add postgresql-client \
        postgresql-dev \
        musl-dev \
        gcc \
        libxml2-dev \
        libxslt-dev \
        linux-headers \
        gettext-dev \
    && apk add --repository http://dl-cdn.alpinelinux.org/alpine/edge/main \
        libcrypto1.1 \
    # && apk add --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing \
    #     gdal \
    #     geos \
    #     proj4 \
    && apk add --no-cache \
               --upgrade \
               --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing \
        geos \
        proj \
        gdal \
        binutils \
    && pip install pipenv

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONIOENCODING=UTF-8


COPY docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]

# set work directory
WORKDIR /usr/src/app

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev build-base 

# install dependencies
RUN pip install --upgrade pip
#COPY ./installation.sh .
#RUN sh installation.sh
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .
