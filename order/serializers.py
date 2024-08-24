from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id',
            'created_at',
            'created_by',
            'name_customer',
            'id_customer',
            'email',
            'email',
            'payment_method',
            'phone_number',
            'check_in_datetime',
            'check_out_datetime',
            'service_use',
            'status'
        ]
        def get_id(self, obj):
            return str(obj.id)