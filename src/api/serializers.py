from rest_framework import serializers

from products.models import (
    Product
)

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField('get_category')
    manufacturer = serializers.SerializerMethodField('get_manufacturer')

    def get_category(self, obj):
        return [cate.name for cate in obj.category.all()]

    def get_manufacturer(self, obj):
        return obj.manufacturer.name

    class Meta:
        model = Product
        fields = (
            'id',
            'category',
            'manufacturer',
            'name',
            'description',
            'price'
        )