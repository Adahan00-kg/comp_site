# Generated by Django 5.1.1 on 2024-10-16 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_site', '0002_cart_cartitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='quantity',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
