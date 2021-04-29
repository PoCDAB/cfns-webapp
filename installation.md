# CFNS webapp
Webapplication made in Django, with GeoDjango and as database: PostgreSQL extented with PostGIS. This MarkDown file will help with the required software installation of this project.

GO GET A COUPLE CUPS OF COFFEE. THIS INSTALLATION MAY TAKE THE MAJORITY OF YOUR WORKDAY.

## First time installation
### Linux (Ubuntu):
Go to correct folder in Linux command line.

	dos2unix installation.sh
	sh installation.sh

### WSL (Windows Subsystem for Linux (Ubuntu)):
Type in (Linux) command line.

	wsl
	dos2unix installation.sh
	sh installation.sh

## Afterwards installation
### Create database
	sudo passwd postgres
	su - postgres
	createdb gis_db
	psql gis_db
	\du
	CREATE EXTENSION postgis;
	\q
	exit

### Get into postgres and check databases
	su - postgres
	psql
	\du+
	\l+

### Make superuser
	python3 manage.py createsuperuser

> Username: admin
> Email: daniel.geerts@rws.nl
> Password: admin

### Run app
	python3 manage.py runserver