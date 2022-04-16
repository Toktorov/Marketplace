from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from apps.order.models import ShopCart, ShopCartForm
from apps.settings.models import Setting
from apps.products.models import Category


# Create your views here.
def index(request):
    return HttpResponse("Order page")


@login_required(login_url='/login')  # проверить логин
def addtoshopcart(request, id):
    url = request.META.get('HTTP_REFERER')  # получение последнего url
    current_user = request.user

    checkproduct = ShopCart.objects.filter(product_id=id)  # проверить товар в корзине
    if checkproduct:
        control = 1  # товар в корзине
    else:
        control = 0  # товар в не корзине

    if request.method == 'POST':
        form = ShopCartForm(request.POST)
        if form.is_valid():
            if control == 1:  # обновляем корзину
                data = ShopCart.objects.get(product_id=id)
                data.quantity += form.cleaned_data['quantity']
                data.save()
            else:  # вложим корзину
                data = ShopCart()
                data.user_id = current_user.id
                data.product_id = id
                data.quantity = form.cleaned_data['quantity']
                data.save()
        messages.success(request, "Продукт добавлен в корзину")
        return HttpResponseRedirect(url)

    else:
        if control == 1:  # обновляем корзину
            data = ShopCart.objects.get(product_id=id)
            data.quantity += 1
            data.save()
        else:  # вложим корзину
            data = ShopCart()
            data.user_id = current_user.id
            data.product_id = id
            data.quantity = 1
            data.save()
        messages.success(request, "Продукт добавлен в корзину")
        return HttpResponseRedirect(url)


def shopcart(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    current_user = request.user
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    total = 0
    for i in shopcart:
        total += i.product.price * i.quantity
    context = {
        'setting': setting,
        'category': category,
        'shopcart': shopcart,
        'total': total,
    }
    return render(request, 'cart/shopcart_products.html', context)


@login_required(login_url='/login')  # проверить логин
def deletefromcart(request, id):
    ShopCart.objects.filter(id=id).delete()
    messages.success(request, "Успешно удален")
    return HttpResponseRedirect('/shopcart')