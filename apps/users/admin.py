from django.contrib import admin
from apps.users.models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    # fields = ('username', 'tel') #Вывести нужное поле
    # exclude = ('username',) #Исключить поле 
    list_display = ('username', 'email', 'tel')
    search_fields = ('username', 'email')
    ordering = ('username',)
    list_per_page = 10

admin.site.register(User, UserAdmin)