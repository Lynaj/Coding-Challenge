# Coding-Challenge

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
"The challenge is to create a web app where users can send virtual money in the currencies of (EUR, USD, GBP) to each other."
	
## Technologies
* Django
* Django REST framework
* Vue.js
* Docker
* Nginx
	
## Setup
The entire project is containerized, so that in order to run it, 
one has to own Docker (https://www.docker.com/) software installed
To run this project, use following commands:

```
$ docker-compose build
$ docker-compose up 
```

The app is available at: 

```
http://localhost:8000/
```


## Test
```
docker-compose -f docker-compose-test.yml up
```

Reports:

  >Silk: http://localhost:8000/silk
  
  >Locust:
  http://127.0.0.1:8089
  
  >Jest:
  frontend > test > unit > coverage > src > index.html
  
  >Nightwatch:
  frontend > test > e2e > reports
  
  >Unittest ( django ):  
