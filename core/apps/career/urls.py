from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CareerViewSet, AllCareerViewSet

router = DefaultRouter()

router.register(r'', CareerViewSet, basename='career')

urlpatterns = [
    path('', include(router.urls)),
    path(
        'career/', CareerViewSet.as_view({'get': 'retrieve'}), name='create_career'),
    path(
        'list/all/', AllCareerViewSet.as_view(), name='create-career')
]
