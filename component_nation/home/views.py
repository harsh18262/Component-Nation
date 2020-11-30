from django.shortcuts import render
from django.http import HttpResponse
# from .models import Prebuilt_70k,Prebuilt_80k,Prebuilt_90k,Prebuilt_1L
from .models import *
from update_prices import *
from mail import *
import re

from django.template import loader

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


    return render(request,'home/desktop.html',{'data70k':data70k,'data80k':data80k,'data90k':data90k,'data1l':data1l,'t70':t70,'t80':t80,'t90':t90})

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
    price=fetch_prices(data1l)
    i=0
    for item in data1l:
        item.price=price[i]
        i+=1
        item.save()
    return render(request,'home/update.html')


def laptop_coding(request):
    dataall=Laptop_Coding_Base.objects.all()
    data30k=Laptop_Coding_30k.objects.all()
    data40k=Laptop_Coding_40k.objects.all()
    data50k=Laptop_Coding_50k.objects.all()
    
    return render(request,'home/laptop/coding.html',{'dataall':dataall,'data30k':data30k,'data40k':data40k,'data50k':data50k})


def laptop_gaming(request):
    
    dataall=Laptop_Gaming_Base.objects.all()
    data30k=Laptop_Gaming_30k.objects.all()
    data40k=Laptop_Gaming_40k.objects.all()
    data50k=Laptop_Gaming_50k.objects.all()
    
    return render(request,'home/laptop/gaming.html',{'dataall':dataall,'data30k':data30k,'data40k':data40k,'data50k':data50k})


def email(request):
    a=request.GET.get('a')
    if(a=='1'):
        data=Prebuilt_70k.objects.all()
    elif(a=='2'):
        data=Prebuilt_80k.objects.all()
   
    return render(request,'home/email.html',{'data':data})

def email_req(request):
    email=request.GET.get('email')
    a=str(request.GET.get('a'))
    url="http://127.0.0.1:8000/email?a="+a
    if(email==None):
        return render(request,'home/email_request.html')
    else:
        send_mail(email,url)
        email=None
        a=None    
        return render(request,'home/email_request.html')




def temp(request):
    data=Prebuilt_70k.objects.all()
    comp=[]
    #for item in data:
    #    comp.append()

    data1=Prebuilt_80k.objects.all()

    return render(request,'home/temp.html',{'data':data,'data1':data1,'new':new})


def console(request):
    dataall=Console_Base.objects.all()
    data_micro=Console_micro.objects.all()
    data_sony=Console_sony.objects.all()
    data_ninten=Console_ninten.objects.all()
    
    return render(request,'home/console.html',{'dataall':dataall,'data_micro':data_micro,'data_sony':data_sony,'data_ninten':data_ninten})

