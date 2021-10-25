from django.db import models
from datetime import datetime
# from time import time

# Create your models here.
class Harga(models.Model):
    harga=models.IntegerField()

class Park(models.Model):
    nopol=models.CharField(default='', max_length=10)
    NOBLOK = [
        ( 'A1', 'A1'),
        ( 'A2', 'A2'),
        ( 'A3', 'A3'),
        ( 'B1', 'B1'),
        ( 'B2', 'B2'),
        ( 'B3', 'B3'),
    ]
    noblok=models.CharField(max_length=3, choices=NOBLOK, default='', null=True, blank=True)
    dtg=models.TimeField(default=datetime.now)
    # klr=models.DateTimeField(auto_now=True, null=True, blank=True)
    harga=models.ForeignKey(Harga, on_delete=models.CASCADE, related_name='biaya')

    def __repr__(self):
        return self.harga