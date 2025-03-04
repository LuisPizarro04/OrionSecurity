from rest_framework import serializers
from .models import *


class TurnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turno
        fields = '__all__'


class CambioTurnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CambioTurno
        fields = '__all__'
