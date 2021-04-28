# CFNS webapp
Webapplication made in Django, with GeoDjango and as database: PostgreSQL extented with PostGIS

## Install required software:
Follow [installation.md](installation.md)

## Start up project:
#### Activate environment:
Go into linux (type 'wsl' in Windows)

	1. python3 -m venv env
	2. source env/bin/activate

#### Update packages:
	1. pip install -r requirements.txt

#### Startup django project:
	1. python manage.py runserver

## Docker:
#### Docker start:
	docker-composer up -d --build

or

	docker-compose build
	docker-compose up -d
	docker exec -t -i **CONTAINER_ID** bash

#### Running containers:
	docker ps

#### Existing images:
	docker images

#### Docker kill all commands:
	docker stop $(docker ps -aq)
	docker stop $(docker images -aq)
	docker rm $(docker ps -aq)
	docker rmi $(docker images -q)
