from django.db import models
from datetime import date, datetime, time, timezone
import time
from django.db.models.fields import TimeField
# from time import time

# Create your models here.
class Blok(models.Model):
    noblok=models.CharField(max_length=3)

    def __str__(self):
        return self.noblok

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
    noblok=models.CharField(max_length=3, choices=NOBLOK, default=NOBLOK)
    # noblok=models.ForeignKey(Blok, on_delete=models.CASCADE, related_name='blok')
    dtg=models.TimeField(default=datetime.now)
    # klr=models.DateTimeField(auto_now=True, null=True, blank=True)
    harga=models.PositiveBigIntegerField(blank=False, null=False)

    def __str__(self):
        return self.nopol, self.noblok, self.dtg

    def biaya(self):
        return self.harga

