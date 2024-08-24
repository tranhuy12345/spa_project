from django.urls import path
from .views import ImageUploadView, ImagesUploadByFileBaseView

urlpatterns = [
    path('', ImageUploadView.as_view(), name='image-upload'),
    path('/many', ImagesUploadByFileBaseView.as_view(), name='images-upload'),
]
