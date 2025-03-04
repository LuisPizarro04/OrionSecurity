from django.db import router
from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'Turno', TurnoViewSet)
router.register(r'CambioTurno', CambioTurnoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
