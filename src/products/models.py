from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)    # Add comma there so it's iterable for the backend?
        verbose_name_plural = "Categories"

    # Override string representation of this object
    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'


class Manufacturer(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'


class Product(models.Model):
    category    = models.ManyToManyField(Category, related_name='product_category')
    manufacturer= models.ForeignKey(Manufacturer, related_name='product_manufacturer', on_delete=models.CASCADE)
    name        = models.CharField(max_length=120)
    slug        = models.SlugField()
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        ordering = ('id',)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('api-product-detail', kwargs={'id': self.id})   # f'/products/{self.id}/'
