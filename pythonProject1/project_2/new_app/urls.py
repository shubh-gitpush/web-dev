from django.urls import path
from new_app import views
app_name='new_app'


urlpatterns=[
    path('',views.index,name='index'),
    path('url/',views.url,name='url'),
    path('other/',views.other,name='other'),

]