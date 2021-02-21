# Generated by Django 3.1.6 on 2021-02-20 12:48

from django.db import migrations, models
import eshop_about_us.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=500)),
                ('main_image', models.ImageField(upload_to=eshop_about_us.models.upload_image_path)),
                ('bottom_image', models.ImageField(upload_to=eshop_about_us.models.upload_image_path)),
            ],
        ),
        migrations.CreateModel(
            name='Designers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('image', models.ImageField(upload_to=eshop_about_us.models.upload_image_path)),
            ],
        ),
    ]