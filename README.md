# aluxion
Aluxion technical test

API to get list of musicians and albums

# INSTALLATION
## Requirements
* Docker and docker-compose installed
* Create a .env file into root folder project. This file will be used to get environment variables.

### .env file  
DJANGO_DEBUG='True'  
DJANGO_ALLOWED_HOSTS='*'

## Run the container
To up the container just run on terminal:  
cd /dir/to/the/repo  
docker-compose up -d

Docker will start on localhost:8000

## Create superuser on database
To create superuser on database we need the docker container id.  
Execute: docker ps and copy ID from output.   
Then execute next:  
docker exec -it docker_container_id python manage.py createsuperuser

# E/R Diagram


# TESTING SERVICES
The services can be tested on browser on http://127.0.0.1:8000

## Musicians service
### Return list of all artists
GET /api/v1/artist/

### Return all albums from a given artist name
GET /api/v1/artist/artist-name/albums

## Albums service
### Return list of all albums with its tracks
GET /api/v1/album/

### Return tracks from a given album title
GET /api/v1/rooms/album-title

### Return list of all albums titles with artist name and total tracks as aggregate data
GET /api/v1/albums
