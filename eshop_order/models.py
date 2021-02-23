from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_date = models.DateTimeField(blank=True, null=True, verbose_name='تاریخ پرداخت')
