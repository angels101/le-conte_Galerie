serve:
	./manage.py runserver

migrate:		
	./manage.py migrate

migrations:	
	python manage.py makemigrations $(app)

collectstatic:
	./manage.py collectstatic

app:
	./manage.py startapp $(name)

superuser:
	./manage.py createsuperuser --usermake $(name)

app:
	./manage.py startapp $(name)
	  #django-admin startapp <name>

superuser:
	./manage.py createsuperuser --username $(name)