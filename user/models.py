from django.contrib.auth.models import User
from django.db import models

class ClientIntake(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    company = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name
