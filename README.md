# SIMPLE CRUD API WITH DJANGO REST FRAMEWORK
[Django REST framework](http://www.django-rest-framework.org/) is a powerful and flexible toolkit for building Web APIs.

## Requirements
- Python 3.6
- Django 3.1
- Django REST Framework

## Installation
After you cloned the repository, you want to create a virtual environment, so you have a clean python installation.
You can do this by running the command
```
python -m venv env
```

After this, it is necessary to activate the virtual environment, you can get more information about this [here](https://docs.python.org/3/tutorial/venv.html)

You can install all the required dependencies by running
```
pip install -r requirements.txt
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
We can test the API using [curl](https://curl.haxx.se/) or [httpie](https://github.com/jakubroztocil/httpie#installation), or we can use [Postman](https://www.postman.com/)

Httpie is a user-friendly http client that's written in Python. Let's try and install that.

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
http  http://127.0.0.1:8000/api/v1/movies/
```
we get:
```
{
    "detail": "Authentication credentials were not provided."
}
```
Instead, if we try to access with credentials:
```
http http://127.0.0.1:8000/api/v1/movies/3 "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE2MjA4Mjk1LCJqdGkiOiI4NGNhZmMzMmFiZDA0MDQ2YjZhMzFhZjJjMmRiNjUyYyIsInVzZXJfaWQiOjJ9.NJrs-sXnghAwcMsIWyCvE2RuGcQ3Hiu5p3vBmLkHSvM"
```
we get the movie with id = 3
```
{  "title":  "Avengers",  "genre":  "Superheroes",  "year":  2012,  "creator":  "admin"  }
```

## Create users and Tokens

First we need to create a user, so we can log in
```
http POST http://127.0.0.1:8000/api/v1/auth/register/ email="email@email.com" username="USERNAME" password1="PASSWORD" password2="PASSWORD"
```

After we create an account we can use those credentials to get a token

To get a token first we need to request
```
http http://127.0.0.1:8000/api/v1/auth/token/ username="username" password="password"
```
after that, we get the token
```
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxNjI5MjMyMSwianRpIjoiNGNkODA3YTlkMmMxNDA2NWFhMzNhYzMxOTgyMzhkZTgiLCJ1c2VyX2lkIjozfQ.hP1wPOPvaPo2DYTC9M1AuOSogdRL_mGP30CHsbpf4zA",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE2MjA2MjIxLCJqdGkiOiJjNTNlNThmYjE4N2Q0YWY2YTE5MGNiMzhlNjU5ZmI0NSIsInVzZXJfaWQiOjN9.Csz-SgXoItUbT3RgB3zXhjA2DAv77hpYjqlgEMNAHps"
}
```
We got two tokens, the access token will be used to authenticated all the requests we need to make, this access token will expire after some time.
We can use the refresh token to request a need access token.

requesting new access token
```
http http://127.0.0.1:8000/api/v1/auth/token/refresh/ refresh="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxNjI5MjMyMSwianRpIjoiNGNkODA3YTlkMmMxNDA2NWFhMzNhYzMxOTgyMzhkZTgiLCJ1c2VyX2lkIjozfQ.hP1wPOPvaPo2DYTC9M1AuOSogdRL_mGP30CHsbpf4zA"
```
and we will get a new access token
```
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE2MjA4Mjk1LCJqdGkiOiI4NGNhZmMzMmFiZDA0MDQ2YjZhMzFhZjJjMmRiNjUyYyIsInVzZXJfaWQiOjJ9.NJrs-sXnghAwcMsIWyCvE2RuGcQ3Hiu5p3vBmLkHSvM"
}
```


The API has some restrictions:
-   The movies are always associated with a creator (user who created it).
-   Only authenticated users may create and see movies.
-   Only the creator of a movie may update or delete it.
-   The API doesn't allow unauthenticated requests.

### Commands
```
Get all movies
http http://127.0.0.1:8000/api/v1/movies/ "Authorization: Bearer {YOUR_TOKEN}" 
Get a single movie
http GET http://127.0.0.1:8000/api/v1/movies/{movie_id}/ "Authorization: Bearer {YOUR_TOKEN}" 
Create a new movie
http POST http://127.0.0.1:8000/api/v1/movies/ "Authorization: Bearer {YOUR_TOKEN}" title="Ant Man and The Wasp" genre="Action" year=2018 
Full update a movie
http PUT http://127.0.0.1:8000/api/v1/movies/{movie_id}/ "Authorization: Bearer {YOUR_TOKEN}" title="AntMan and The Wasp" genre="Action" year=2018
Partial update a movie
http PATCH http://127.0.0.1:8000/api/v1/movies/{movie_id}/ "Authorization: Bearer {YOUR_TOKEN}" title="AntMan and The Wasp" 
Delete a movie
http DELETE http://127.0.0.1:8000/api/v1/movies/{movie_id}/ "Authorization: Bearer {YOUR_TOKEN}"
```

### Pagination
The API supports pagination, by default responses have a page_size=10 but if you want change that you can pass through params page_size={your_page_size_number}
```
http http://127.0.0.1:8000/api/v1/movies/?page=1 "Authorization: Bearer {YOUR_TOKEN}"
http http://127.0.0.1:8000/api/v1/movies/?page=3 "Authorization: Bearer {YOUR_TOKEN}"
http http://127.0.0.1:8000/api/v1/movies/?page=3&page_size=15 "Authorization: Bearer {YOUR_TOKEN}"
```

### Filters
The API supports filtering, you can filter by the attributes of a movie like this
```
http http://127.0.0.1:8000/api/v1/movies/?title="AntMan" "Authorization: Bearer {YOUR_TOKEN}"
http http://127.0.0.1:8000/api/v1/movies/?year=2020 "Authorization: Bearer {YOUR_TOKEN}"
http http://127.0.0.1:8000/api/v1/movies/?year__gt=2019&year__lt=2022 "Authorization: Bearer {YOUR_TOKEN}"
http http://127.0.0.1:8000/api/v1/movies/?genre="Action" "Authorization: Bearer {YOUR_TOKEN}"
http http://127.0.0.1:8000/api/v1/movies/?creator__username="myUsername" "Authorization: Bearer {YOUR_TOKEN}"
```

You can also combine multiples filters like so
```
http http://127.0.0.1:8000/api/v1/movies/?title="AntMan"&year=2020 "Authorization: Bearer {YOUR_TOKEN}"
http http://127.0.0.1:8000/api/v1/movies/?year__gt=2019&year__lt=2022&genre="Action" "Authorization: Bearer {YOUR_TOKEN}"
```

