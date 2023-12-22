from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Tools
from .serializers import ToolsSerializer
from rest_framework.views import APIView
from rest_framework import viewsets, exceptions
from rest_framework import viewsets, exceptions
from rest_framework.generics import ListAPIView


class ToolsViewSet(viewsets.ModelViewSet):
    queryset = Tools.objects.all()
    serializer_class = ToolsSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context

    def create_designation(self, request):
        if request.method == 'POST':
            serializer = ToolsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors)
        else:
            raise exceptions.MethodNotAllowed(request.method)


class AllBlogViewSet(ListAPIView):
    queryset = Tools.objects.all()
    serializer_class = ToolsSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context

    @classmethod
    def get_extra_actions(cls):
        return []
