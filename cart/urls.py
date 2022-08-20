from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('<int:product_id>/', views.add_to_cart, name='add_item'),
    path('details/', views.show_cart, name='details'),
    path('remove_item/<int:product_id>', views.remove_item, name='remove_item'),
    path('delete_item/<int:product_id>', views.delete_item, name='delete_item')
]
