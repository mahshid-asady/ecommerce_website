from django.urls import path

from eshop_contact.views import contactUs

urlpatterns = [
    path('contact/',contactUs, name='contact')
]