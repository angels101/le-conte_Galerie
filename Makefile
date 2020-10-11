serve:
	 ./manage.py runserver

 migrate:		
 	./manage.py migrate

 migrations:	python manage.py makemigrations $(app)

 collectstatic:	./manage.py collectstatic

 app:	./manage.py startapp $(name)

 