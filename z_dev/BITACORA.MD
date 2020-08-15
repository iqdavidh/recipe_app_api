#Sitios usados

###Dependencias de python
https://pypi.org/

La version actual 
djangorestframework>=3.11.1


Docker Images
https://hub.docker.com


Vemos que la distribución es con Alpne
docker-compose run app sh -c "python --version"
docker-compose run app sh -c "cat /etc/os-release"


###Usar

####para reconstruir el contenedos con los cambios en DockerFiled y docker-compose

docker-compose build

####correr test
docker-compose run app sh -c "python manage.py test"

####correr test con flake8
docker-compose run --rm app sh -c "python manage.py test && flake8"


docker-compose run --rm app sh -c "python manage.py createsuperuser"

####crear una aplicacion
docker-compose run --rm app sh -c "python manage.py startapp user"

