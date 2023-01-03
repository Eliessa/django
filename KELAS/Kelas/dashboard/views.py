from django.shortcuts import render
from dashboard.forms import FormBarang
from dashboard.models import Barang, Transaksi, ItemModel
from django.shortcuts import render,HttpResponseRedirect,Http404
from rest_framework.parsers import JSONParser
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import ItemSerializer

@csrf_exempt
def ItemsView(request):
 
    if request.method == 'GET':
        items = ItemModel.objects.all()
        serializer = ItemSerializer(items, many =True)
        return JsonResponse(serializer.data, safe =False)
 
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer =ItemSerializer(data = data)
 
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status =201)
        return JsonResponse(serializer.errors,status = 400)

@csrf_exempt
def ItemView(request,nm):
    try: 
        item = ItemModel.objects.get(id = nm)
    except ItemModel.DoesNotExist:
        raise Http404('Not found')
 
    if request.method == 'GET':
        serializer = ItemSerializer(item)
        return JsonResponse(serializer.data)
 
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ItemSerializer(item,data =data)
 
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status =400)
 
    if request.method == "DELETE":
        item.delete()
        return HttpResponse(status =204)



def tambah_barang(request):
    form=FormBarang()
    konteks={
        'form':form,
    }
    return render(request, 'tambah_barang.html', konteks)

def  product(request):
    titlee="Product"
    trs=Transaksi.objects.all()
    konteks={
        'titel':titlee,
        'trs':trs,
    }
    return render(request,'product.html', konteks)
def Barang_view(request):
    barangs=Barang.objects.all()
    konteks={
        'barangs':barangs  
    }
    return render(request,'tampil_brg.html',konteks)

def trsn(request):
    trs=Transaksi.objects.all()
    konteks={
        'trs':trs
    }
    return render(request,'tampil_transaksi.html',konteks)
    
# Create your views here.
