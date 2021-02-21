from django.urls import path
from django.views.generic import TemplateView

from .views import login, register

urlpatterns = [

    path('login', login, name='login'),
    path('register', register, name='register'),

]
