from django.shortcuts import render
from rest_framework import status
from .serializers import OrderSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Order
# Create your views here.
class CreateOrderAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data.copy()  # Create a mutable copy of request data
        data['user'] = request.user.id  # Assign authenticated user

        serializer = OrderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    
# views.py

class UserOrderHistoryAPIView(APIView):
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated

    def get(self, request):
        # Retrieve the orders for the authenticated user
        orders = Order.objects.filter(user=request.user)
        
        # Serialize the orders
        serializer = OrderSerializer(orders, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

