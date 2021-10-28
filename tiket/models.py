from django.db import models
from datetime import date, datetime, time, timezone
import time
from django.db.models.fields import TimeField


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
    klr=models.TimeField(auto_now=True)
    harga=models.PositiveBigIntegerField(blank=False, null=False)

    # def waktu(self):
    #     if self.dtg + datetime.time(0,0,5,0):
    #         return self.harga + 500