from django.db import models


class Books(models.Model):
    name = models.CharField(max_length=30)
    auther = models.CharField(max_length=30)
    

    class Meta:
        verbose_name = _("")
        verbose_name_plural = _("s")

    def __str__(self):
        return self.name

