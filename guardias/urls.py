from django.db import router
from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'Guardia', GuardiaViewSet)


urlpatterns = [
    path('', include(router.urls)),
]