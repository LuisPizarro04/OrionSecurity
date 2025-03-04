from rest_framework import serializers
from .models import *


class NovedadDiariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = NovedadDiaria
        fields = '__all__'


class ReporteIncidenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReporteIncidente
        fields = '__all__'


class ReporteGeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReporteGeneral
        fields = '__all__'
