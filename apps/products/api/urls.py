from apps.products.api.views import ProductAPIView
from django.urls import path

urlpatterns = [
    path('api/products', ProductAPIView.as_view(), name = "api_products"),
]