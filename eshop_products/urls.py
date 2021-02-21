from django.urls import path

from eshop_products.views import ProductsList, SearchProductsView, product_detail

urlpatterns= [
    path('products/', ProductsList.as_view(), name='products'),
    path('search/', SearchProductsView.as_view(), name= 'search'),
    path('products/<productId>/<name>', product_detail),
]