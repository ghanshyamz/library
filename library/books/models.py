from django.db import models


class Books(models.Model):
    name = models.CharField(max_length=30)
    auther = models.CharField(max_length=30)
    

    def __str__(self):
        return self.name

