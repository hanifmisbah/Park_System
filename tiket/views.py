from datetime import datetime
from django.shortcuts import redirect, render

from . import models, forms
# Create your views here.

def index(req):
    home1 = models.Park.objects.all()
    return render(req, 'home/dashboard.html', {
        'data1' : home1,
    })
    # for d in home1:
    #     print(d[8])
    # print(home1)
    #     datawaktu = models.Park.objects.all()
    # def waktu(req):
    #         time = d
    #         print(time)
    
    # print(waktu)

    # if time + datetime.time(0,0,5,0):
    #     return home1.harga + 500
    # home2 = models.Harga.objects.all()

def input_nopol(req):
    form = forms.Park()
    if req.POST:
        form = forms.Park(req.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    data = models.Park.objects.all()
    return render(req, 'tiket/input.html', {
        'data' : data,
        'form' : form,
    })

def delete(req, id):
    models.Park.objects.filter(pk=id).delete()
    return redirect('/')

def login(req):
    return render(req, 'login/login.html')