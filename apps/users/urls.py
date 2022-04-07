from django.urls import path 
from apps.users.views import register, user_login


urlpatterns = [
    path('register/', register, name = "regsiter"),
    path('login/', user_login, name = "user_login"),
]