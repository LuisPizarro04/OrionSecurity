from rest_framework import serializers
from .models import *


class GuardiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guardia
        fields = '__all__'