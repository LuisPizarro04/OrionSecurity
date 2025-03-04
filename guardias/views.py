from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from .serializers import *
from rest_framework.permissions import IsAuthenticated


# Create your views here.


class GuardiaViewSet(viewsets.ModelViewSet):
    queryset = Guardia.objects.all()
    serializer_class = GuardiaSerializer
    permission_classes = [IsAuthenticated]