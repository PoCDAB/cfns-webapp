# CFNS webapp
Webapplication made in Django, with GeoDjango and as database: PostgreSQL extented with PostGIS

## (Easy method) Start up project (via Docker):
Go into linux (type 'wsl' in Windows)

	1. docker-compose up


## (Hard method) Start up project (via python):
#### Install required software:
Follow [installation.md](installation.md)

#### Activate environment:
Go into linux (type 'wsl' in Windows)

	1. source env/bin/activate

#### Update packages:
	1. pip3 install -r requirements.txt

#### Startup django project:
	1. python3 manage.py runserver

@Daniël Geerts, 2021