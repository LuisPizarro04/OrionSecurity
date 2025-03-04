from django.core.mail import send_mail
from django.conf import settings
from .models import Notificacion


def enviar_notificacion(usuario, tipo, mensaje, metodo='email'):
    """Crea y envía una notificación a un usuario."""

    notificacion = Notificacion.objects.create(
        usuario_destino=usuario,
        tipo=tipo,
        mensaje=mensaje,
        metodo_envio=metodo
    )

    if metodo == 'email':
        send_mail(
            subject=f"Notificación: {tipo}",
            message=mensaje,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[usuario.email],
            fail_silently=False,
        )
        notificacion.estado = 'enviado'
        notificacion.save()

    return notificacion
