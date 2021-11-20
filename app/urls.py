from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('home/', views.home),
    path('home/search', views.search),
    path('new_customer', views.new_customer),
    path('edit_customer/<customer_id>', views.edit_customer),
    path('update_customer/<customer_id>', views.add_or_update_customer),
    path('add_customer', views.add_or_update_customer),
    path('delete_customer/<customer_id>', views.delete_customer),
    path('services/<customer_id>', views.customer_services),
    path('add_service/<customer_id>/<service_id>', views.add_service),
    path('delete_service/<customer_id>/<service_id>', views.delete_service),
    path('service/<service_id>', views.service),
]
