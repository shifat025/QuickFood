from django.urls import path, include
from .views import UserOrderHistoryAPIView, CreateOrderAPIView, OrderStatusUpdateView,OrderListAPIView



urlpatterns = [
    path('create/', CreateOrderAPIView.as_view(), name='create-order'),
   path('history/', UserOrderHistoryAPIView.as_view(), name='order-history'),
   path('<int:pk>/update-status/', OrderStatusUpdateView.as_view(), name='update-order-status'),
   path('get/', OrderListAPIView.as_view(), name='order-list'),
]