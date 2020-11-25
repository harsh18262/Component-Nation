from django.contrib import admin
from .models import Prebuilt_Base,Prebuilt_70k,Prebuilt_80k,Prebuilt_90k,Prebuilt_1L
# Register your models here.

#admin.site.register(Prebuilt_Base)
admin.site.register(Prebuilt_70k)
admin.site.register(Prebuilt_80k)
admin.site.register(Prebuilt_90k)
admin.site.register(Prebuilt_1L)