from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import Q


class Service(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    desc = models.TextField(null=True)
    uploaded_by = models.ForeignKey(User,
                                    related_name="uploaded_by",
                                    on_delete=models.CASCADE)


class Customer(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=24)
    last_name = models.CharField(max_length=24)
    address = models.CharField(max_length=64)
    services = models.ManyToManyField(Service,
                                      related_name="customers")


def search(info):
    return Customer.objects.filter(Q(first_name__icontains=info['search']) |
                                   Q(last_name__icontains=info['search']))


def add_customer(info):
    new_customer = Customer.objects.create(
        first_name=info['f_name'],
        last_name=info['l_name'],
        address=info['address'])
    return new_customer


def update_customer(info, customer_id):
    customer = Customer.objects.get(id=customer_id)
    if info['f_name']:
        customer.first_name = info['f_name']
    if info['l_name']:
        customer.last_name = info['l_name']
    if info['address']:
        customer.address = info['address']
    customer.save()


def delete_customer(customer_id):
    Customer.objects.get(id=customer_id).delete()
    return


def add_service(customer_id, service_id):
    Customer.objects.get(id=customer_id).services.add(Service.objects.get(id=service_id))


def delete_service(customer_id, service_id):
    Customer.objects.get(id=customer_id).services.remove(Service.objects.get(id=service_id))






