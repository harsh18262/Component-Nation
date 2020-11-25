from django.db import models

# Create your models here.

class Prebuilt_Base(models.Model):
        id=models.AutoField(primary_key=True)
        product = models.TextField(default=" ")
        desc = models.TextField(default=" ")
        img = models.ImageField(upload_to='Pre_built/images',default='default.jpg')
        url=models.URLField(default=" ")
        price=models.CharField(max_length=20,default=0)

class Prebuilt_70k(Prebuilt_Base):
    pass

class Prebuilt_80k(Prebuilt_Base):
    pass

class Prebuilt_90k(Prebuilt_Base):
    pass

class Prebuilt_1L(Prebuilt_Base):
    pass
