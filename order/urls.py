from django.urls import path
from .views import OrderView,OrderDetailView

urlpatterns = [
    path('', OrderView.as_view(), name='order-view'),
    path('/<str:id>', OrderDetailView.as_view(), name='order-view-detail'),
]
