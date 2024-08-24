from decimal import Decimal
from django.shortcuts import render
import datetime
import os
from django.shortcuts import render
from bson import Decimal128
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.views import APIView

from enums.enums import Status
from util.custom_response import CustomResponse
from .models import Service
from django.core.files.storage import default_storage
from django.conf import settings
from .serializers import ServiceSerializer
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.permissions import IsAuthenticated
from user.permissions import IsAdminUser, IsCustomerUser

# Create your views here.
@extend_schema_view(
    get=extend_schema(tags=['Service']),
    post=extend_schema(tags=['Service']),
)
class ServiceView(APIView):
    
    def get(self, request, *args, **kwargs):
        services = Service.objects.filter(status=Status.ACTIVE.value)
        service_serializer = ServiceSerializer(services, many=True)
        return CustomResponse(data=service_serializer.data, status=status.HTTP_200_OK,message='Service found successfully')

    def post(self, request, *args, **kwargs):
        service_serializer = ServiceSerializer(data=request.data)
        if service_serializer.is_valid():
            service_serializer.save()
            return CustomResponse(data=service_serializer.data, status=status.HTTP_201_CREATED,message='Service created sucessfully')
        return CustomResponse(data=service_serializer.errors,status=status.HTTP_400_BAD_REQUEST,message='Service data invalid')
    
@extend_schema_view(
    get=extend_schema(tags=['Service']),
    put=extend_schema(tags=['Service']),
    delete=extend_schema(tags=['Service']),
)
class ServiceDetailView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    def get(self, request,id=None, **kwargs):
        try:
            # Tìm dịch vụ theo id và status
            service = Service.objects.get(id=id, status=Status.ACTIVE.value)
        except Service.DoesNotExist:
            # Quăng lỗi nếu không tìm thấy dịch vụ
            return CustomResponse(status=status.HTTP_404_NOT_FOUND,message='Service not found')
        service_serializer = ServiceSerializer(service,many=False)
        return CustomResponse(data=service_serializer.data, status=status.HTTP_200_OK,message='Service found successfully')
    
    def put(self, request,id=None, **kwargs):
        try:
            # Tìm dịch vụ theo id và status
            service = Service.objects.get(id=id, status=Status.ACTIVE.value)
        except Service.DoesNotExist:
            # Quăng lỗi nếu không tìm thấy dịch vụ
            return CustomResponse(status=status.HTTP_404_NOT_FOUND,message='Service not found')
        service_serializer = ServiceSerializer(service, data=request.data)
        if service_serializer.is_valid():
            service_serializer.save()
            return CustomResponse(data=service_serializer.data, status=status.HTTP_200_OK,message='Service updated successfully')
        return CustomResponse(data=service_serializer.errors, status=status.HTTP_200_OK,message='Invalid data')
    
    def delete(self, request, id=None, **kwargs):
        try:
            # Tìm dịch vụ theo id và status
            service = Service.objects.get(id=id, status=Status.ACTIVE.value)
        except Service.DoesNotExist:
            # Quăng l��i nếu không tìm thấy dịch vụ
            return CustomResponse(status=status.HTTP_404_NOT_FOUND, message='Service not found')
        service.status = int(Status.INACTIVE.value)

            # return CustomResponse(status=status.HTTP_400_BAD_REQUEST, message=f'Error updating service: {str(e)}')
        return CustomResponse(status=status.HTTP_200_OK, message='Service deleted successfully')

