from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = "shop"

urlpatterns = [
    path('', views.products, name='index'),
    path('<slug:slug>/', views.products, name='products_by_category'),
    path('<slug:category_slug>/<slug:product_slug>/', views.product, name='product'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
