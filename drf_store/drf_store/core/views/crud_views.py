from rest_framework import generics as generic_API_views

from common.mixins import CreateRetrieveUpdateDestroyViewSet
from common.paginators import CustomPaginator
from drf_store.core.models import Product, Order
from drf_store.core.serializers.crud_serializers import ProductListSerializer, OrderListSerializer, \
    OrderCreateUpdateRetrieveSerializer, \
    ProductCreateUpdateRetrieveSerializer


class ProductsListAPIView(generic_API_views.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    pagination_class = CustomPaginator


class OrdersListAPIView(generic_API_views.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer
    pagination_class = CustomPaginator


class OrderCreateUpdateDeleteViewSet(CreateRetrieveUpdateDestroyViewSet):
    queryset = Order.objects.prefetch_related('products')

    def get_serializer_class(self):
        if self.action in ('retrieve',):
            return OrderListSerializer
        return OrderCreateUpdateRetrieveSerializer


class ProductCreateUpdateDeleteViewSet(CreateRetrieveUpdateDestroyViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductCreateUpdateRetrieveSerializer

    def get_serializer_class(self):
        if self.action in ('retrieve',):
            return ProductListSerializer
        return ProductCreateUpdateRetrieveSerializer
