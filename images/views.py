from django.shortcuts import render
import datetime
import os
from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.views import APIView

from images.firebase import upload_image_to_firebase
from .models import Image
from django.core.files.storage import default_storage
from django.conf import settings
from .serializers import ImageSerializer
# Create your views here.
class ImageUploadView(APIView):
    def post(self, request, *args, **kwargs):
        file_serializer = ImageSerializer(data=request.data)
        
        if file_serializer.is_valid():
            image_file = request.FILES.get('image')
            if image_file:
                # Lưu hình ảnh vào thư mục media
                file_name = default_storage.save(os.path.join('images', image_file.name), image_file)
                image_url = os.path.join(settings.MEDIA_URL, file_name)

                # Lưu thông tin vào MongoDB
                file_serializer.validated_data['image_url'] = image_url
                file_serializer.save()

                return Response(file_serializer.data, status=status.HTTP_201_CREATED)
            return Response({'error': 'No image file provided'}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    
class ImagesUploadView(APIView):
    def post(self, request, *args, **kwargs):
        images = request.FILES.getlist('images')

        if not images:
            return Response({'error': 'No images provided'}, status=status.HTTP_400_BAD_REQUEST)
        
        image_urls = []  # Danh sách để lưu trữ URL hình ảnh đã lưu
        response_data = []

        for image_file in images:
             # Lưu hình ảnh vào thư mục media
            file_name = default_storage.save(os.path.join('images', image_file.name), image_file)
            image_url = os.path.join(settings.MEDIA_URL, file_name)

            # Tạo đối tượng mới và lưu thông tin vào MongoDB
            image_instance = Image(
                image=file_name,
                image_url=image_url,
                created_at=datetime.datetime.now()
            )
            image_instance.save()

            # Thêm thông tin hình ảnh vào danh sách phản hồi
            serializer = ImageSerializer(image_instance)
            response_data.append(serializer.data)
        
        return Response(response_data, status=status.HTTP_201_CREATED)
    

class ImagesUploadByFileBaseView(APIView):
    def post(self, request, *args, **kwargs):
        images = request.FILES.getlist('images')

        if not images:
            return Response({'error': 'No images provided'}, status=status.HTTP_400_BAD_REQUEST)
        
        response_data = []

        for image_file in images:
            # Upload the image to Firebase
            image_url = upload_image_to_firebase(image_file)

            # Create a new instance and save information in MongoDB (if needed)
            image_instance = Image(
                image=image_file.name,
                image_url=image_url,
                created_at=datetime.datetime.now()
            )
            image_instance.save()

            # Add the image information to the response list
            serializer = ImageSerializer(image_instance)
            response_data.append(serializer.data)
        
        return Response(response_data, status=status.HTTP_201_CREATED)
    
class ImageUploadByFileBaseView(APIView):
    def post(self, request, *args, **kwargs):
        file_serializer = ImageSerializer(data=request.data)
        
        if file_serializer.is_valid():
            image_file = request.FILES.get('image')
            if image_file:
                # Lưu hình ảnh vào thư mục media
                image_url = upload_image_to_firebase(image_file)

                # Lưu thông tin vào MongoDB
                file_serializer.validated_data['image_url'] = image_url
                file_serializer.save()

                return Response(file_serializer.data, status=status.HTTP_201_CREATED)
            return Response({'error': 'No image file provided'}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


