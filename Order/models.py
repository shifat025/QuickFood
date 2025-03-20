from django.db import models
from django.contrib.auth.models import User
from Restuarant.models import Restaurant, MenuItem

class Order(models.Model):
    STATUS_CHOICES = [
        ('Preparing', 'Preparing'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered'),
        ('Canceled', 'Canceled'),  # Added Canceled status
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Preparing')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_created = models.DateTimeField(auto_now_add=True)
    cancel_reason = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Order {self.id} for {self.user.username}"

    def cancel(self, reason):
        """Helper method to cancel the order."""
        self.status = 'Canceled'
        self.cancel_reason = reason
        self.save(update_fields=['status', 'cancel_reason'])

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price_at_order = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.menu_item.name} in Order {self.order.id}"


class PaymentInformation(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Failed', 'Failed'),
        ('Refunded', 'Refunded'),
    ]
    
    PAYMENT_METHOD_CHOICES = [
        ('COD', 'Cash on Delivery'),
        ('Online', 'Online Payment'),
    ]

    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='payment_info')
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHOD_CHOICES)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='Pending')
    transaction_id = models.CharField(max_length=255, blank=True, null=True)
    payment_date = models.DateTimeField(null=True, blank=True)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Payment for Order {self.order.id} ({self.payment_status})"

    def process_payment(self):
        """Handles the payment processing logic."""
        if self.payment_method == 'Online':
            if self.payment_status == 'Completed':
                self.order.status = 'Preparing'
            elif self.payment_status == 'Failed':
                self.order.status = 'Canceled'
        elif self.payment_method == 'COD':
            self.order.status = 'Preparing'

        self.order.save()

    def save(self, *args, **kwargs):
        """Override save method to process payment automatically."""
        self.process_payment()
        super().save(*args, **kwargs)



