from django.forms import ModelForm
from . import models

class Park(ModelForm):
    class Meta:
        model=models.Park
        exclude=['dtg']

    def __init__(self, *args, **kwargs):
        super(Park, self).__init__(*args, **kwargs)
        self.fields['nopol'].widget.attrs['class'] = 'form-control'
        self.fields['noblok'].widget.attrs['class'] = 'form-control'
        self.fields['harga'].widget.attrs['class'] = 'form-control'

# class Harga(ModelForm):
#     class Meta:
#         model=models.Harga
#         exclude=[]