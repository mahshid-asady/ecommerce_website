from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

from eshop_products.models import Product


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True, null=True)
    email = models.EmailField()
    content = models.TextField()
    posted_on = models.DateTimeField(default=timezone.now, editable=False)
    active = models.BooleanField(default=False)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['posted_on']


    def __str__(self):
        return 'Comment {} by {}'.format(self.content[:20], self.user.name)