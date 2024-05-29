import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','project_2.settings')#configure the settings
import django
django.setup()#setup the project settings
import random
from faker import Faker
from new_app.models import webpage,Topic,Record




#fake pop script
fakegen=Faker()
Topics=['search','social','market','news','games']

def add_topic():
    t=Topic.objects.get_or_create(top_name=random.choice(Topics))[0]
    #it will add topic randomly from topics list it wiil either create or get the topic
    t.save()
    return t
def populate(N=5):
    for entry in range(N):
        #topic of entry
        top=add_topic()
        #fake data for entry
        fake_url=fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()
        #webpage entry
        web=webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]
        Rec=Record.objects.get_or_create(name=web,date=fake_date)[0]

if __name__=='__main__':
    print('populating script')
    populate(20)
    print('populating complete')
