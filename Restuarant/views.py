from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Restaurant, MenuItem
from .serializers import RestaurantSerializer, MenuItemSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from QuickFood.permissions import IsOwner

class RestaurantList(APIView):
    def get(self, request):
        # Retrieve all restaurant objects
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)

class RestaurantCreate(APIView):
    permission_classes = [IsOwner]
    def post(self, request):
        # Create a new restaurant
        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RestaurantUpdate(APIView):
    permission_classes = [IsOwner]
    def patch(self, request, pk):
        # Update a specific restaurant (partial update)
        try:
            restaurant = Restaurant.objects.get(pk=pk)
        except Restaurant.DoesNotExist:
            return Response({"detail": "Restaurant not found."}, status=status.HTTP_404_NOT_FOUND)

        # Update the restaurant
        serializer = RestaurantSerializer(restaurant, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RestaurantDelete(APIView):
    permission_classes = [IsOwner]
    def delete(self, request, pk):
        # Delete a specific restaurant
        try:
            restaurant = Restaurant.objects.get(pk=pk)
        except Restaurant.DoesNotExist:
            return Response({"detail": "Restaurant not found."}, status=status.HTTP_404_NOT_FOUND)

        restaurant.delete()
        return Response({"detail": "Restaurant deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

    

class MenuItemList(APIView):
    def get(self, request):
        # Retrieve all menu items
        menu_items = MenuItem.objects.all()
        serializer = MenuItemSerializer(menu_items, many=True)
        return Response(serializer.data)

class MenuItemCreate(APIView):
    permission_classes = [IsOwner]
    def post(self, request):
        # Create a new menu item
        serializer = MenuItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MenuItemUpdate(APIView):
    permission_classes = [IsOwner]
    def patch(self, request, pk):
        # Update a specific menu item (partial update)
        try:
            menu_item = MenuItem.objects.get(pk=pk)
        except MenuItem.DoesNotExist:
            return Response({"detail": "Menu item not found."}, status=status.HTTP_404_NOT_FOUND)

        # Update the menu item
        serializer = MenuItemSerializer(menu_item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MenuItemDelete(APIView):
    permission_classes = [IsOwner]
    def delete(self, request, pk):
        # Delete a specific menu item
        try:
            menu_item = MenuItem.objects.get(pk=pk)
        except MenuItem.DoesNotExist:
            return Response({"detail": "Menu item not found."}, status=status.HTTP_404_NOT_FOUND)

        menu_item.delete()
        return Response({"detail": "Menu item deleted successfully."}, status=status.HTTP_204_NO_CONTENT)