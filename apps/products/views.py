from django.shortcuts import render
from apps.products.models import Product
from apps.settings.models import Setting
from apps.categories.models import Category

# Create your views here.
def product_detail(request, id):
    product = Product.objects.get(id = id)
    random_products = Product.objects.all().order_by('?')[:20]
    home = Setting.objects.latest('id')
    categories = Category.objects.all().order_by('?')[:5]
    context = {
        'product' : product,
        'random_products' : random_products,
        'home' : home,
        'categories' : categories,
    }
    return render(request, 'product-left-sidebar.html', context)