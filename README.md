# CRUD employees

Project to CRUD employees made with DRF

## tools

 - django
 - django rest
 - postgresql
 - docker

## installation

Make sure you have docker installed, then run in the root folder:

```
$ docker-compose up -d
$ docker-compose run restapi python manage.py migrate
$ docker-compose run restapi python manage.py createsuperuser
```

## usage

The project will be available at http://localhost:8000 and you have the following features available as required:

### admin website
 - http://localhost:8000/admin

### crud api
 - http://localhost:8000/api/employees/
