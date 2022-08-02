from django.contrib import admin
from App.models import Customer
admin.site.site_header = "Login authentication Application"
# Register your models here.

admin.site.register(Customer)
