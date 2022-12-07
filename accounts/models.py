from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    phoneNumber = models.CharField(max_length=64, default=True)

    def __str__(self):
        return self.email
