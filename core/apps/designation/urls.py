from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DesignationViewSet, AllDesignationViewSet

router = DefaultRouter()

router.register(r'', DesignationViewSet, basename='designation')

urlpatterns = [
    path('', include(router.urls)),
    path(
        'designation/', DesignationViewSet.as_view({'get': 'retrieve'}), name='create_designation'),
    path(
        'list/all/', AllDesignationViewSet.as_view(), name='all_designation'),

]
