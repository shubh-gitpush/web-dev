from django.shortcuts import render
from level_app.forms import UserForm,UserProfileInfoForm
# Create your views here.
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import logging
logger=logging.getLogger(__name__)
def index(request):
     return render(request,'new_app/index.html')
@login_required
def user_logout(request):
    logout(request)
    logger.info("Redirecting to index")
    return HttpResponseRedirect(reverse('index'))

def register(request):
     registered=False
     if request.method== "POST":
         #if it is posted by a html
         user_form=UserForm(data=request.POST)
         profile_form=UserProfileInfoForm(data=request.POST)

         if user_form.is_valid() and profile_form.is_valid():
             # If the forms (UserForm and UserProfileInfoForm) are valid, it saves the user and profile information to the database.
             user=user_form.save()
             user.set_password(user.password)
             user.save()
             profile=profile_form.save(commit=False)
             profile.user=user

             if 'profile_pic' in request.FILES:
                 profile.profile_pic=request.FILES['profile_pic']
             profile.save()
             registered=True
         else:
            print(user_form.errors,profile_form.errors)
     else:
         user_form=UserForm()
         profile_form=UserProfileInfoForm()
     return render(request,'new_app/registration.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})
#If the request method is not POST (e.g., GET request), it creates blank instances of the UserForm and UserProfileInfoForm.

def user_login(request):
    if request.method=='POST':#always put capital post both in html and python
        username=request.POST.get('username')#because name = username in login.html
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)

        if user:#if it is authenticated
          if user.is_active:
              login(request,user)
              return HttpResponseRedirect(reverse('index'))#send them back to homapage
          else:
              return HttpResponse("Account not available")
        else:
            logger.warning('someone tried to log in')
            print(f'username: {username}and password {password}')
            return HttpResponse('invalid login details ')

    else:
        return render(request,'new_app/login.html')

