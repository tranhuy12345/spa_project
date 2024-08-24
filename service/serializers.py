from decimal import Decimal, InvalidOperation
from rest_framework import serializers
from .models import Service

class ServiceSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    image_url = serializers.ListField(child=serializers.CharField(), allow_empty=True)
    class Meta:
        model = Service
        fields = ['id','name', 'description', 'image_url', 'created_at', 'price', 'discount','time_service']
    def get_id(self, obj):
        return int(obj.id)
    def get_image_url(self, obj):
        return obj.get_image_url()
    
