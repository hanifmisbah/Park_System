from django.forms import ModelForm
from . import models

class Blok(ModelForm):
    class Meta:
        model=models.Blok
        exclude=[]

class Park(ModelForm):
    class Meta:
        model=models.Park
        exclude=[]