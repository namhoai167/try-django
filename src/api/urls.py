# TODO Migrate to Router and Queryset

from django.urls import path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from .views import (
    ProductList,
    ProductDetail,
)

urlpatterns = [
    path('products/', ProductList.as_view(), name='api-products-list'),
    path('products/<int:id>', ProductDetail.as_view(), name='api-product-detail'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]