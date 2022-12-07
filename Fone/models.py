from django.db import models
from accounts.models import CustomUser
from django.urls import reverse

# Create your models here.
class Fone(models.Model):
    carName = models.CharField(max_length=255, default="Car Name")
    carModel = models.CharField(max_length=255, default="Car Model")
    carFactory = models.CharField(max_length=255, default="Factory")
    driver = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.carName

    def get_absolute_url(self):
        return reverse("Fone-list")
