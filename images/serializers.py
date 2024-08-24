from rest_framework import serializers
from .models import Image


class ImageSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    class Meta:
        model = Image
        fields = ['id', 'image', 'image_url', 'created_at']
    def get_id(self, obj):
        return int(obj.id)