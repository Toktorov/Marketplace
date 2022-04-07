from django.shortcuts import render, redirect
from apps.products.models import Product, ProductComment
from apps.settings.models import Setting
from apps.categories.models import Category
from django.db.models import Q

# Create your views here.
def product_detail(request, id):
    product = Product.objects.get(id = id)
    random_products = Product.objects.all().order_by('?')[:20]
    home = Setting.objects.latest('id')
    categories = Category.objects.all().order_by('?')[:5]
    if 'comment' in request.POST:
        id = request.POST.get('post_id')
        message = request.POST.get('comment_message')
        comment = ProductComment.objects.create(message=message, product=product, user=request.user)
        return redirect('product_detail', product.id)

    context = {
        'product' : product,
        'random_products' : random_products,
        'home' : home,
        'categories' : categories,
    }
    return render(request, 'product-left-sidebar.html', context)

def product_search(request):
    products = Product.objects.all()
    qury_obj = request.GET.get('key')
    home = Setting.objects.latest('id')
    if qury_obj:
        products = Product.objects.filter(Q(title__icontains = qury_obj))
    context = {
        'home' : home, 
        'products' : products
    }
    return render(request, 'products/search.html', context)