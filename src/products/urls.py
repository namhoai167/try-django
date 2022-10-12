from django.urls import path
from .views import products_display_view, product_detail_view

urlpatterns = [
    path('products/', products_display_view, name='products-display'),
    path('products/<int:id>', product_detail_view, name='product-detail'),
]