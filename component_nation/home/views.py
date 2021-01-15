from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
from update_prices import *
from mail import *
import re

from django.template import loader
link=""
# Create your views here.
def home(request):
    
    return render(request,'home/index.html')

def aboutus(request):
    data=about.objects.all()
    return render(request,'home/about.html',{'data':data})

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
    t1=total(data1l)


    return render(request,'home/desktop.html',{'data70k':data70k,'data80k':data80k,'data90k':data90k,'data1l':data1l,'t70':t70,'t80':t80,'t90':t90,'t1':t1})

def update(request):

   
    data70k=Prebuilt_70k.objects.all()
    data80k=Prebuilt_80k.objects.all()
    data90k=Prebuilt_90k.objects.all()
    data1l=Prebuilt_1L.objects.all()
    data_console=Console_Base.objects.all()
    

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
    price=fetch_prices(data_console)
    i=0
    for item in data_console:
        item.price=price[i]
        i+=1
        item.save()
    
    return render(request,'home/update.html')

def update_laptops(request):

   
    data_code=Laptop_Coding_Base.objects.all()
    data_game=Laptop_Gaming_Base.objects.all()
    

    price=fetch_prices(data_code)
    i=0
    for item in data_code:
        item.price=price[i]
        i+=1
        item.save()
    price=fetch_prices(data_game)
    i=0
    for item in data_game:
        item.price=price[i]
        i+=1
        item.save()
    return render(request,'home/update_laptop.html')

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
        t=total(data)
    elif(a=='2'):
        data=Prebuilt_80k.objects.all()
        t=total(data)
    elif(a=='3'):
        data=Prebuilt_90k.objects.all()
        t=total(data)
    elif(a=='4'):
        data=Prebuilt_1L.objects.all()
        t=total(data)
    return render(request,'home/email.html',{'data':data,'total':t})

def email_req(request):
    email=request.GET.get('email')
    a=str(request.GET.get('a'))
    url=link+"/email?a="+a
    if(email==None):
        return render(request,'home/email_request.html')
    else:
        send_mail(email,url)
        email=None
        a=None    
        return render(request,'home/email_request.html')

def callback_req(request):
    email=request.GET.get('email')
    Name=str(request.GET.get('name'))
    sub=str(request.GET.get('sub'))
    body=str(request.GET.get('body'))
    callback_mail("componentnation@gmail.com",email,Name,sub,body)
    email=None
    Name=None
    sub=None
    body=None
    return render(request,'home/callback_req.html')


def temp(request):
    #dataa=about.objects.all()
    dataa=about.objects.all()
    return render(request,'home/temp.html',{'data1':dataa})


def console(request):
    dataall=Console_Base.objects.all()
    data_micro=Console_micro.objects.all()
    data_sony=Console_sony.objects.all()
    data_ninten=Console_ninten.objects.all()
    
    return render(request,'home/console.html',{'dataall':dataall,'data_micro':data_micro,'data_sony':data_sony,'data_ninten':data_ninten})

def compare(request):
    a=request.GET.get('a')
    b=request.GET.get('b')
    
    if(a=='1'):
        data=Prebuilt_70k.objects.all()
    elif(a=='2'):
        data=Prebuilt_80k.objects.all()
    elif(a=='3'):
        data=Prebuilt_90k.objects.all()
    elif(a=='4'):
        data=Prebuilt_1L.objects.all()
    if(b=='1'):
        data1=Prebuilt_70k.objects.all()
    elif(b=='2'):
        data1=Prebuilt_80k.objects.all()
    elif(b=='3'):
        data1=Prebuilt_90k.objects.all()
    elif(b=='4'):
        data1=Prebuilt_1L.objects.all()

    comp=[]
    name=['Processor','Motherboard','Ram','SSD','HDD','Graphics Card','Case','Power Supply']
    for item,item1,name in zip(data,data1,name):
        comp.append(name)
        comp.append(item.product)
        comp.append(item1.product)

    return render(request,'home/compare.html',{'comp':comp})

