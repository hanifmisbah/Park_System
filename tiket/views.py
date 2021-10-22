from django.shortcuts import redirect, render

from . import models, forms
# Create your views here.
def index(req):
    home = models.Blok.objects.all()
    home1 = models.Park.objects.all()
    home2 = models.Ket.objects.all()
    return render(req, 'home/index.html', {
        'data' : home,
        'data1' : home1,
        'data2' : home2,
    })

def input_nopol(req):
    # form_input = forms.Park()

    if req.POST:
        models.Park.objects.create(
            nopol=req.POST['nopol']
        )
    # if req.POST:
    #     form_input = forms.Park(req.POST)
    #     if form_input.is_valid():
    #         form_input.save()
        return redirect('/')

    data = models.Park.objects.all()
    datablok = models.Blok.objects.all()
    return render(req, 'tiket/index.html', {
        'data' : data,
        'datablok' : datablok,
        # 'form' : form_input,
    })

def input_noblok(req):
    if req.POST:
        models.Blok.objects.create(
            noblok=req.POST['noblok']
        )
        return redirect('/')

    data = models.Blok.objects.all()
    return render(req, 'blok/index.html', {
        'data' : data,
        # 'form' : form_input,
    })
