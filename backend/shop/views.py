from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from django.forms.models import model_to_dict

from .models import CatalogCategory, Product, Event, Form
import json


# Create your views here.
@require_http_methods(["GET"])
def getCatalog(request, cc_id):
    cc_id = int(cc_id)
    try:
        catalog = CatalogCategory.objects.get(id=cc_id)
    except CatalogCategory.DoesNotExist:
        return HttpResponseNotFound()
    return JsonResponse(list(Product.objects.all().filter(category=cc_id).values()), safe=False)

@require_http_methods(["GET"])
def getProduct(request, p_id):
    p_id = int(p_id)
    try:
        product = Product.objects.get(id=p_id)
    except Product.DoesNotExist:
        return HttpResponseNotFound()
    return JsonResponse(model_to_dict(product))

@require_http_methods(["GET", "POST", "DELETE"])
def productList(request, p_id):
    p_id = int(p_id)
    try:
        product = Product.objects.get(id=p_id)
    except Product.DoesNotExist:
        return HttpResponseNotFound()
    #if request.session['order']:
    return HttpResponseNotFound()

@require_http_methods(["GET"])
def getProductEvents(request, p_id):
    p_id = int(p_id)
    try:
        product = Product.objects.get(id=p_id)
    except Product.DoesNotExist:
        return HttpResponseNotFound()
    return JsonResponse(list(Event.objects.all().filter(product=p_id).values()), safe=False)

@require_http_methods(["GET"])
def getEventForms(request, e_id):
    e_id = int(e_id)
    try:
        event = Event.objects.get(id=e_id)
    except Event.DoesNotExist:
        return HttpResponseNotFound()
    return JsonResponse(list(Form.objects.all().filter(event=e_id).values()), safe=False)
