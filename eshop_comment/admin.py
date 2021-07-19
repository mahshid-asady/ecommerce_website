from django.contrib import admin

from eshop_products.models import Product
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'product', 'posted_on', 'active')
    list_filter = ('active', 'posted_on')
    search_fields = ('user', 'email', 'content')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
