from django.shortcuts import render
from rest_framework import viewsets, exceptions
from .models import Designation
from .serializers import DesignationSerailizer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView


class DesignationViewSet(viewsets.ModelViewSet):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerailizer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context

    def create_designation(self, request):
        if request.method == 'POST':
            serializer = DesignationSerailizer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors)
        else:
            raise exceptions.MethodNotAllowed(request.method)


class AllDesignationViewSet(ListAPIView):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerailizer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context

    @classmethod
    def get_extra_actions(cls):
        return []
