from django.contrib import admin

from .models import Cart


class CartAdmin(admin.ModelAdmin):
    model = Cart
    list_display = ['user', 'product']


admin.site.register(Cart, CartAdmin)
