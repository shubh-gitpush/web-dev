from django.urls import path
from level_app import views
app_name='new_app'
#it acts as a namespace to avoid conflict
urlpatterns=[
    path('', views.index, name='index'),
    path('register/',views.register,name='register'),
    path('user_login/', views.user_login, name='user_login'),

]
