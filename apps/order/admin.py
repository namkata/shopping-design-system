from django.contrib import admin
from .models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'status', 'order_date', 'user', 'payment', 'created_at', 'updated_at')
    search_fields = ('order_number', 'user__username', 'user__email')


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price', 'created_at', 'updated_at')
    search_fields = ('order__order_number', 'product__name')
