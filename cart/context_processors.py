from .models import Cart, CartItems
from .views import get_cart_id

def counter(request):
    items_count = 0
    if 'admin' in request.path:
        return {}
    else:    
        try:
            cart = Cart.objects.get(cart_id=get_cart_id(request))
            cart_items = CartItems.objects.all().filter(cart=cart)
            for cart_item in cart_items:
                items_count += cart_item.quantity
        except Cart.DoesNotExist:
            items_count = 0

    return dict(items_count=items_count)            