from django.shortcuts import render
from decimal import Decimal
from django.shortcuts import render
import datetime
import os
from django.shortcuts import render
from bson import Decimal128
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.views import APIView

from enums.enums import Status, StatusOrder
from util.custom_response import CustomResponse
from .models import Order
from django.core.files.storage import default_storage
from django.conf import settings
from .serializers import OrderSerializer
from drf_spectacular.utils import extend_schema_view, extend_schema


# Create your views here.
@extend_schema_view(
    get=extend_schema(tags=['Order']),
    post=extend_schema(tags=['Order']),
)
class OrderView(APIView):
    
    def get(self, request, *args, **kwargs):
        order = Order.objects.all()
        order_serializer = OrderSerializer(order, many=True)
        return CustomResponse(data=order_serializer.data, status=status.HTTP_200_OK,message='Order found successfully')

    def post(self, request, *args, **kwargs):
        order_serializer = OrderSerializer(data=request.data)
        if order_serializer.is_valid():
            order_serializer.save()
            return CustomResponse(data=order_serializer.data, status=status.HTTP_201_CREATED,message='Order created sucessfully')
        return CustomResponse(data=order_serializer.errors,status=status.HTTP_400_BAD_REQUEST,message='Order data invalid')
    
@extend_schema_view(
    get=extend_schema(tags=['Order']),
    put=extend_schema(tags=['Order']),
    delete=extend_schema(tags=['Order']),
)
class OrderDetailView(APIView):
    def get(self, request,id=None, **kwargs):
        try:
            # Tìm dịch vụ theo id và status
            order = Order.objects.get(id=id)
        except order.DoesNotExist:
            # Quăng lỗi nếu không tìm thấy dịch vụ
            return CustomResponse(status=status.HTTP_404_NOT_FOUND,message='Order not found')
        Order_serializer = OrderSerializer(order,many=False)
        return CustomResponse(data=Order_serializer.data, status=status.HTTP_200_OK,message='Order found successfully')
    
    def put(self, request,id=None, **kwargs):
        try:
            # Tìm dịch vụ theo id và status
            order = Order.objects.get(id=id)
        except order.DoesNotExist:
            # Quăng lỗi nếu không tìm thấy dịch vụ
            return CustomResponse(status=status.HTTP_404_NOT_FOUND,message='Order not found')
        Order_serializer = OrderSerializer(order, data=request.data)
        if Order_serializer.is_valid():
            Order_serializer.save()
            return CustomResponse(data=Order_serializer.data, status=status.HTTP_200_OK,message='Order updated successfully')
        return CustomResponse(data=Order_serializer.errors, status=status.HTTP_200_OK,message='Invalid data')
    
    def delete(self, request, id=None, **kwargs):
        try:
            # Tìm dịch vụ theo id và status
            order = Order.objects.get(id=id)
        except order.DoesNotExist:
            # Quăng l��i nếu không tìm thấy dịch vụ
            return CustomResponse(status=status.HTTP_404_NOT_FOUND, message='Order not found')
        order.status = StatusOrder.CANCELLED.value
        order.save()
            # return CustomResponse(status=status.HTTP_400_BAD_REQUEST, message=f'Error updating Order: {str(e)}')
        return CustomResponse(status=status.HTTP_200_OK, message='Order deleted successfully')