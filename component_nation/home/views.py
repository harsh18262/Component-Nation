from django.shortcuts import render
from django.http import HttpResponse
from .models import Prebuilt_70k,Prebuilt_80k,Prebuilt_90k,Prebuilt_1L
from update_prices import *
import re
# Create your views here.
def home(request):
    return render(request,'home/index.html')

def about(request):
    
    return render(request,'home/about.html')

def contact(request):
    
    return render(request,'home/contact.html')

def desktop(request):

    data70k=Prebuilt_70k.objects.all()
    data80k=Prebuilt_80k.objects.all()
    data90k=Prebuilt_90k.objects.all()
    data1l=Prebuilt_1L.objects.all()
    t70=total(data70k)
    t80=total(data80k)
    t90=total(data90k)
    # t1=total(data1l)


    return render(request,'home/desktop.html',{'data70k':data70k,'data80k':data80k,'data90k':data90k,'data1l':data1l,'t70':t70,'t80':t80})

def update(request):

   
    data70k=Prebuilt_70k.objects.all()
    data80k=Prebuilt_80k.objects.all()
    data90k=Prebuilt_90k.objects.all()
    data1l=Prebuilt_1L.objects.all()
    

    price=fetch_prices(data70k)
    i=0
    for item in data70k:
        item.price=price[i]
        i+=1
        item.save()
    price=fetch_prices(data80k)
    i=0
    for item in data80k:
        item.price=price[i]
        i+=1
        item.save()
    price=fetch_prices(data90k)
    i=0
    for item in data90k:
        item.price=price[i]
        i+=1
        item.save()
    return render(request,'home/update.html')


def temp(request):
    
    return render(request,'home/temp.html')






