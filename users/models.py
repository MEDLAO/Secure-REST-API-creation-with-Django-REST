from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):

    user_id = models.IntegerField(primary_key=True)  # id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    username = None

    USERNAME_FIELD = 'email'
