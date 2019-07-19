from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from .models import Category, Product, Brand

def home_page(request, parent=None):
    categories = Category.objects.all()
    for c in Category:
        if not c.parent:
            top_categpry = Product.objects.filter(category=category)
            
    context = {
        'categories': top_categpry
    }

    return render(request, 'store/product/home.html', context)

    

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    # products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'store/product/list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    context = {
        'product': product
    }
    return render(request, 'store/product/detail.html', context)
