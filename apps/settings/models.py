from django.db import models

# Create your models here.
class Setting(models.Model):
    title = models.CharField(max_length=250)
    decription = models.TextField()
    logo = models.ImageField(upload_to = 'logo/')
    tel = models.CharField(max_length=255)
    email = models.EmailField()
    facebook = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)
    linkedin = models.CharField(max_length=255)

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Настройка"
        verbose_name_plural = "Настройки"

class About(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.CharField(max_length=255)
    position = models.CharField(max_length=100)
    signature = models.ImageField(upload_to = "signature/")

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"

class AboutImage(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name="about_image")
    image = models.ImageField(upload_to = "about_image/")

    class Meta:
        verbose_name = "Фото о нас"
        verbose_name_plural = "Фото о нас"

class Team(models.Model):
    team_image = models.ImageField(upload_to = "team_image/")
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=100)
    facebook = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
    skype = models.CharField(max_length=255)
    youtube = models.CharField(max_length=255)

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Команды"