from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from home.models import *
from .serializer import dataserializer
# Create your views here.


@api_view(['GET'])
def prebuilt(request,bud):
    if bud == "70K" or bud == "70k":
        data=Prebuilt_70k.objects.all()
    if bud == "80K" or bud == "80k":
        data=Prebuilt_80k.objects.all()
    if bud == "90K" or bud == "90k":
        data=Prebuilt_90k.objects.all()
    if bud == "1L" or bud == "1l":
        data=Prebuilt_1L.objects.all()
    if bud == "all" or bud == "all":
        data=Prebuilt_Base.objects.all()
    
    

    serializer=dataserializer(data,many=True)
    return Response(serializer.data)
