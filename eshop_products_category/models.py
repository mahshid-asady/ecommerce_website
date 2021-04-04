from django.db import models


# Create your models here.
from django.urls import reverse


class ProductCategory(models.Model):
    name = models.CharField(max_length=200,db_index=True)
    slug = models.SlugField(max_length=200,db_index=True,unique=True, default=None)
    pub_date = models.DateTimeField(auto_now_add=True, null=True)


    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def get_absolute_url(self):
        return reverse('product_list_by_category',
                       args=[self.slug])
    def __str__(self):
        return self.name
