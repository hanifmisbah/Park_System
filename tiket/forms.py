from django.forms import ModelForm
from . import models

class Park(ModelForm):
    class Meta:
        model=models.Park
        exclude=['dtg']

# class Harga(ModelForm):
#     class Meta:
#         model=models.Harga
#         exclude=[]