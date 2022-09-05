from django.contrib import admin

from drf_store.core.models import Product, Order


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')
    ordering = ('title', 'price')
    list_filter = ('title',)
    list_per_page = 20


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('date',)
    ordering = ('date',)
    list_filter = ('date',)
    list_per_page = 20
