# Description

This project is an example web application using Django Rest Framework to create a simple CRUD (Create, Read, Update, Delete) API for "Post" entities in a blog. Below are some steps to get started using this API.

## Installation

Install all the required dependencies by running:


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
