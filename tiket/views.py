from datetime import datetime
from django.db.models.expressions import OrderBy
from django.forms.models import model_to_dict
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
import datetime
from . import models, forms
# Create your views here.
def index(req):
    home1 = models.Park.objects.all()
    data = []
    for h in home1:
        data.append(model_to_dict(h))    #=========> merubah array versi django menjadi array biasa
        for d in range(len(data)):          #======> memanggil values tertentu
            time = str(data[d]['dtg'])
            time2 = str(datetime.time(0, 0, 3, 0))
            frmt = '%H:%M:%S.%f'
            # diff = datetime.datetime.strptime(time2, frmt) + datetime.datetime.strptime(time, frmt)
            # tdelta = datetime.strptime(time, frmt) + datetime.strptime(time2, frmt)
            print(time)
    # print(data)
    return render(req, 'home/dashboard.html', {
        'data1' : home1,
        # 'data2' : home2,
    })

# def input_nopol(req):
#     if req.POST:
#         models.Park.objects.create(
#             nopol=req.POST['nopol'],
#             noblok=req.POST['noblok'],
#             harga=req.POST['harga'],
#             dtg=req.POST['dtg'],
#         )
#         return redirect('/')
#     data = models.Park.objects.all()
#     return render(req, 'tiket/input.html', {
#         'data' : data,
#     })
    
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
