from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['status']  # Only allow updating the status field

    def validate_status(self, value):
        if value not in dict(Order.STATUS_CHOICES).keys():
            raise serializers.ValidationError("Invalid status.")
        return value