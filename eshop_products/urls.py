from django.urls import path

from eshop_products.views import ProductsList, SearchProductsView, product_detail

urlpatterns= [
    path('products/', ProductsList.as_view(), name='products'),
    path('products/<productId>/<name>', product_detail,name='product_detail_page'),
    path('search/', SearchProductsView.as_view(), name='search'),


]