from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Items(models.Model):
    name = models.CharField(max_length=255)
    description = 