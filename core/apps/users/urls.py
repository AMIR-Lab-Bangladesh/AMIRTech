from django.urls import path
from .views import UserDetailView
from .models import User

urlpatterns = [
    path('user/<id>/', UserDetailView.as_view()),
]
