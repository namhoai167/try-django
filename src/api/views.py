from django.http import Http404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from drf_spectacular.utils import extend_schema

from products.models import Product
from .serializers import ProductSerializer

# Create your views here.
class ProductList(APIView):

    def get(self, request):
        category = request.query_params.get('category')
        manufacturer = request.query_params.get('manufacturer')
        if category is not None and manufacturer is not None:
            products = Product.objects.filter(category__name=category, manufacturer__name=manufacturer)
        elif category is not None and manufacturer is None:
            products = Product.objects.filter(category__name=category)
        elif category is None and manufacturer is not None:
            products = Product.objects.filter(manufacturer__name=manufacturer)
        else:
            products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetail(APIView):

    def get_object(self, id):
        try:
            return Product.objects.get(id=id)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, id):
        product = self.get_object(id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    @extend_schema(
        request=ProductSerializer,
        responses={200: ProductSerializer},
    )
    def put(self, request, id):
        product = self.get_object(id)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        product = self.get_object(id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
