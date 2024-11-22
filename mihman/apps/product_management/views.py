from django.shortcuts import render
from .models import Category,Subcategory, Product
from django.shortcuts import render, get_object_or_404

def product_detail(request, product_id):
    
    product = Product.objects.get(id=product_id)
    
    return render(request, 'product_management/product_detail.html', {'product': product})


def category_list(request, cat_id):
    
    category = Category.objects.get(id=cat_id)
    products = Product.objects.filter(category=category)
    
    all_categories = Category.objects.all().prefetch_related('subcategory_set')
    
    context = {'category': category,  'products': products, 'all_categories': all_categories}
    
    return render(request, 'product_management/product_list.html', context)


def sub_category_list(request, subcat_id):
    
    subcategory = get_object_or_404(Subcategory, id=subcat_id)
    products = Product.objects.filter(subcategory=subcategory)
    
    all_categories = Category.objects.all().prefetch_related('subcategory_set')
    
    context = {'subcategory': subcategory, 'products': products, 'all_categories': all_categories}
    
    return render(request, 'product_management/product_list.html', context)







