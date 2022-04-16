from django.urls import path
from apps.order.views import index, addtoshopcart, deletefromcart

urlpatterns = [
    path('cart/', index, name="order"),
    path('addtoshopcart/<int:id>', addtoshopcart, name="addtoshopcart"),
    path('deletefromcart/<int:id>', deletefromcart, name="deletefromcart"),
]