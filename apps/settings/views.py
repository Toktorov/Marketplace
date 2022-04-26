from django.shortcuts import render
from apps.settings.models import Setting, About, Team
from apps.products.models import Product, Discount, ProductComment
from apps.categories.models import Category
from django.template import RequestContext

# Create your views here.
def index(request):
    home = Setting.objects.latest('id')
    slide_products = Product.objects.all().order_by('-id')[:5]
    products = Product.objects.all().order_by('-id')[:8]
    one_random_product = Product.objects.all().order_by('?')[:1]
    two_random_product = Product.objects.all().order_by('?')[:1]
    three_random_product = Product.objects.all().order_by('?')[:1]
    expensive_products = Product.objects.all().order_by('-price')[:3]
    categories = Category.objects.all().order_by('-id')
    discount_product = Discount.objects.all()[:1]
    most_popular_product = Product.objects.all().order_by('-price')
    comments = ProductComment.objects.all().order_by('-id')
    context = {
        'home' : home,
        'products' : products,
        'slide_products' : slide_products,
        'one_random_product' : one_random_product,
        'two_random_product' : two_random_product,
        'three_random_product' : three_random_product,
        'expensive_products' : expensive_products,
        'categories' : categories,
        'discount_product' : discount_product,
        'most_popular_product' : most_popular_product,
        'comments' : comments,
    }
    return render(request, 'index-2.html', context)

def about_us(request):
    home = Setting.objects.latest('id')
    about = About.objects.latest('id')
    teams = Team.objects.all().order_by('-id')
    context = {
        'home' : home,
        'about' : about,
        'teams' : teams
    }
    return render(request, 'about.html',context)

def handler404(request, exception):
    home = Setting.objects.latest('id')
    categories = Category.objects.all().order_by('-id')
    context = {
        'home' : home,
        'categories' : categories,
    }
    response = render(request, "404.html", context=context)
    response.status_code = 404
    return response