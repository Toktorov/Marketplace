from django.urls import path 
from apps.users.views import register


urlpatterns = [
    path('register/', register, name = "regsiter")
]