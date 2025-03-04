from django.contrib import admin
from .models import Notificacion


@admin.register(Notificacion)
class NotificacionAdmin(admin.ModelAdmin):
    list_display = ('usuario_destino', 'tipo', 'estado', 'fecha_creacion')
    list_filter = ('tipo', 'estado')
    search_fields = ('usuario_destino__username', 'mensaje')
    ordering = ('-fecha_creacion',)
