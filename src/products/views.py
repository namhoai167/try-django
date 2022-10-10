from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def home_view(*args, **kwargs):
    return HttpResponse('<h1>Welcome to homepage</h1>')

def products_display_view(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'products/product_display.html', context)

def product_detail_view(request, id):
    context = {
        'product': Product.objects.get(id=id)
    }
    return render(request, 'products/product_detail.html', context)
    