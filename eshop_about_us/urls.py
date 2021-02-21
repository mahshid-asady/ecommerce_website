from django.urls import path

from .views import information

urlpatterns = [
    path('aboutus/', information, name='info'),
]