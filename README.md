## Get started

1. Clone down the repo.
2. Download .env file and add it under `music_project` folder. Make sure the file name is `.env`.
3. Run command `python3 -m venv .venv` and `source .venv/bin/activate` to setup virtual environment.
4. Run command `pip install -r requirements.txt` to install the dependencies.
5. Run command `python manage.py makemigrations` and `python manage.py migrate`.
6. Run command `python manage.py createsuperuser` and follow prompt to create a superuser. Make sure you add some email address when make a superuser.
7. Run command `python manage.py runserver` to run the server.
8. Use the URL in the terminal and in the `api/music` path, checkout the app.
9. Run command `python manage.py test` to run unit test.
10. Docker instructions will be updated.
