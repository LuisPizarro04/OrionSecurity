from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from .serializers import *
from rest_framework.permissions import IsAuthenticated


# Create your views here.


class NotificacionViewSet(viewsets.ModelViewSet):
    queryset = Notificacion.objects.all()
    serializer_class = NotificacionSerializer
    permission_classes = [IsAuthenticated]
