all: makemigrations migrate run

run: 
	python manage.py runserver

makemigrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

admin:
	python manage.py createsuperuser
