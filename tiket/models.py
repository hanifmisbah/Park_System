from django.db import models
from datetime import date, datetime, time, timedelta, timezone
from django.utils.timezone import utc
import datetime


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
    #     if self.dtg + (self.dtg + datetime.timedelta(time(0,0,2,0))):
    #         return self.harga + 500
    # def waktu(self):
    #     if self.dtg:
    #         now = datetime.datetime.utcnow().replace(tzinfo=utc)
    #         timediff = now - self.dtg
    #         return timediff.total_seconds()