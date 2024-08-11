from django.contrib import admin
from blog_app.models import Post,comment

# Register your models here.
admin.site.register(Post)
admin.site.register(comment)