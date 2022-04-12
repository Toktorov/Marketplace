from django.contrib import admin
from apps.products.models import Product, ProductImage, Discount, ProductComment

# Register your models here.
class ProductImageAdmin(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]
    list_display = ('title', 'price')
    search_fields = ('title', 'price')
    ordering = ('-price',)
    list_per_page = 10

admin.site.register(Product, ProductAdmin)
admin.site.register(Discount)
admin.site.register(ProductComment)