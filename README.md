# mada_crm

start guide:

* clone the repository on your machine
* change the credintils of the database on settings.py file make sure to create mada_crm schema
* run the following commands:

```aidl
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
and insert superuser info

then you run the server:
```aidl
python manage.py runserver
```

go to localhost:8000/admin and create employees accounts and services

and you are good to go

**Screenshots:**

![login](https://github.com/diaa95/mada_crm/blob/master/screeshots/login.PNG)
![homePage](https://github.com/diaa95/mada_crm/blob/master/screeshots/home.PNG)
![addCustomer](https://github.com/diaa95/mada_crm/blob/master/screeshots/add_customer.PNG)
![editDeleteCustomer](https://github.com/diaa95/mada_crm/blob/master/screeshots/edit_cutomer.PNG)
![addStopServices](https://github.com/diaa95/mada_crm/blob/master/screeshots/add_stop_services.PNG)
