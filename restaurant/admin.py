from django.contrib import admin
from .models import Menu, Booking, Order, OrderItem, Address


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "status", "payment_method", "total_amount", "created_at")
    inlines = [OrderItemInline]


admin.site.register(Menu)
admin.site.register(Booking)
admin.site.register(Address)
