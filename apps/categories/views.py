from django.shortcuts import render
from apps.categories.models import Category
from apps.products.models import Product
from apps.settings.models import Setting

# Create your views here.
def category_detail(request, slug):
    category = Category.objects.get(slug = slug)
    categories = Category.objects.all().order_by('-id')
    home = Setting.objects.latest('-id')
    products = Product.objects.all().order_by('-id')
    context = {
        'category' : category,
        'products' : products,
        'home' : home,
        'categories' : categories,
    }
    return render(request, 'category_detail.html', context)
