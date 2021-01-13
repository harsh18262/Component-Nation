"""component_nation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the iznclude() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('about', views.about,name='about'),
    path('desktop', views.desktop,name='desktop'),
    path('contact', views.contact,name='contact'),
    path('update', views.update,name='update'),
    path('update_laptops', views.update_laptops,name='update_laptops'),
    path('laptop_gaming', views.laptop_gaming,name='laptop_gaming'),
    path('laptop_coding', views.laptop_coding,name='laptop_coding'),
    path('email', views.email,name='email'),
    path('email_req', views.email_req,name='email_request'),
    path('consoles', views.console,name='consoles'),
    path('compare', views.compare,name='compare'),
    path('temp', views.temp,name='temp'),
    path('callback_req', views.callback_req,name='callback_req'),
]

urlpatterns += static(settings.ASSETS_URL, document_root=settings.ASSETS_ROOT)
urlpatterns += static(settings.VENDOR_URL, document_root=settings.VENDOR_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)