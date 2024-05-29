from django import forms
from django.contrib.auth.models import User
from .models import UserProfileInfo

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
     #models.Model: Base class for all models
    class Meta():
        #This inner class is used to provide metadata to the form. The Meta class defines which model is associated with the form and which fields from that model should be included in the form.
        model =User
        #This line within the Meta class specifies that the form is associated with the User model. This tells Django to use the User model to create the form fields.
        fields=('username','email','password')
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
       model = UserProfileInfo
       fields=('portfolio_site','profile_pic')
       #This specifies the fields from the UserProfileInfo model that should be included in the form. Here, the form will include fields for portfolio_site and profile_pic