from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    tel = models.CharField(max_length=255, default="0", blank=True, null=True)
    profile_image = models.ImageField(upload_to = "profile_image/", blank=True, null=True)

    def __str__(self):
        return self.username 

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"