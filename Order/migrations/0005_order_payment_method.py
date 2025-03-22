# Generated by Django 5.1.7 on 2025-03-22 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0004_rename_deliveryadresss_order_deliveryadress'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('COD', 'Cash on Delivery'), ('Online', 'Online Payment')], default=1, max_length=50),
            preserve_default=False,
        ),
    ]
