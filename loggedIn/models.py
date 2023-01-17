# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser



# class CustomUser(AbstractBaseUser):
#     user_ptr = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True, parent_link=True)
#     Nationality = models.CharField(max_length=25, blank=True)
#     USERNAME_FIELD = 'username'
#     username = models.CharField(max_length=150, unique=True)

