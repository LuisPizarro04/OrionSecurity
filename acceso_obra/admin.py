from django.contrib import admin
from .models import PersonaAcceso, RegistroAcceso, RegistroVehiculo


@admin.register(PersonaAcceso)
class PersonaAccesoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'identificacion', 'tipo_persona', 'empresa')
    list_filter = ('tipo_persona',)
    search_fields = ('nombre', 'identificacion', 'empresa')
    ordering = ('nombre',)


@admin.register(RegistroAcceso)
class RegistroAccesoAdmin(admin.ModelAdmin):
    list_display = ('persona', 'motivo_visita', 'fecha_hora_entrada', 'fecha_hora_salida', 'metodo_verificacion', 'autorizado_por')
    list_filter = ('metodo_verificacion',)
    search_fields = ('persona__nombre', 'autorizado_por')
    ordering = ('-fecha_hora_entrada',)


@admin.register(RegistroVehiculo)
class RegistroVehiculoAdmin(admin.ModelAdmin):
    list_display = ('persona', 'motivo_visita', 'patente', 'tipo_vehiculo', 'fecha_hora_entrada', 'fecha_hora_salida', 'autorizado_por')
    list_filter = ('tipo_vehiculo',)
    search_fields = ('persona__nombre', 'patente')
    ordering = ('-fecha_hora_entrada',)
