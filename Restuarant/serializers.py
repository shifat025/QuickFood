from rest_framework import serializers
from .models import Restaurant, MenuItem

class RestaurantSerializer(serializers.ModelSerializer):
    owner_name = serializers.CharField(source='owner.username', read_only=True)
    class Meta:
        model = Restaurant
        fields = ['id','name', 'description', 'location', 'image', 'owner_name']

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'
