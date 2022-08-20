from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from shop.models import Product
from django.db.models import Q
# Create your views here.

def search_results(request):
    products_list = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        products_list = Product.objects.all().filter(Q(name__icontains=query) | Q(description__icontains=query))

    paginator = Paginator(products_list, 6) 
    try:
        page = int(request.GET.get('page', 1))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)         

    return render(request, 'search.html', { 'query': query, 'products': products })     
