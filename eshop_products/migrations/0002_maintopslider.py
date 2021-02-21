# Generated by Django 3.1.6 on 2021-02-09 10:07

from django.db import migrations, models
import eshop_products.models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainTopSlider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=23)),
                ('image', models.ImageField(upload_to=eshop_products.models.upload_gallery_image_path, verbose_name='تصویر')),
            ],
        ),
    ]
