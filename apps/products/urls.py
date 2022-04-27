from django.urls import path 
from apps.products.views import product_detail, product_search, product_create, product_update, favorite_product, post_share


urlpatterns = [
    path('product/<str:slug>', product_detail, name = "product_detail"),
    path('search/', product_search, name = "product_search"),
    path('create/', product_create, name = "product_create"),
    path('update/<str:slug>', product_update, name = "product_update"),
    path('favorite/', favorite_product, name = "favorite_product"),
    path('<post_id>/share', post_share, name='post_share'),
]