# Register your models here.


from django.contrib import admin

from .models import Turno, CambioTurno


@admin.register(Turno)
class TurnoAdmin(admin.ModelAdmin):
    list_display = ('guardia', 'fecha', 'hora_inicio', 'hora_fin', 'estado', 'asistencia_registrada')
    list_filter = ('fecha', 'estado', 'asistencia_registrada')
    search_fields = ('guardia__nombre', 'fecha')
    ordering = ('fecha', 'hora_inicio')
    fieldsets = (
        ('Detalles del Turno', {
            'fields': ('guardia', 'fecha', 'hora_inicio', 'hora_fin', 'estado')
        }),
        ('Asistencia', {
            'fields': ('asistencia_registrada', 'hora_entrada', 'hora_salida')
        }),
    )


@admin.register(CambioTurno)
class CambioTurnoAdmin(admin.ModelAdmin):
    list_display = ('turno_original', 'guardia_nuevo', 'fecha_solicitud', 'aprobado_por')
    list_filter = ('fecha_solicitud',)
    search_fields = ('turno_original__guardia__nombre', 'guardia_nuevo__nombre')
    ordering = ('-fecha_solicitud',)
