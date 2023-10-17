# Books library

Simple books library
***

## Features

- Registration/Authentication
- Books
    - Pagination for books list
    - Creating/changing/deleting books
    - Add comments for book
- Search books by title or author name
- API for list and detail books

***

## Technology stack

- Python 3.11
- Django 4.2.5
- Django REST Framework 3.14.0
- Poetry 1.5.1
- PostgreSQL
- Docker
- Docker-compose
- pre-commit
- black
- flake8
- mypy
- isort

***

## Start app

1. Clone repository:
    ```
   git clone
2. Create .env file:
   ```
   POSTGRES_PASSWORD=
   POSTGRES_USER=
   POSTGRES_DB=
   PGUSER=

   DB_USER=
   DB_PASSWORD=
   DB_HOST=
   DB_PORT=
   DB_NAME=


   SECRET_KEY=""
   DEBUG=

3. Run docker container with db
   ```
    docker-compose up

4. Make migrations
   ```
    python manage.py makemigration
    python manage.py migrate

5. Create superuser
   ```
    python manage.py createsuperuser

6. Run app
   ```
   python manage.py runserver

***

## Project structure

- `api/`: API for books list and detail
- `visit_app/`: Django settings
- `.env`: environment variables
- `.pre-commit-config.yaml`: pre-commit settings
- `docker-compose.yaml`: docker compose file for db
- `poetry.lock`: packages dependencies
- `pyproject.toml`: packages list
- `manage.py`: Django app management
