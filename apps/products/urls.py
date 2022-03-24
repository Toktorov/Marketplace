from django.urls import path 
from apps.products.views import product_detail


urlpatterns = [
    path('product/<int:id>', product_detail, name = "product_detail"),
]