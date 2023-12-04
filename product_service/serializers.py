from rest_framework import serializers
from .models import Product, CartItems


class ProductSerializer(serializers.Serializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'image_url',
                  'uom_name', 'uom_quantitive')


class ProductDetailSerializer(serializers.Serializer):
    class Meta:
        model = Product
        field = ('name', 'description', 'price',
                 'uom_name', 'uom_quantitive', 'image_url', 'category_id', 'inventory_id', 'promotion_id')


class CartItemSerializer(serializers.Serializer):
    class Meta:
        model = CartItems
        field = ('quantity', 'product_id')
