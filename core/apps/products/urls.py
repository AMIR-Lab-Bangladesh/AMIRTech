from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, AllProductViewSet

router = DefaultRouter()

router.register(r'', ProductViewSet, basename='blog')

urlpatterns = [
    path('', include(router.urls)),
    path(
        'product/', ProductViewSet.as_view({'get': 'retrieve'}), name='create_product'),
    path(
        'list/all/', AllProductViewSet.as_view(), name='create-product')
]
