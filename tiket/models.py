from django.db import models
from django.db.models.deletion import CASCADE
# from time import time

# Create your models here.
class Blok(models.Model):
    noblok=models.CharField(default='', max_length=5)
    
class Park(models.Model):
    nopol=models.CharField(default='', max_length=10)

class Ket(models.Model):
    noblok=models.ForeignKey(Blok, on_delete=models.CASCADE, related_name='blok')
    dtg=models.TimeField(null=True, blank=True)
    klr=models.TimeField(null=True, blank=True)