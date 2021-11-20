from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from app import models


def index(request):
    return redirect('/login')
    # return render(request, 'main/home.html')


def home(request):
    context = {
        'all_customers': models.Customer.objects.all()
    }
    return render(request, 'main/home.html', context)


def search(request):
    # print("********************", request.GET)
    users = models.search(request.GET)
    if users:
        context = {
            'all_customers': models.search(request.GET)
        }
    else:
        context = {
            'all_customers': None
        }
    return render(request, 'main/home.html', context)



def new_customer(request):
    context = {
        'customer': None
    }
    return render(request, 'main/add_or_edit_customer.html', context)

def edit_customer(request, customer_id):
    context = {
        'customer': models.Customer.objects.get(id=customer_id)
    }
    return render(request, 'main/add_or_edit_customer.html', context)


def add_or_update_customer(request, customer_id=None):
    if customer_id:
        models.update_customer(request.POST, customer_id)
    else:
        models.add_customer(request.POST)
    return redirect('/home')


def delete_customer(request, customer_id):
    models.delete_customer(customer_id)
    return redirect('/home')


def customer_services(request, customer_id):
    context = {
        "customer": models.Customer.objects.get(id=customer_id),
        "all_services": models.Service.objects.all()
    }
    return render(request, 'main/customer_services.html', context)


def add_service(request, customer_id, service_id):
    models.add_service(customer_id, service_id)
    return redirect(f'/services/{customer_id}')


def delete_service(request, customer_id, service_id):
    models.delete_service(customer_id, service_id)
    return redirect(f'/services/{customer_id}')


def service(request, service_id):
    pass
