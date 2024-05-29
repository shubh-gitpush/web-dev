import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','project_3.settings')#configure the settings
import django
django.setup()#setup the project settings
import random
from faker import Faker
from app_3.models import first_name,last_name,email

fakegen=Faker()

def populate(N=5):
    for entry in range(N):
        #fake data for entry
        fake_f_name=fakegen.first_name()
        fake_l_name = fakegen.last_name()
        fake_email = fakegen.email()
        #webpage entry
        f_name_entry=first_name.objects.get_or_create(f_name=fake_f_name)[0]
        l_name_entry = last_name.objects.get_or_create(l_name=fake_l_name)[0]
        mail_1=email.objects.get_or_create(email=fake_email)[0]
if __name__=='__main__':
    print('it was a success')
    populate(10)
    print("populate comple")

