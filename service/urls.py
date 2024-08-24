from django.urls import path
from .views import ServiceDetailView, ServiceView

urlpatterns = [
    path('',ServiceView.as_view(), name='service'),
    # URL mới cho việc lấy dịch vụ theo id
    path('/<int:id>', ServiceDetailView.as_view(), name='service-detail'),
]
