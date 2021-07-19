# pull official base image
FROM python:3.9.6-alpine3.13

# Add packages for the Postgresql extend POSTGIS; library
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
    && apk add --no-cache \
               --upgrade \
               --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing \
        geos \
        proj \
        gdal \
        binutils

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONIOENCODING=UTF-8

# set work directory
WORKDIR /usr/src/app

# setup python virtual envirment
RUN pip install pipenv
COPY Pipfile Pipfile.lock ./
RUN pipenv install

# install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

#RUN ["python3", "manage.py", "collectstatic", "--no-input"]
#RUN ["python3", "manage.py", "migrate"]
#CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

# docker image build -t python .
# docker container run -p 8000:8000 python