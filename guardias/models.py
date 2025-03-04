from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Guardia(models.Model):
    TIPO_CONTRATO_CHOICES = [
        ('plazo_fijo', 'Plazo Fijo'),
        ('indefinido', 'Indefinido'),
        ('part_time', 'Part-Time'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='guardia')
    dni = models.CharField(max_length=20, unique=True)
    tipo_contrato = models.CharField(max_length=20, choices=TIPO_CONTRATO_CHOICES, verbose_name="Tipo de contrato")
    certificaciones = models.TextField(blank=True, null=True)
    fecha_examen_medico = models.DateField(blank=True, null=True)
    equipamiento_asignado = models.TextField(blank=True, null=True)  # Lista de equipamiento
    fecha_contratacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Guardia: {self.user.username} - DNI: {self.dni}"
