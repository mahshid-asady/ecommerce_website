# Generated by Django 3.1.6 on 2021-07-12 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products', '0009_product_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='active',
        ),
    ]
