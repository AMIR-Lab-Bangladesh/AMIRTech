from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ApplicationViewSet, AllApplicationViewSet

router = DefaultRouter()

router.register(r'', ApplicationViewSet, basename='applicant')

urlpatterns = [
    path('', include(router.urls)),
    path(
        'applicant/', ApplicationViewSet.as_view({'get': 'retrieve'}), name='create_applicant'),
    path(
        'list/all/', AllApplicationViewSet.as_view(), name='create-applicant')
]
