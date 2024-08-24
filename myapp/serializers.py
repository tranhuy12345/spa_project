from rest_framework import serializers
from .models import Item,Image,Service

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    class Meta:
        model = Image
        fields = ['id', 'image', 'image_url', 'created_at']
    def get_id(self, obj):
        return str(obj.id)

class ServiceSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    image_url = serializers.ListField(child=serializers.CharField(), allow_empty=True)
    class Meta:
        model = Service
        fields = ['id','name', 'description', 'image_url', 'created_at', 'price', 'discount']
    def get_id(self, obj):
        return str(obj.id)