# INSTAllATION GUIDE
GO GET A COUPLE CUPS OF COFFEE. THIS INSTALLATION MAY TAKE THE MAJORITY OF YOUR WORKDAY.

Blijf alert tijdens de installatie, zo af en toe vraagt de command prompt om uw wachtwoord in te voeren.

## First time installation

Go into linux (type 'wsl' in Windows)

	1. python3 -m venv env
	1. source env/bin/activate

### To install dos2unix
	sudo apt-get update
	sudo apt-get install dos2unix

### Linux (Ubuntu):
Go to the correct folder in the Linux command line.

	dos2unix installation.sh
	sh installation.sh

### WSL (Windows Subsystem for Linux (Ubuntu)):
Type in the (Linux) command line.

	wsl
	dos2unix installation.sh
	sh installation.sh

## Afterwards installation
### Create database
	sudo passwd postgres
	postgres
	su - postgres
	createdb gis_db
	psql gis_db
	CREATE EXTENSION postgis;
	\q
	exit

### Get into postgres and check databases
	su - postgres
	psql
	\du+
	\l+

### check postgresql (database) status
	service postgresql status

### migrate
	cd webapp/
	python3 manage.py makemigrations
	python3 manage.py makemigrations core
	python3 manage.py migrate

#### Make superuser
	python3 manage.py createsuperuser

> Username: admin
> Email: *name*@rws.nl
> Password: admin

### Run app
	python3 manage.py runserver
