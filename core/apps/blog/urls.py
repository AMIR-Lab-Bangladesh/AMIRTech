from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogViewSet, AllBlogViewSet

router = DefaultRouter()

router.register(r'', BlogViewSet, basename='blog')

urlpatterns = [
    path('', include(router.urls)),
    path(
        'blog/', BlogViewSet.as_view({'get': 'retrieve'}), name='create_blog'),
    path(
        'list/all/', AllBlogViewSet.as_view(), name='create-blog')
]
