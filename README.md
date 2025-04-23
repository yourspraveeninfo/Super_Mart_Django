# Super_Mart_Django
#html #css #Bootstrap #python #mysql #django #authentication

1. py -m venv .venv
2. .venv/scripts/activate
3. pip install django 
4. pip install django-bootstrap-v5
5.pip install Pillow
6. pip install mysqlclient
7. DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'demo2',  #---------> change database name 
        'USER': 'root',
        'PASSWORD': '*******',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}
8. py manage.py makemigrations 
9. py manage.py migrate
10. py manage.py createsuperuser - username & password
11. py manage.py runserver
12. stop server
13. DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'demo2',  #---------> change database name 
        'USER': 'root',
        'PASSWORD': '******',
        'HOST': 'localhost',
        'PORT': '3306'
    }
  14. py manage.py runserver
  15. open website - login with created super user - username & password
  16. Add data in all customer , product, & orders
  17. open mysql workbench refer and check show all datas in every fields
}
