# SystemProject
pip install django-extensions
and add this in the install app of settings.py

INSTALLED_APPS = [
    'django_extensions'
]
Then run

python ./manage.py reset_db
Then run migrations again

python manage.py makemigrations
python manage.py migrate

Now, run migrations for your installed apps

python manage.py makemigrations your_app_name
python manage.py migrtate your_app_name

Done! See Your Database...