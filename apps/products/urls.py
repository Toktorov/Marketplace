from django.urls import path 
from apps.products.views import product_detail, product_search, product_create, product_update


urlpatterns = [
    path('product/<int:id>', product_detail, name = "product_detail"),
    path('search/', product_search, name = "product_search"),
    path('create/', product_create, name = "product_create"),
    path('update/<int:id>', product_update, name = "product_update"),
]