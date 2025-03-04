from django.db import router
from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'NovedadDiaria', NovedadDiariaViewSet)
router.register(r'ReporteIncidente', ReporteIncidenteViewSet)
router.register(r'ReporteGeneral', ReporteGeneralViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
