# Visit app

***

## Features

- Show retail outlets list bound to the transferred phone number
- Visit retail outlets

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
   git clone https://github.com/AndrewIsaev/visit_app.git
   
2. Install poetry and dependencies:
    ``` 
   pip install poetry
   poetry install

3. Create .env file:
   ```
   POSTGRES_PASSWORD=
   POSTGRES_USER=
   POSTGRES_DB=visit_app_db
   PGUSER=

   DB_USER=
   DB_PASSWORD=
   DB_HOST=
   DB_PORT=
   DB_NAME=visit_app_db


   SECRET_KEY=""
   DEBUG=

4. Run docker container with db
   ```
    docker-compose up

5. Make migrations
   ```
    python manage.py makemigration
    python manage.py migrate

6. Create superuser
   ```
    python manage.py createsuperuser

7. Run app
   ```
   python manage.py runserver

***

## Project structure

- `api/`: API for visit app
- `visit_app/`: Django settings
- `.env`: environment variables
- `.pre-commit-config.yaml`: pre-commit settings
- `docker-compose.yaml`: docker compose file for db
- `poetry.lock`: packages dependencies
- `pyproject.toml`: packages list
- `manage.py`: Django app management
