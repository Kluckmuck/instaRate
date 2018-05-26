from django.test import TestCase, Client
from ..models import CatalogCategory, Catalog, Product, Event, Form, Question
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
        event = Event.objects.create(product=product, name='Workshop', description='A great workshop', photo='www.fake.com')
        form = Form.objects.create(event=event, name='First form', description='A nice form')
        question = Question.objects.create(form=form, title='Do you like')



        Product.objects.create(category=shirtCategory, name='White Shirt', description='A white shirt', photo='www.fake.com')
        Product.objects.create(category=shirtCategory, name='Blue Shirt', description='A blue shirt', photo='www.fake.com')
        Product.objects.create(category=shirtCategory, name='Red Shirt', description='A red shirt', photo='www.fake.com')

        Event.objects.create(product=product, name='Seminar', description='A fantastic seminar', photo='www.fake.com')

        Form.objects.create(event=event, name='First form', description='A nice form')
        Form.objects.create(event=event, name='First form', description='A nice form')
        Form.objects.create(event=event, name='First form', description='A nice form')

        Question.objects.create(form=form, title='like it')
        Question.objects.create(form=form, title='like that')
        Question.objects.create(form=form, title='cardiB')
        Question.objects.create(form=form, title='skrrt')

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

    def test_getForms(self):
        response = self.client.get('/api/event/1/')

        data = json.loads(response.content.decode())
        self.assertEqual(len(data), 4)
        self.assertEqual(response.status_code, 200)

    def test_getQuestion(self):
        response = self.client.get('/api/form/1/')

        data = json.loads(response.content.decode())
        self.assertEqual(len(data), 5)
        self.assertEqual(response.status_code, 200)

    def test_postForm(self):
        response = self.client.post('/api/event/1/', json.dumps({'name': 'Spiderman','description': 'Batman'}), content_type='application/json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Form.objects.get(id=5).name, 'Spiderman')

    def test_deleteForm(self):
        response = self.client.delete('/api/form/1/')

        self.assertRaises(Form.DoesNotExist, Form.objects.get, id=1)
        self.assertEqual(response.status_code, 204)

        response = self.client.delete('/api/form/10/')

        self.assertRaises(Form.DoesNotExist, Form.objects.get, id=10)
        self.assertEqual(response.status_code, 404)

    def test_postQuestion(self):
        response = self.client.post('/api/form/1/', json.dumps({'title': 'My title'}), content_type='application/json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Question.objects.get(id=6).title, 'My title')

    def test_deleteQuestion(self):
        response = self.client.delete('/api/question/1/')

        self.assertRaises(Question.DoesNotExist, Question.objects.get, id=1)
        self.assertEqual(response.status_code, 204)

        response = self.client.delete('/api/question/10/')

        self.assertRaises(Question.DoesNotExist, Question.objects.get, id=10)
        self.assertEqual(response.status_code, 404)
