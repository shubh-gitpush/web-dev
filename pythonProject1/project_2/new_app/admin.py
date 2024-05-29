from django.contrib import admin
from new_app.models import Record,Topic,webpage
# Register your models here.
admin.site.register(Record)#registers all te models which were created in models.py
admin.site.register(Topic)
admin.site.register(webpage)