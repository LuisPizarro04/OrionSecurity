from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from .serializers import *
from rest_framework.permissions import IsAuthenticated


# Create your views here.


class PersonaAccesoViewSet(viewsets.ModelViewSet):
    queryset = PersonaAcceso.objects.all()
    serializer_class = PersonaAccesoSerializer
    permission_classes = [IsAuthenticated]


class RegistroAccesoViewSet(viewsets.ModelViewSet):
    queryset = RegistroAcceso.objects.all()
    serializer_class = RegistroAccesoSerializer
    permission_classes = [IsAuthenticated]


class RegistroVehiculoViewSet(viewsets.ModelViewSet):
    queryset = RegistroVehiculo.objects.all()
    serializer_class = RegistroVehiculoSerializer
    permission_classes = [IsAuthenticated]
