from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.urls import reverse

# Create your models here.
class User (AbstractUser):
    pass

