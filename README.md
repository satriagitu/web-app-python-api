# Description

This project is an example web application using Django Rest Framework to create a simple CRUD (Create, Read, Update, Delete) API for "Post" entities in a blog. Below are some steps to get started using this API.

## Installation

Install all the required dependencies by running:
```bash
pip install -r requirements.txt

## Run
Run server:

```bash
python manage.py runserver

or

```bash
python3 manage.py runserver

## Usage

Here are some available endpoints:

### Register User

```bash
curl --location 'localhost:8000/api/v1/auth/register/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username":"name",
    "password":"pass",
    "confirm_password":"pass",
    "email":"sani.gitu4@gmail.com",
    "first_name":"sani",
    "last_name":"gitu"
}'

```bash
curl --location 'localhost:8000/api/v1/auth/token/' \
--header 'Content-Type: application/json' \
--data '{
    "username":"user",
    "password":"pass"
}'

```bash
curl --location 'localhost:8000/api/v1/auth/token/refresh/' \
--header 'Content-Type: application/json' \
--data '{
    "refresh":"<refresh_token>"
}'

```bash
curl --location 'localhost:8000/api/v1/blog/post/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <access_token>' \
--data '{
    "title": "Post 14",
    "content": "Isi aja 14",
    "author": 1,
    "categories": [1]

```bash
curl --location --request GET 'localhost:8000/api/v1/blog/post/7/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <access_token>'

```bash
curl --location --request PATCH 'localhost:8000/api/v1/blog/post/update/7/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <access_token>' \
--data '{
    "title": "Updated Post 7"
}'

```bash
curl --location --request DELETE 'localhost:8000/api/v1/blog/post/delete/7/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <access_token>'

```bash
curl --location --request GET 'localhost:8000/api/v1/blog/post/list' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <access_token>'

