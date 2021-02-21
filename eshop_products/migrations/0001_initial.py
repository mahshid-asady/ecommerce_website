# Generated by Django 3.1.6 on 2021-02-06 18:57

from django.db import migrations, models
import django.db.models.deletion
import eshop_products.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('eshop_products_category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='عنوان')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('price', models.IntegerField(verbose_name='قیمت')),
                ('image', models.ImageField(blank=True, null=True, upload_to=eshop_products.models.upload_image_path, verbose_name='تصویر')),
                ('active', models.BooleanField(default=False, verbose_name='فعال / غیرفعال')),
                ('visit_count', models.IntegerField(default=0, verbose_name='تعداد بازدید')),
                ('brand', models.CharField(max_length=32, verbose_name='برند')),
                ('product_code', models.IntegerField(null=True, verbose_name='کد محصول')),
                ('categories', models.ManyToManyField(blank=True, to='eshop_products_category.ProductCategory', verbose_name='دسته بندی ها')),
            ],
            options={
                'verbose_name': 'محصول',
                'verbose_name_plural': 'محصولات',
            },
        ),
        migrations.CreateModel(
            name='ProductGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='عنوان')),
                ('image', models.ImageField(upload_to=eshop_products.models.upload_gallery_image_path, verbose_name='تصویر')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eshop_products.product', verbose_name='محصول')),
            ],
            options={
                'verbose_name': 'تصویر',
                'verbose_name_plural': 'تصاویر',
            },
        ),
    ]