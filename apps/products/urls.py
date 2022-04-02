from django.urls import path 
from apps.products.views import product_detail, product_search


urlpatterns = [
    path('product/<int:id>', product_detail, name = "product_detail"),
    path('search/', product_search, name = "product_search"),
]