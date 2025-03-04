from django.db.models.signals import post_save
from django.dispatch import receiver
from libro_novedades.models import ReporteIncidente
from .utils import enviar_notificacion


@receiver(post_save, sender=ReporteIncidente)
def notificar_incidente(sender, instance, created, **kwargs):
    if created:
        mensaje = f"Se ha registrado un nuevo incidente:\n\n{instance.descripcion}"
        enviar_notificacion(instance.reportado_por, 'incidente', mensaje)
