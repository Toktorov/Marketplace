from django.shortcuts import render, redirect
from apps.products.models import Product, ProductComment
from apps.products.forms import CommentForm
from apps.settings.models import Setting
from apps.categories.models import Category
from django.db.models import Q

# Create your views here.
def product_detail(request, id):
    product = Product.objects.get(id = id)
    random_products = Product.objects.all().order_by('?')[:20]
    home = Setting.objects.latest('id')
    categories = Category.objects.all().order_by('?')[:5]
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.product = product
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

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