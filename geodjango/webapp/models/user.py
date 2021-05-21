from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    id = models.AutoField(primary_key=True)

    username = models.CharField(
        max_length=128,
        unique = True,
    )

    email = models.EmailField(
        max_length=256,
        unique = True,
    )

    password = models.CharField(
        max_length=128,
    )

    firstname = models.CharField(
        max_length=128,
    )

    lastname = models.CharField(
        max_length=128
    )

    organisation = models.CharField(
        max_length=128
    )

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
