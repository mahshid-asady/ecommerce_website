from django.contrib import admin

# Register your models here.


from django.contrib import admin

# Register your models here.

from .models import Product, ProductGallery, MainTopSlider


class ProductAdmin(admin.ModelAdmin):
    pass

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductGallery)
admin.site.register(MainTopSlider)
