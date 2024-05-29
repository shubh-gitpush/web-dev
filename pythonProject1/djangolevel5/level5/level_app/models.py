from django.db import models
from django.contrib.auth.models import User


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    #
    portfolio_site = models.URLField(blank=True)
    #This defines a field to store a URL, which can be a link to the user's portfolio or personal website.
    profile_pic = models.ImageField(upload_to='profile', blank=True)
    #  This defines a field to store an image, which can be used for the user's profile picture.
    #upload_to='profile': This specifies the directory within the MEDIA_ROOT where the uploaded images will be stored. Images will be uploaded to MEDIA_ROOT/profile.
#blank=True: This makes the profile picture optional.
    def __str__(self):
        return self.user.username

# Create your models here.
