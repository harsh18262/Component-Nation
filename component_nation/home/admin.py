from django.contrib import admin
from .models import Prebuilt_Base,Prebuilt_70k,Prebuilt_80k,Prebuilt_90k,Prebuilt_1L
from .models import Laptop_Coding_Base,Laptop_Coding_30k,Laptop_Coding_40k,Laptop_Coding_50k
from .models import Laptop_Gaming_Base,Laptop_Gaming_30k,Laptop_Gaming_40k,Laptop_Gaming_50k
from .models import Console_micro,Console_sony,Console_ninten
# Register your models here.

#admin.site.register(Prebuilt_Base)
admin.site.register(Prebuilt_70k)
admin.site.register(Prebuilt_80k)
admin.site.register(Prebuilt_90k)
admin.site.register(Prebuilt_1L)

admin.site.register(Laptop_Gaming_30k)
admin.site.register(Laptop_Gaming_40k)
admin.site.register(Laptop_Gaming_50k)


admin.site.register(Laptop_Coding_30k)
admin.site.register(Laptop_Coding_40k)
admin.site.register(Laptop_Coding_50k)

admin.site.register(Console_micro)
admin.site.register(Console_sony)
admin.site.register(Console_ninten)