from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from sultan.models import Category, Product


def index(request):
    return render(request, 'sultan/index.html')

def catalog(request, gender_slug, catalog_slug=None):
    if catalog_slug is None:
        return render(request, 'sultan/gender.html', {'gender_slug': gender_slug, 'cats' : Category.objects.filter(gender=gender_slug)})
    else:
        return render(request, 'sultan/catalog.html', {'gender_slug': gender_slug, 'category_slug': catalog_slug, 'products' : Product.objects.filter(category__id= Category.objects.get(slug=catalog_slug).id)})

def good(request, good_slug):
    return render(request, 'sultan/good.html', {'good': Product.objects.get(slug=good_slug)})

def contacts(request):
    return render(request, 'sultan/contacts.html')

def search(request):
    return HttpResponse('hello from search')

def cart(request):
    return HttpResponse('hello from cart')