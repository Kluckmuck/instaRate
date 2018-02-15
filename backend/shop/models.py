from django.db import models
from django.utils import timezone

# Create your models here.
class Catalog(models.Model):
    name = models.CharField(max_length=255)
    publisher = models.CharField(max_length=300)
    description = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
       return self.name

class CatalogCategory(models.Model):
    catalog = models.ForeignKey('Catalog', related_name='categories', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    description = models.TextField(blank=True)

    def __str__(self):
     if self.parent:
         return u'%s: %s - %s' % (self.catalog.name, self.parent.name, self.name)
     return u'%s: %s' % (self.catalog.name, self.name)

class Product(models.Model):
    category = models.ForeignKey('CatalogCategory', related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    description = models.TextField()
    photo = models.CharField(max_length=300)
    manufacturer = models.CharField(max_length=300, blank=True)
    price_SEK = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
       return self.name

class Order(models.Model):
    type = models.CharField(max_length=300)
    reference = models.CharField(max_length=300)
    name = models.ForeignKey('Product', related_name='order', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    quantity_unit = models.CharField(max_length=300)
    unit_price = models.IntegerField()
    tax_rate = models.IntegerField()
    total_amount = models.IntegerField()
    total_discount_amount = models.IntegerField()
    total_tax_amount = models.IntegerField()
