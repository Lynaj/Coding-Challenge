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
