from django.urls import path
from apps.cart import views

urlpatterns = [
    path('cart/', views.cart_view, name='cart_page'),
    path('update/', views.cart_update, name='update_cart'),
    path('cart_check/', views.cart_check, name = "cart_check"),
]