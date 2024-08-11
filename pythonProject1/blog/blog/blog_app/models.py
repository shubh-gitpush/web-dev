from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE) #authorisation superuser
    title=models.CharField(max_length=256)
    text=models.TextField()
    text2 = models.TextField()
    image=models.ImageField(upload_to ='uploads/',null=True, blank=True)
    image2 = models.ImageField(upload_to='uploads/',null=True, blank=True)
    video_file = models.FileField(upload_to='videos/',null=True, blank=True)
    create_date=models.DateTimeField(default=timezone.now)
    published_date=models.DateTimeField(blank=True,null=True)# either null or empty you can make
    def publish(self):
        self.published_date=timezone.now()
        self.save()


    def approve_comments(self):
        return self.comments.filter(approved_comments=True)
    def get_absolute_url(self):#always name it that
        return reverse('post_detail',kwargs={'pk':self.pk})#kwargs=key word argument
    #after creating a post go to detail page of that post for the primary key of the post you created

    def __str__(self):
        return self.title


class comment(models.Model):
    post=models.ForeignKey('blog_app.post',related_name='comments',on_delete=models.CASCADE)#connect with above class
    author =models.CharField(max_length=256)
    text=models.TextField()
    created_date=models.DateTimeField(default=timezone.now)
    approved_comment=models.BooleanField(default=False)
    def approve(self):
        self.approved_comment=True
        self.save()
    def get_absolute_url(self):
        return reverse('post_list')#homepage list of all the post
    def __str__(self):
        return self.text

class Reply(models.Model):
    Comment = models.ForeignKey(comment, related_name='replies', on_delete=models.CASCADE)
    author = models.CharField(max_length=256)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text



