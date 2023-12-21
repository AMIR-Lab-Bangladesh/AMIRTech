from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Blog
from .serializers import BlogSerializer
from rest_framework.views import APIView
from rest_framework import viewsets, exceptions
from rest_framework import viewsets, exceptions
from rest_framework.generics import ListAPIView


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context

    def create_designation(self, request):
        if request.method == 'POST':
            serializer = BlogSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors)
        else:
            raise exceptions.MethodNotAllowed(request.method)


class AllBlogViewSet(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context

    @classmethod
    def get_extra_actions(cls):
        return []
