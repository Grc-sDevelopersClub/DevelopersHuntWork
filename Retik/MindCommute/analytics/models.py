from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Journal(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    headline = models.CharField(max_length = 150)
    content = models.TextField(max_length = 3000)
    created = models.DateTimeField(auto_now = True)
    modified = models.DateTimeField(auto_now_add = True)
