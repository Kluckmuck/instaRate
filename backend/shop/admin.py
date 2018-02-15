from django.contrib import admin

from .models import Catalog, CatalogCategory, Product

# Register your models here.
admin.site.register(Catalog)
admin.site.register(CatalogCategory)
admin.site.register(Product)
