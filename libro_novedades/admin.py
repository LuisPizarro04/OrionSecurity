from django.contrib import admin
from .models import NovedadDiaria, ReporteIncidente, ReporteGeneral


@admin.register(NovedadDiaria)
class NovedadDiariaAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'descripcion', 'reportado_por')
    search_fields = ('descripcion', 'reportado_por')
    ordering = ('-fecha',)


@admin.register(ReporteIncidente)
class ReporteIncidenteAdmin(admin.ModelAdmin):
    list_display = ('fecha_reporte', 'descripcion', 'reportado_por', 'estado')
    list_filter = ('estado',)
    search_fields = ('descripcion', 'reportado_por')
    ordering = ('-fecha_reporte',)


@admin.register(ReporteGeneral)
class ReporteGeneralAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'elaborado_por', 'resumen')
    search_fields = ('resumen', 'elaborado_por')
    ordering = ('-fecha',)
