from django.urls import path 
from apps.categories.views import category_detail


urlpatterns = [
    path('category/<int:id>', category_detail, name = "category_detail"),
]