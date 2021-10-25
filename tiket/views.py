from django.shortcuts import redirect, render

from . import models, forms
# Create your views here.
def index(req):
    home1 = models.Park.objects.all()
    return render(req, 'home/index1.html', {
        'data1' : home1,
    })

def input_nopol(req):
    form = forms.Park()
    if req.POST:
        form = forms.Park(req.POST)
        if form.is_valid():
            form.instance.owner = req.user
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