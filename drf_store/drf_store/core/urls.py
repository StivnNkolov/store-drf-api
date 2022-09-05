from django.urls import path
from rest_framework import routers

from drf_store.core.views.crud_views import ProductsListAPIView, OrdersListAPIView, OrderCreateUpdateDeleteViewSet, \
    ProductCreateUpdateDeleteViewSet
from drf_store.core.views.report_views import OrderReportAPIView

router = routers.SimpleRouter()
router.register(r'orders', OrderCreateUpdateDeleteViewSet, basename='order')
router.register(r'products', ProductCreateUpdateDeleteViewSet, basename='product')

urlpatterns = [
                  path('products_list/', ProductsListAPIView.as_view(), name='products list'),
                  path('orders_list/', OrdersListAPIView.as_view(), name='orders list'),
                  path('stats/', OrderReportAPIView.as_view(), name='report')
              ] + router.urls
