web: gunicorn manage:app
heroku ps:scale web=1
release: python manage.py db init
release: python manage.py db stamp head
release: python manage.py db migrate
release: python manage.py db upgrade