from django.db import models

# Create your models here.

class first_name(models.Model):
    f_name = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.f_name

class last_name(models.Model):
    l_name = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.l_name

class email(models.Model):
    email=models.EmailField(max_length=254,unique=True)
    def __str__(self):
        return self.email
