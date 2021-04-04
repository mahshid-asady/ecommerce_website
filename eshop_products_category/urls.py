from django.urls import path

from eshop_products.views import products_categories_partial, ProductsListByCategory

urlpatterns = [
    path('products_categories_partial', products_categories_partial, name='products_categories_partial'),
    path('products/<category_name>', ProductsListByCategory.as_view(), name='product_list_by_category'),
]
