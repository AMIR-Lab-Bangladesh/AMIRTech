from django.shortcuts import render

from .serializers import UserSerializer
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from .models import User
from rest_framework.views import APIView


class UserDetailView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context
