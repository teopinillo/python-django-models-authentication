from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class User (AbstractUser):
    pass

class BlogPost (models.Model):
    title = models.CharField ( max_length = 200, unique= True)
    author = models.ForeignKey (settings.AUTH_USER_MODEL, related_name="post", on_delete=models.CASCADE)
    body = models.TextField()
    postdate = models.DateTimeFiled(auto_now_add=True, blank=True)

    def __str__(self):
        self.title