from django.shortcuts import render
from apps.settings.models import Setting
from apps.products.models import Product

# Create your views here.
def index(request):
    home = Setting.objects.latest('id')
    products = Product.objects.all().order_by('-id')[:8]
    context = {
        'home' : home,
        'products' : products,
    }
    return render(request, 'index-2.html', context)