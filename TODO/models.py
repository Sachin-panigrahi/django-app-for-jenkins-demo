from django.db import models

# Create your models here.


class Tasks(models.Model):
    name=models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    status = models.CharField(max_length=6)