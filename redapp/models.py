from django.db import models


class UserProfile(models.Model):
    username = models.CharField(max_length=225, unique=True)
    password = models.CharField(max_length=225)
    email = models.EmailField(unique=True)
