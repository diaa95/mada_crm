from django.contrib import admin
from .models import Service, Customer
from django.contrib.auth.models import Group

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc')
admin.site.site_header = "Mada CRM"
admin.site.register(Service, ServiceAdmin)
admin.site.register(Customer)
admin.site.unregister(Group)
