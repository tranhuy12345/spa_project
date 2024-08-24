from django.urls import path
from .views import GetListServiceView, ImageUploadView,ImagesUploadView,CreatedServiceView

urlpatterns = [
    path('service',GetListServiceView.as_view(), name='get-list-service'),
    path('service',CreatedServiceView.as_view(), name='created-service'),
    path('upload', ImageUploadView.as_view(), name='image-upload'),
    path('upload/many', ImagesUploadView.as_view(), name='images-upload'),
]
