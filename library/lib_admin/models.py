from django.db import models
from django.contrib.auth.models import AbstractUser

class LibAdmin(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True, max_length=30)

    def __str__(self):
        return self.first_name + " " + self.last_name
