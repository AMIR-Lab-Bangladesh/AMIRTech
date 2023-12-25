from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SocialLinkViewSet, SocialLinkByIdViewSet

router = DefaultRouter()

router.register(r'', SocialLinkViewSet, basename='blog')

urlpatterns = [
    path('', include(router.urls)),
    path(
        'sociallink/', SocialLinkViewSet.as_view({'get': 'retrieve'}), name='create_socail_link'),
    path('sociallink/<int:id>/', SocialLinkByIdViewSet.as_view(),
         name='social-link-detail'),
]
