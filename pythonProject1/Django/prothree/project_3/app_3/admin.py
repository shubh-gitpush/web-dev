from django.contrib import admin
from app_3.models import email,first_name,last_name
# Register your models here.
admin.site.register(last_name)#registers all te models which were created in models.py
admin.site.register(first_name)
admin.site.register(email)
# Register your models here.
