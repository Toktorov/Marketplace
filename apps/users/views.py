from django.shortcuts import render, redirect
from apps.users.forms import UserRegistrationForm, LoginForm, UpdateProfileForm
from apps.settings.models import Setting
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from apps.users.models import User

# Create your views here.
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return redirect('index')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

def user_profile(request, id):
    user = User.objects.get(id = id)
    home = Setting.objects.latest('id')
    context = {
        'user' : user,
        'home' : home,
    }
    return render(request, 'account/profile.html', context)

def update_profile(request, id):
    user = User.objects.get(id = id)
    form = UpdateProfileForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect('user_profile', user.id)
    context = {
        'form' : form,
    }
    return render(request, 'account/update.html', context)

def delete_profile(request, id):
    user = User.objects.get(id = id)
    if request.method == "POST":
        user.delete()
        return redirect('index')
    return render(request, 'account/delete.html')