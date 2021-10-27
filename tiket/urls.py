from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('nopol/', views.input_nopol),
    # path('harga/', views.input_harga),
    path('<id>/hapus/', views.delete),
]