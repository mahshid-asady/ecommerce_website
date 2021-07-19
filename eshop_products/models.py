import os
from django.db.models import Q

from django.db import models

# Create your models here.
from django.shortcuts import get_object_or_404
from django.urls import reverse

from eshop_products_category.models import ProductCategory


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.name}{ext}"
    return f"products/{final_name}"


def upload_gallery_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/galleries/{final_name}"


class ProductsManager(models.Manager):
    def get_products_by_category(self, category_name):
        return self.get_queryset().filter(categories__name__iexact=category_name, available=True)

    def search(self, query):
        lookup = (
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(tag__title__icontains=query)
        )
        return self.get_queryset().filter(lookup, active=True).distinct()

    def get_active_products(self):
        return self.get_queryset().filter(active=True)

    def get_by_id(self, product_id):
        qs = self.get_queryset().filter(id=product_id)
        if qs.count() == 1:
            return qs.first()
        return None





class Product(models.Model):
    name = models.CharField(max_length=200, db_index=True, default='SOME STRING')
    description = models.TextField(verbose_name='توضیحات')
    slug = models.SlugField(max_length=200, db_index=True, default='example')
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name='تصویر')
    stock = models.PositiveIntegerField(default=None)
    active = models.BooleanField(default=True)
    pub_date = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    visit_count = models.IntegerField(default=0, verbose_name='تعداد بازدید')
    categories = models.ManyToManyField(ProductCategory, blank=True, verbose_name="دسته بندی ها")
    brand = models.CharField(max_length=32, verbose_name='برند')
    product_code = models.IntegerField(verbose_name='کد محصول', null=True)
    discount = models.BooleanField(default=False)
    discount_amount = models.IntegerField(null=True, blank=True)
    price= models.IntegerField(default=100)

    objects = ProductsManager()

    class Meta:
        ordering = ('-pub_date',)
        index_together = (('id', 'slug'),)

        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'


    def get_absolute_url(self):
        return reverse('product_detail_page',
                       args=[self.id, self.slug])





class ProductGallery(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    image = models.ImageField(upload_to=upload_gallery_image_path, verbose_name='تصویر')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')

    class Meta:
        verbose_name = 'تصویر'
        verbose_name_plural = 'تصاویر'

    def __str__(self):
        return self.title


class MainTopSlider(models.Model):
    title = models.CharField(max_length=23)
    image = models.ImageField(upload_to=upload_gallery_image_path, verbose_name='تصویر')

class RecommendedProducts(models.Model):
    pass