# SIMPLE CRUD API WITH DJANGO REST FRAMEWORK
[Django REST framework](http://www.django-rest-framework.org/) is a powerful and flexible toolkit for building Web APIs.

## Requirements
- Pythton 3.6
- Django (1.10, 1.11, 2.0)
- Django REST Framework

## Installation
```
	pip install django
	pip install djangorestframework
```

## Structure
In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our application using the HTTP methods - GET, POST, PUT, DELETE. Endpoints should be logically organized around _collections_ and _elements_, both of which are resources.

In our case, we have one single resource, `movies`, so we will use the following URLS - `/movies/` and `/movies/<id>` for collections and elements, respectively:

Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`movies` | GET | READ | Get all movies
`movies/:id` | GET | READ | Get a single movie
`movies`| POST | CREATE | Create a new movie
`movies/:id` | PUT | UPDATE | Update a movie
`movies/:id` | DELETE | DELETE | Delete a movie

## Use
We can test the API using [curl](https://curl.haxx.se/) or [httpie](https://github.com/jakubroztocil/httpie#installation). Httpie is a user friendly http client that's written in Python. Let's install that.

You can install httpie using pip:
```
pip install httpie
```

First, we have to start up Django's development server.
```
	python manage.py runserver
```
Only authenticated users can use the API services, for that reason if we try this:
```
	http  http://127.0.0.1:8000/api/v1/movies/3
```
we get:
```
 {  "detail":  "Authentication credentials were not provided."  }
```
Instead, if we try to access with credentials:
```
	http -a root:root1234 http://127.0.0.1:8000/api/v1/movies/3
```
we get the movie with id = 3
```
{  "title":  "Avengers",  "genre":  "Superheroes",  "year":  2012,  "creator":  "admin"  }
```
The API have some restrictions:
-   The movies are always associated with a creator (user who created it).
-   Only authenticated users may create and see movies.
-   Only the creator of a movie may update or delete it.
-   Unauthenticated requests shouldn't have access.

### Commands
```
http -a root:root1234 http://127.0.0.1:8000/api/v1/movies/
http -a root:root1234 GET http://127.0.0.1:8000/api/v1/movies/3
http -a root:root1234 POST http://127.0.0.1:8000/api/v1/movies/ title="Ant Man and The Wasp" genre="Action" year=2018
http -a root:root1234 PUT http://127.0.0.1:8000/api/v1/movies/3 title="AntMan and The Wasp" genre="Action" year=2018
http -a root:root1234 DELETE http://127.0.0.1:8000/api/v1/movies/3
```
Finally, I provide a DB to make these tests.

