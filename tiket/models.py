from django.db import models
from datetime import date, datetime, time, timezone
import time
from django.db.models.fields import TimeField
# from time import time

# Create your models here.
# class Harga(models.Model):
#     harga=models.IntegerField(blank=False)

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
    noblok=models.CharField(max_length=3, choices=NOBLOK, default='' )
    dtg=models.TimeField(auto_now=True)
    # klr=models.DateTimeField(auto_now=True, null=True, blank=True)
    harga=models.PositiveBigIntegerField(blank=False, null=False)
    # harga=models.ForeignKey(Harga, default='', blank=True, on_delete=models.CASCADE, related_name='biaya')

    # def biaya(self):
    #     if self.dtg + timedelta(hours=0, minutes=0, seconds=20):
    #         return self.harga + 500

    def biaya(self):
        x = self.dtg
        y = self.dtg+time()
        
        waktu = y - x
        print (waktu)