from django.shortcuts import render
from django.http import HttpResponse

from fetch_price import *
import re
# Create your views here.
def home(request):
    return render(request,'home/index.html')

def about(request):
    
    return render(request,'home/about.html')

def contact(request):
    
    return render(request,'home/contact.html')

def desktop(request):
    price=[]
    urls=[]
    total=0


    for i in range (2,10):
        price.append(fetch_prices(2,i))
        urls.append(fetch_urls(2,i))
    for i in range (8):
        total = total + int(re.sub("[^0-9]","",price[i]))
    data=get_prices(5,2)
    total="{:,}".format(total)

    return render(request,'home/desktop.html',{'price':price,'total':total,'url':urls,'desc':data})





