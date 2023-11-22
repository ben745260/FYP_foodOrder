from django.contrib import admin
from .models import Product, ProductCategory, Order

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'category', 'price', 'pub_date')
    list_filter = ('category',)
    search_fields = ('product_name', 'category')

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'order_user', 'order_lastEditor', 'order_lastUpdateTime')