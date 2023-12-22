from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ToolsViewSet

router = DefaultRouter()

router.register(r'', ToolsViewSet, basename='blog')

urlpatterns = [
    path('', include(router.urls)),
    path(
        'tools/', ToolsViewSet.as_view({'get': 'retrieve'}), name='create_tools'),

]
