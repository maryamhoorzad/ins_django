from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from .models import Category, Product, Brand

def home_page(request, parent=None):
    categories = Category.objects.all()
    base_category = []
    for c in Category.objects.all():
        if not c.parent:
              base_category.append(c)    

    context = {
        'categories': base_category
    }

    return render(request, 'store/home.html', context)

    

def product_list(request, category_slug=None):
    
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'store/list.html', context)


def product_detail(request, id):
    
    product = get_object_or_404(Product, pk=id)
    context = {
        'product': product
    }
    return render(request, 'store/detail.html', context)
