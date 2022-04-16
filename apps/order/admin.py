from django.contrib import admin

# Register your models here.
from apps.order.models import ShopCart, Order, OrderProduct

class ShopCartAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'quantity', 'price', 'amount']
    list_filter = ['user']

class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('user', 'product', 'price', 'quantity', 'amount')
    can_delete = False 
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'city', 'total', 'status']
    list_filter = ['status']
    readonly_fields = ('user', 'address', 'city', 'country', 'phone', 'first_name', 'ip', 'last_name', 'total')
    can_delete = False
    inlines = [OrderProductInline]

class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'price', 'quantity', 'amount']
    list_filter = ['user']

admin.site.register(OrderProduct, OrderProductAdmin)
admin.site.register(ShopCart, ShopCartAdmin)
admin.site.register(Order, OrderAdmin)