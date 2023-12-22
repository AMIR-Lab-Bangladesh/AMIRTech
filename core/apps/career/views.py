from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Career
from .serializers import CareerSerializer
from rest_framework.views import APIView
from rest_framework import viewsets, exceptions
from rest_framework import viewsets, exceptions
from rest_framework.generics import ListAPIView


class CareerViewSet(viewsets.ModelViewSet):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context

    def create_designation(self, request):
        if request.method == 'POST':
            serializer = CareerSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors)
        else:
            raise exceptions.MethodNotAllowed(request.method)


class AllCareerViewSet(ListAPIView):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context

    @classmethod
    def get_extra_actions(cls):
        return []
