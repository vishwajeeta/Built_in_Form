from rest_framework import serializers
from .models import personalinfo

class personalinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=personalinfo
        fields='__all__'