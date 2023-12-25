from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CartViewSet, AllCartViewSet

router = DefaultRouter()

router.register(r'', CartViewSet, basename='cart')

urlpatterns = [
    path('', include(router.urls)),
    path(
        'cart/', CartViewSet.as_view({'get': 'retrieve'}), name='create_cart'),
    path(
        'list/all/', AllCartViewSet.as_view(), name='create-cart')
]
