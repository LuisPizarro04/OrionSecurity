from django.db import router
from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'PersonaAcceso', PersonaAccesoViewSet)
router.register(r'RegistroAcceso', RegistroAccesoViewSet)
router.register(r'RegistroVehiculo', RegistroVehiculoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
