from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    headline = models.CharField(max_length = 100)
    description = models.TextField(max_length = 500)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    created = models.DateTimeField(auto_now_add = True )
    modified = models.DateTimeField(auto_now = True)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    created = models.DateTimeField(default = now)
    modified = models.DateTimeField(default = now)
    reply = models.ForeignKey('self', on_delete = models.CASCADE, null = True, related_name = 'replies', blank = True)
