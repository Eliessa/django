from turtle import title
from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static
from dashboard.views import product, tambah_barang, Barang_view,trsn, ItemsView, ItemView
from dashboard.views import product

def coba1(request):
    return HttpResponse('Selamat Sore, selamat menangis')
def  coba2(request):
    titelnya="Home"
    konteks = {
        'titel':titelnya,
    }
    return render(request,'index.html', konteks)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    
    path ('items/', ItemsView),
    path('item/<int:nm>/', ItemView),
    path('product/', product),
    path('addbarang/', tambah_barang),
    path('Vbrg/',Barang_view, name = 'barang_uts'),
    path('Vbrg/vtrans/',trsn, name = 'trsn_uts'),
]
