from rest_framework import serializers
from .models import ShoppingCart, CartItem


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'


class ShoppingCartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(
        many=True,
        read_only=True,
        source='cartitem_set' # noqa
    )

    class Meta:
        model = ShoppingCart
        fields = '__all__'
