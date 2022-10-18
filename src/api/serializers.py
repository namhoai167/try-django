from rest_framework import serializers

from products.models import (
    Product
)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'category',
            'manufacturer',
            'name',
            'description',
            'price',
            'get_absolute_url',
        )