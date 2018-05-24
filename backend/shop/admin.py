from django.contrib import admin

from .models import Catalog, CatalogCategory, Product, Event, Form, Question

# Register your models here.
admin.site.register(Catalog)
admin.site.register(CatalogCategory)
admin.site.register(Product)
admin.site.register(Event)
admin.site.register(Form)
admin.site.register(Question)
