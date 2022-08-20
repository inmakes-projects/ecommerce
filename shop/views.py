from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from .models import Category, Product



# Create your views here.

def index(request):
    return render(request, 'index.html')

def products(request, slug=None):
    category = None
    products_list = None
    if slug != None:
        category = get_object_or_404(Category, slug=slug)
        products_list = Product.objects.all().filter(category=category, available=True)
    else:
        products_list = Product.objects.all().filter(available=True)    
    paginator = Paginator(products_list, 6)
    
    try:
        page = int(request.GET.get('page', 1))
    except:
        page = 1
       
    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)            

    return render(request, 'products.html', { 'category': category, 'products': products})


def product(request, category_slug, product_slug):
    try:
        product = Product.objects.get(slug=product_slug, category__slug=category_slug)
    except Exception as e:
        raise e

    return render(request, 'product.html', { 'product': product })        

