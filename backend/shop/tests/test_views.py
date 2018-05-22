from django.test import TestCase, Client
from ..models import CatalogCategory, Catalog, Product, Event
import json

# Create your tests here.
## 200 (Ok) : Request was responded successfully.
## 201 (Created) : Request has created new resources successfully.
## 401 (Unauthorized) : Request requires authentication. This should be returned if you are requesting without signing in.
## 403 (Forbidden) : Request is forbidden. This should be returned if your request tries to modify resources of which you are not the owner.
## 404 (Not Found) : Requested resource is not found.
## 405 (Method not allowed) : Requested URL does not allow the method of the request.

class CatalogCategoryTestCase(TestCase):
    def setUp(self):
        cTop = Catalog.objects.create(name='Products', publisher='Jacuzzi', description='Top level catalog')
        ##Cshirt = Catalog.objects.create(name='Shirts', publisher='Jacuzzi', description='Shirt catalog')

        shirtCategory = CatalogCategory.objects.create(catalog=cTop, name='Shirts')
        product = Product.objects.create(category=shirtCategory, name='Black Shirt', description='A black shirt', photo='www.fake.com')

        Product.objects.create(category=shirtCategory, name='White Shirt', description='A white shirt', photo='www.fake.com')
        Product.objects.create(category=shirtCategory, name='Blue Shirt', description='A blue shirt', photo='www.fake.com')
        Product.objects.create(category=shirtCategory, name='Red Shirt', description='A red shirt', photo='www.fake.com')

        Event.objects.create(product=product, name='Workshop', description='A great workshop', photo='www.fake.com')
        Event.objects.create(product=product, name='Seminar', description='A fantastic seminar', photo='www.fake.com')


        self.client = Client()

    def test_getCatalog_oob(self):
        response = self.client.get('/api/cc/150/')

        self.assertEqual(response.status_code, 404)

    def test_getCatalog(self):
        response = self.client.get('/api/cc/1/')

        data = json.loads(response.content.decode())
        self.assertEqual(len(data), 4)
        self.assertEqual(response.status_code, 200)

    def test_getProduct(self):
        response = self.client.get('/api/product/1/')

        data = json.loads(response.content.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['name'], 'Black Shirt')

    def test_getProduct_oob(self):
        response = self.client.get('/api/product/150/')
        self.assertEqual(response.status_code, 404)

    def test_getEvents(self):
        response = self.client.get('/api/product/1/events/')

        data = json.loads(response.content.decode())
        self.assertEqual(len(data), 2)
        self.assertEqual(response.status_code, 200)
