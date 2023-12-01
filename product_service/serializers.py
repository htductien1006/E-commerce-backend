from rest_framework import serializers
from .models import Product

from . import services


class ProductSerializer(serializers.Serializer):
    class Meta:
        model = Product
        fields = ('name', )

class ProductDetailSerializer(serializers.Serializer):
    class Meta: 
        model = Product
        field = ('name', )