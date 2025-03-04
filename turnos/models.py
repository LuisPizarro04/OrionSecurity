from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from guardias.models import Guardia


class Turno(models.Model):
    ESTADO_TURNO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('completado', 'Completado'),
        ('cancelado', 'Cancelado'),
    ]

    guardia = models.ForeignKey(Guardia, on_delete=models.CASCADE, verbose_name="Guardia asignado")
    fecha = models.DateField(verbose_name="Fecha del turno")
    hora_inicio = models.TimeField(verbose_name="Hora de inicio")
    hora_fin = models.TimeField(verbose_name="Hora de término")
    estado = models.CharField(max_length=15, choices=ESTADO_TURNO_CHOICES, default='pendiente',
                              verbose_name="Estado del turno")

    asistencia_registrada = models.BooleanField(default=False, verbose_name="Asistencia registrada")
    hora_entrada = models.DateTimeField(blank=True, null=True, verbose_name="Hora de entrada")
    hora_salida = models.DateTimeField(blank=True, null=True, verbose_name="Hora de salida")

    def __str__(self):
        return f"{self.guardia} - {self.fecha} ({self.hora_inicio} - {self.hora_fin})"

    class Meta:
        verbose_name = "Turno"
        verbose_name_plural = "Turnos"
        ordering = ['fecha', 'hora_inicio']


class CambioTurno(models.Model):
    turno_original = models.ForeignKey(Turno, on_delete=models.CASCADE, related_name='cambios',
                                       verbose_name="Turno original")
    guardia_nuevo = models.ForeignKey(Guardia, on_delete=models.CASCADE, verbose_name="Guardia reemplazo")
    motivo = models.TextField(verbose_name="Motivo del cambio")
    aprobado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                     verbose_name="Aprobado por")
    fecha_solicitud = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de solicitud")

    def __str__(self):
        return f"Cambio de {self.turno_original} a {self.guardia_nuevo}"

    class Meta:
        verbose_name = "Cambio de Turno"
        verbose_name_plural = "Cambios de Turno"
        ordering = ['-fecha_solicitud']
