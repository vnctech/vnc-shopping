from django.shortcuts import render
from .models import Category, Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_management/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'product_management/product_detail.html', {'product': product})



