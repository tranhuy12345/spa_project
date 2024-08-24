from django.urls import path
from .views import ImageUploadView,ImagesUploadView

urlpatterns = [
    path('', ImageUploadView.as_view(), name='image-upload'),
    path('/many', ImagesUploadView.as_view(), name='images-upload'),
]
