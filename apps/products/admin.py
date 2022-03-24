from django.contrib import admin
from apps.products.models import Product, ProductImage

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductImage)