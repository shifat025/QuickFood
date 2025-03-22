from django.urls import path, include
from .views import UserOrderHistoryAPIView, CreateOrderAPIView



urlpatterns = [
    path('create/', CreateOrderAPIView.as_view(), name='create-order'),
   path('history/', UserOrderHistoryAPIView.as_view(), name='order-history'),
]