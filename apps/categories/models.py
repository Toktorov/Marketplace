from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"