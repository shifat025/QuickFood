from django.contrib import admin
from .models import Order, OrderItem, PaymentInformation

# Register the models without customizations
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(PaymentInformation)
