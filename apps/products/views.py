from django.shortcuts import render
from apps.products.models import Product
from apps.settings.models import Setting
from apps.categories.models import Category

# Create your views here.
def product_detail(request, id):
    product = Product.objects.get(id = id)
    home = Setting.objects.latest('id')
    categories = Category.objects.all().order_by('?')[:5]
    context = {
        'product' : product,
        'home' : home,
        'categories' : categories,
    }
    return render(request, 'product-left-sidebar.html', context)