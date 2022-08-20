from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Product
from .models import Cart, CartItems

# Create your views here.

def get_cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart    

def add_to_cart(request,product_id):
    product = Product.objects.get(id=product_id)
    # creating/getting current cart session
    try:
        cart = Cart.objects.get(cart_id=get_cart_id(request))
    except Cart.DoesNotExist:
       cart = Cart.objects.create(
            cart_id = get_cart_id(request)
       )
       cart.save()     
    # adding/updating items to the cart
    try:
        cart_item = CartItems.objects.get(product=product, cart=cart)
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity += 1
        cart_item.save()
    except CartItems.DoesNotExist:
        cart_item = CartItems.objects.create(
            product = product,
            cart= cart,
            quantity = 1
        )
        cart_item.save()

    return redirect('cart:details')

def remove_item(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        cart = Cart.objects.get(cart_id=get_cart_id(request))
        cart_item = CartItems.objects.get(product=product, cart=cart)
        if cart_item.quantity <= 1:
            cart_item.delete()
        else:
            cart_item.quantity -= 1
            cart_item.save()
    except Cart.DoesNotExist:
        pass

    return redirect('cart:details')     

def delete_item(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    try:
        cart = Cart.objects.get(cart_id=get_cart_id(request))
        cart_item = CartItems.objects.get(product=product, cart=cart)
        cart_item.delete()
    except Cart.DoesNotExist:
        pass    

    return redirect('cart:details')    

def show_cart(request):
    total = counter = 0
    cart_items = None
    try:
        cart = Cart.objects.get(cart_id=get_cart_id(request))
        cart_items = CartItems.objects.all().filter(cart = cart, active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            counter += cart_item.quantity
    except:
        pass    

    return render(request, 'cart.html', { 'cart_items': cart_items, 'total': total, 'counter': counter })