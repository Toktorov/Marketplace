from rest_framework import generics
from apps.products.models import Product
from apps.products.api.serializers import ProductSerializer


class ProductAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

