from django.shortcuts import render
from apps.settings.models import Setting
from apps.products.models import Product

# Create your views here.
def index(request):
    home = Setting.objects.latest('id')
    slide_products = Product.objects.all().order_by('-id')[:5]
    products = Product.objects.all().order_by('-id')[:8]
    one_random_product = Product.objects.all().order_by('?')[:1]
    context = {
        'home' : home,
        'products' : products,
        'slide_products' : slide_products,
        'one_random_product' : one_random_product,
    }
    return render(request, 'index-2.html', context)