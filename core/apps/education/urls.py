from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EducationViewSet, AllEducationViewSet

router = DefaultRouter()

router.register(r'', EducationViewSet, basename='education')

urlpatterns = [
    path('', include(router.urls)),
    path(
        'education/', EducationViewSet.as_view({'get': 'retrieve'}), name='create_education'),
    path(
        'list/all/', AllEducationViewSet.as_view(), name='education')
]
