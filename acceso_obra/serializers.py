from rest_framework import serializers
from .models import *


class PersonaAccesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonaAcceso
        fields = '__all__'


class RegistroAccesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroAcceso
        fields = '__all__'


class RegistroVehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroVehiculo
        fields = '__all__'
