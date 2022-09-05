from rest_framework import serializers as drf_serializers

from drf_store.core.models import Order, Product


class ProductListSerializer(drf_serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'price',
        )


class OrderListSerializer(drf_serializers.ModelSerializer):
    products = ProductListSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = (
            'id',
            'date',
            'products',
        )


class OrderCreateUpdateRetrieveSerializer(drf_serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            'date',
            'products',
        )


class ProductCreateUpdateRetrieveSerializer(drf_serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'title',
            'price',
        )
