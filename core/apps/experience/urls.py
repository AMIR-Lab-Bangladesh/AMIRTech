from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExperienceViewSet, AllExperienceViewSet

router = DefaultRouter()

router.register(r'', ExperienceViewSet, basename='experience')

urlpatterns = [
    path('', include(router.urls)),
    path(
        'experience/', ExperienceViewSet.as_view({'get': 'retrieve'}), name='create_experience'),
    path(
        'list/all/', AllExperienceViewSet.as_view(), name='all-experience')
]
