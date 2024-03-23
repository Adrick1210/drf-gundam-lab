from django.db import models

# Create your models here.
class MobileSuit(models.Model):
    name=models.CharField(max_length=100)
    serial=models.CharField()
    pilot=models.CharField(max_length=100)
    series=models.CharField(max_length=100)