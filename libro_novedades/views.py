from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from .serializers import *
from rest_framework.permissions import IsAuthenticated


# Create your views here.


class NovedadDiariaViewSet(viewsets.ModelViewSet):
    queryset = NovedadDiaria.objects.all()
    serializer_class = NovedadDiariaSerializer
    permission_classes = [IsAuthenticated]


class ReporteIncidenteViewSet(viewsets.ModelViewSet):
    queryset = ReporteIncidente.objects.all()
    serializer_class = ReporteIncidenteSerializer
    permission_classes = [IsAuthenticated]


class ReporteGeneralViewSet(viewsets.ModelViewSet):
    queryset = ReporteGeneral.objects.all()
    serializer_class = ReporteGeneralSerializer
    permission_classes = [IsAuthenticated]
