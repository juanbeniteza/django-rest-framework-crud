

# Django REST Framework CRUD API

[Django REST framework](http://www.django-rest-framework.org/) is a powerful and flexible toolkit for building Web APIs.

## Requirements
- Python 3.6
- Django 3.1
- Django REST Framework

## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/roran-williams/django-rest-framework-crud.git
   cd django-rest-framework-crud

2. **Create a virtual environment:**
   ```bash
   python -m venv env
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```bash
     .\env\Scripts\activate
     ```
   - On Unix or MacOS:
     ```bash
     source env/bin/activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Apply migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Start the Django development server:**
   ```bash
   python manage.py runserver
   ```

7. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```
   To access the admin interface, visit:
   ```
   http://localhost:8000/admin
   ```

## API Structure
The API provides CRUD operations for a single resource, `blog`, with the following endpoints:

Endpoint | HTTP Method | CRUD Method | Result
-- | -- | -- | --
`blogs` | GET | READ | Get all blogs
`blogs/:id` | GET | READ | Get a single blog
`blogs` | POST | CREATE | Create a new blog
`blogs/:id` | PUT | UPDATE | Update a blog
`blogs/:id` | DELETE | DELETE | Delete a blog

## Usage
1. **Access the API endpoints:**
   - Use [curl](https://curl.haxx.se/) or [httpie](https://github.com/jakubroztocil/httpie#installation) or [Postman](https://www.postman.com/).
   - You can install httpie using pip:
        ```
        pip install httpie
        ```

2. **Authenticate users:**
   - Create a user:
     ```bash
     http POST "http://127.0.0.1:8000/api/roran-williams/auth/register/" email="email@email.com" username="USERNAME" password="PASSWORD" password2="PASSWORD"
     ```
   - Get a token:
     ```bash
     http "http://127.0.0.1:8000/api/roran-williams/auth/token/" username="username" password="password"
     ```
   After that, we get the token:
   ```json
   {
       "refresh": "YOUR_REFRESH_TOKEN",
       "access": "YOUR_ACCESS_TOKEN"
   }
   ```

4. **Use the obtained token in requests:**
   ```bash
   http "http://127.0.0.1:8000/api/roran-williams/blogs/" "Authorization: Bearer {YOUR_TOKEN}"
   ```

### Token Management
We got two tokens; the access token will be used to authenticate all the requests we need to make. This access token will expire after some time. We can use the refresh token to request a new access token.
- To refresh an access token:
  ```bash
  http "http://127.0.0.1:8000/api/roran-williams/auth/token/refresh/" refresh="{YOUR_REFRESH_TOKEN}"
  ```

### Commands
```bash
# Get all blogs
http "http://127.0.0.1:8000/api/roran-williams/blogs/" "Authorization: Bearer {YOUR_TOKEN}"

# Get a single blog
http GET "http://127.0.0.1:8000/api/roran-williams/blogs/{blog_id}/" "Authorization: Bearer {YOUR_TOKEN}"

# Create a new blog
http -f POST "http://127.0.0.1:8000/api/roran-williams/blogs/" "Authorization: Bearer {YOUR_TOKEN}" topic="blog" title="Ant Man and The Wasp" image@"path/to/your/image" content="Action blog" year=2018

# Full update a blog
http -f PUT "http://127.0.0.1:8000/api/roran-williams/blogs/{blog_id}/" "Authorization: Bearer {YOUR_TOKEN}" topic="new topic" title="new title" content="new content" year=2019

# Partial update a blog
http PATCH "http://127.0.0.1:8000/api/roran-williams/blogs/{blog_id}/" "Authorization: Bearer {YOUR_TOKEN}" title="new title"

http -f PATCH "http://127.0.0.1:8000/api/roran-williams/blogs/{blog_id}/" "Authorization: Bearer {YOUR_TOKEN}" image@"new/path/to/image"

# Delete a blog
http DELETE "http://127.0.0.1:8000/api/roran-williams/blogs/{blog_id}/" "Authorization: Bearer {YOUR_TOKEN}"
```

## Pagination
- The API supports pagination. Example:
  ```bash
  http "http://127.0.0.1:8000/api/roran-williams/blogs/?page=3" "Authorization: Bearer {YOUR_TOKEN}"
  ```

## Filters
- The API supports filtering. Examples:
  ```bash
  http "http://127.0.0.1:8000/api/roran-williams/blogs/"?title="AntMan and The Wasp" "Authorization: Bearer {YOUR_TOKEN}"
  http "http://127.0.0.1:8000/api/roran-williams/blogs/"?year=2020 "Authorization: Bearer {YOUR_TOKEN}"
  ```

## Contributing
Feel free to contribute to the project. Open a pull request or create issues if you encounter any problems.

## Issues
If you have any issues or questions, please open an issue on the GitHub repository.
```
