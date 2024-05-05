from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class User (AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100,unique=True)
    last_name = models.CharField(max_length=100)
    username=models.CharField(max_length=25)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name"]
