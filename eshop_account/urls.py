from django.urls import path
from django.views.generic import TemplateView

from .views import login_process, register, logout_process

urlpatterns = [

    path('login', login_process, name='login'),
    path('register', register, name='register'),
    path('logout', logout_process, name='logout'),

]
