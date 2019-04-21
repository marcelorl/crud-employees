# CRUD employees

Project to CRUD employees made with DRF

## tools

 - django
 - django rest
 - postgresql
 - docker
 - 

## installation

```
docker-compose up -d
docker-compose run restapi python manage.py migrate
docker-compose run restapi python manage.py createsuperuser
```

## usage

Then, the project will be available at http://localhost:8000 and you have the following features available:

Admin website -> http://localhost:8000/admin
CRUD API -> http://localhost:8000/api/employees