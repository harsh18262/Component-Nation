from rest_framework import serializers
from home.models import Prebuilt_Base

class dataserializer(serializers.ModelSerializer):
    class Meta:
        model=Prebuilt_Base
        fields='__all__'
