from django.contrib import admin

from .models import Product


class ProductsAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['title', 'price', 'tags', 'content', 'slug', 'downloads']


admin.site.register(Product, ProductsAdmin)
