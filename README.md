# mada_crm

start guide:

1- clone the repository on your machine
2- change the credintils of the database on settings.py file
3- run the following commands:

'''
python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser
'''
and insert superuser info

then you run the server:
'''
python manage.py runserver
'''

go to localhost:8000/admin and create employees users and services

you are good to go

screenshots:
![login](https://github.com/diaa95/mada_crm/blob/master/screeshots/login.PNG)
![homePage](https://github.com/diaa95/mada_crm/blob/master/screeshots/home.PNG)
![addCustomer](https://github.com/diaa95/mada_crm/blob/master/screeshots/add_customer.PNG)
![editDeleteCustomer](https://github.com/diaa95/mada_crm/blob/master/screeshots/edit_cutomer.PNG)
![addStopServices](https://github.com/diaa95/mada_crm/blob/master/screeshots/add_stop_services.PNG)
