from django.shortcuts import render, redirect, get_object_or_404
from apps.products.models import Product, ProductComment, FavoriteProduct, LikeProduct
from apps.settings.models import Setting
from apps.categories.models import Category
from django.db.models import Q
from apps.products.forms import ProductCreateForm, ProductUpdateForm, EmailPostForm
from django.core.mail import send_mail

# Create your views here.
def product_detail(request, slug):
    product = Product.objects.get(slug = slug)
    random_products = Product.objects.all().order_by('?')[:20]
    home = Setting.objects.latest('id')
    categories = Category.objects.all().order_by('?')[:5]
    if 'like' in request.POST:
        try:
            like = LikeProduct.objects.get(user=request.user, product=product)
            like.delete()
        except:
            LikeProduct.objects.create(user=request.user, product=product)
    if 'comment' in request.POST:
        id = request.POST.get('post_id')
        message = request.POST.get('comment_message')
        comment = ProductComment.objects.create(message=message, product=product, user=request.user)
        return redirect('product_detail', product.slug)


    context = {
        'product' : product,
        'random_products' : random_products,
        'home' : home,
        'categories' : categories,
    }
    return render(request, 'products/detail.html', context)

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

def product_create(request):
    form = ProductCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    context = {
        'form' : form
    }
    return render(request, 'products/create.html', context)

def product_update(request, slug):
    product = Product.objects.get(slug = slug)
    form = ProductUpdateForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('product_detail', product.slug)
    context = {
        'form' : form
    }
    return render(request, 'products/update.html', context)

def favorite_product(request):
    products = FavoriteProduct.objects.all()
    context = {
        'products' : products,
    }
    return render(request, 'products/favorite.html', context)

def post_share(request, post_id):
    # Retrieve post by id
    post = get_object_or_404(Product, id=post_id)
    sent = False
    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{} ({}) recommends you reading "{}"'.format(cd['name'], cd['email'], post.title)
            message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(post.title, post_url, cd['name'], cd['comments'])
            send_mail(subject, message, 'admin@myblog.com',[cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'products/share.html', {'post': post,
                                                    'form': form,
                                                    'sent': sent})