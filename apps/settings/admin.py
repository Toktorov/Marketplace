from django.contrib import admin
from apps.settings.models import Setting, About, AboutImage, Team
# Register your models here.

admin.site.register(Setting)
admin.site.register(About)
admin.site.register(AboutImage)
admin.site.register(Team)