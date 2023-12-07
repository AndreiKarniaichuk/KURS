# admin.py

from django.contrib import admin
from .models import Guest, Waiter, Menu, Orders, Payment

@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ('guest_id', 'first_name', 'last_name', 'phone_number')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

@admin.register(Waiter)
class WaiterAdmin(admin.ModelAdmin):
    list_display = ('waiter_id', 'first_name', 'last_name')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('dish_id', 'dish_name', 'description', 'price')

    def __str__(self):
        return self.dish_name

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'guest', 'waiter', 'status', 'created_at')

    def __str__(self):
        return f"Order {self.order_id} by {self.guest.first_name} {self.guest.last_name}"

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('payment_id', 'order', 'amount', 'payment_time')

    def __str__(self):
        return f"Payment {self.payment_id} for Order {self.order.order_id}"
