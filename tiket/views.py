from datetime import datetime
from django.shortcuts import redirect, render

from . import models, forms
# Create your views here.
def index(req):
    home1 = models.Park.objects.all()
    print(home1)
    time = 2
    for d in home1:
        # d.dtg
        # print(d.dtg)
        time+=1
        print(time)

    # if time + datetime.time(0,0,5,0):
    #     return home1.harga + 500
    print(time)
    return render(req, 'home/index1.html', {
        'data' : home1,
        # 'time' : time,
        # 'data2' : home2,
    })

def input_nopol(req):
    form = forms.Park()
    if req.POST:
        form = forms.Park(req.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    data = models.Park.objects.all()
    return render(req, 'tiket/index.html', {
        'data' : data,
        'form' : form,
    })

def delete(req, id):
    models.Park.objects.filter(pk=id).delete()
    return redirect('/')

# def input_harga(req):
#     form = forms.Harga()
#     if req.POST:
#         form = forms.Harga(req.POST)
#         if form.is_valid():
#             form.instance.owner = req.user
#             form.save()
#         return redirect('/')

#     data = models.Harga.objects.all()
#     return render(req, 'harga/index.html', {
#         'data' : data,
#         'form' : form,
#     })
