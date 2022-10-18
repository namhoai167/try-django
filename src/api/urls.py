from django.urls import path
from .views import (
    ProductList,
    ProductDetail,
)

urlpatterns = [
    path('products/', ProductList.as_view(), name='api-products-list'),
    path('products/<int:id>', ProductDetail.as_view(), name='api-product-detail'),
]