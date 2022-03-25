## Get started

### Lab 32 - Django Permissions & Postgresql

**note**: this lab is only meant to work on container.

1. Clone down the repo from main branch.
2. Download .env file and add it under `root` folder. Make sure the file name is `.env`.
3. Run command `docker-compose up` to start the container.
4. Run command `docker-compose run web python manage.py migrate` to migrate.
5. Run command `docker-compose run web python manage.py createsuperuser` to create a superuser.
6. Checkout the app at `http://0.0.0.0:8000/api/music/`

### Lab 31 - Django REST Framework / Docker

1. Clone down the repo from django-rest branch.
2. Download .env file and add it under `music_project` folder and `root` folder. Make sure its under both folder, one is for local and the other one is for docker. Make sure the file name is `.env`.
3. Run command `python3 -m venv .venv` and `source .venv/bin/activate` to setup virtual environment.
4. Run command `pip install -r requirements.txt` to install the dependencies.
5. Run command `python manage.py makemigrations` and `python manage.py migrate`.
6. Run command `python manage.py createsuperuser` and follow prompt to create a superuser. Make sure you add some email address when make a superuser.
7. Run command `python manage.py runserver` to run the server.
8. Use the URL in the terminal and in the `api/music` path, checkout the app.
9. Run command `python manage.py test` to run unit test.
10. For running on the docker, run command `docker-compose up` and checkout the app at `http://0.0.0.0:8000/api/music/`
