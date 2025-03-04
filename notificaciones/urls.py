from django.db import router
from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'Notificacion', NotificacionViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
