from django.db import models
from django.utils.translation import gettext_lazy as _


class PersonaAcceso(models.Model):
    TIPO_PERSONA_CHOICES = [
        ('empleado', 'Empleado'),
        ('proveedor', 'Proveedor'),
        ('visitante', 'Visitante'),
    ]

    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    identificacion = models.CharField(max_length=50, unique=True, verbose_name="Número de identificación")
    tipo_persona = models.CharField(max_length=10, choices=TIPO_PERSONA_CHOICES, verbose_name="Tipo de persona")
    empresa = models.CharField(max_length=100, blank=True, null=True, verbose_name="Empresa (si aplica)")

    def __str__(self):
        return f"{self.nombre} - {self.tipo_persona}"

    class Meta:
        verbose_name = "Persona Autorizada"
        verbose_name_plural = "Personas Autorizadas"
        ordering = ['nombre']


class RegistroAcceso(models.Model):
    METODO_VERIFICACION_CHOICES = [
        ('qr', 'Código QR'),
        ('pin', 'PIN'),
        ('credencial', 'Credencial'),
    ]

    persona = models.ForeignKey(PersonaAcceso, on_delete=models.CASCADE, verbose_name="Persona")
    fecha_hora_entrada = models.DateTimeField(auto_now_add=True, verbose_name="Fecha y hora de entrada")
    fecha_hora_salida = models.DateTimeField(blank=True, null=True, verbose_name="Fecha y hora de salida")
    metodo_verificacion = models.CharField(max_length=15, choices=METODO_VERIFICACION_CHOICES,
                                           verbose_name="Método de verificación")
    autorizado_por = models.CharField(max_length=100, blank=True, null=True, verbose_name="Autorizado por")

    def __str__(self):
        return f"{self.persona} - Entrada: {self.fecha_hora_entrada}"

    class Meta:
        verbose_name = "Registro de Acceso"
        verbose_name_plural = "Registros de Acceso"
        ordering = ['-fecha_hora_entrada']


class RegistroVehiculo(models.Model):
    persona = models.ForeignKey(PersonaAcceso, on_delete=models.CASCADE, verbose_name="Conductor")
    patente = models.CharField(max_length=10, verbose_name="Patente del vehículo")
    tipo_vehiculo = models.CharField(max_length=50, verbose_name="Tipo de vehículo")
    fecha_hora_entrada = models.DateTimeField(auto_now_add=True, verbose_name="Fecha y hora de entrada")
    fecha_hora_salida = models.DateTimeField(blank=True, null=True, verbose_name="Fecha y hora de salida")
    autorizado_por = models.CharField(max_length=100, blank=True, null=True, verbose_name="Autorizado por")

    def __str__(self):
        return f"{self.patente} - Entrada: {self.fecha_hora_entrada}"

    class Meta:
        verbose_name = "Registro de Vehículo"
        verbose_name_plural = "Registros de Vehículos"
        ordering = ['-fecha_hora_entrada']
