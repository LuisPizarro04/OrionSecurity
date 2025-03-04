from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Notificacion(models.Model):
    TIPO_CHOICES = [
        ('turno', 'Cambio de Turno'),
        ('incidente', 'Reporte de Incidente'),
        ('acceso', 'Acceso No Autorizado'),
        ('general', 'Notificación General'),
    ]

    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('enviado', 'Enviado'),
        ('leido', 'Leído'),
    ]

    usuario_destino = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario destinatario")
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, verbose_name="Tipo de Notificación")
    mensaje = models.TextField(verbose_name="Mensaje de la notificación")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='pendiente', verbose_name="Estado")
    metodo_envio = models.CharField(max_length=10, choices=[('email', 'Email'), ('sms', 'SMS')], default='email',
                                    verbose_name="Método de envío")

    def __str__(self):
        return f"Notificación ({self.get_tipo_display()}) para {self.usuario_destino.username} - {self.get_estado_display()}"

    class Meta:
        verbose_name = "Notificación"
        verbose_name_plural = "Notificaciones"
        ordering = ['-fecha_creacion']
