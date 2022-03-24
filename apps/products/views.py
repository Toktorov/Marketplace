from django.shortcuts import render
from apps.products.models import Product
from apps.settings.models import Setting

# Create your views here.
def product_detail(request, id):
    product = Product.objects.get(id = id)
    home = Setting.objects.latest('id')
    context = {
        'product' : product,
        'home' : home,
    }
    return render(request, 'product-left-sidebar.html', context)