from django.db import models

from accounts.models import CustomUser


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    nickname = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    messenger_contact = models.CharField(max_length=100)