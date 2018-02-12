from django.db import models

# Create your models here.
class Catalog(models.Model):
    name = models.CharField(max_length=255)
    publisher = models.CharField(max_length=300)
    description = models.TextField()
    pub_date = models.DateTimeField(default=datetime.now)

class CatalogCategory(models.Model):
    catalog = models.ForeignKey('Catalog', related_name='categories')
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children')
    name = models.CharField(max_length=300)
    description = models.TextField(blank=True)

 def __unicode__(self):
     if self.parent:
         return u'%s: %s - %s' % (self.catalog.name, self.parent.name, self.name)
     return u'%s: %s' % (self.catalog.name, self.name)

class Product(models.Model):
    category = models.ForeignKey('CatalogCategory', related_name='products')
    name = models.CharField(max_length=300)
    description = models.TextField()
    photo = models.CharField(max_length=300)
    manufacturer = models.CharField(max_length=300, blank=True)
    price_SEK = models.DecimalField(max_digits=6, decimal_places=2)

class Order(models.Model):
    type = models.CharField(max_length=300)
    reference = models.CharField(max_length=300)
    name = models.ForeignKey('Product')
    quantity = models.IntegerField(max_length=300)
    quantity_unit = models.CharField(max_length=300)
    unit_price = models.IntegerField(max_length=300)
    tax_rate = models.IntegerField(max_length=300)
    total_amount = models.IntegerField(max_length=300)
    total_discount_amount = models.IntegerField(max_length=300)
    total_tax_amount = models.IntegerField(max_length=300)
