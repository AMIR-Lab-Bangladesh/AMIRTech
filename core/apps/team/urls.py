from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeamViewSet

router = DefaultRouter()

router.register(r'', TeamViewSet, basename='teamviewset')

urlpatterns = [
    path('', include(router.urls)),
    path(
        'team/', TeamViewSet.as_view({'get': 'retrieve'}), name='teamviewset'),
]
