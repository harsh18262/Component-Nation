from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include
from api import views

urlpatterns = [
    path('Prebuilt/<str:bud>', views.prebuilt),

]