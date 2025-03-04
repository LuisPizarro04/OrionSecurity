from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from .serializers import *
from rest_framework.permissions import IsAuthenticated


# Create your views here.


class TurnoViewSet(viewsets.ModelViewSet):
    queryset = Turno.objects.all()
    serializer_class = TurnoSerializer
    permission_classes = [IsAuthenticated]


class CambioTurnoViewSet(viewsets.ModelViewSet):
    queryset = CambioTurno.objects.all()
    serializer_class = CambioTurnoSerializer
    permission_classes = [IsAuthenticated]
