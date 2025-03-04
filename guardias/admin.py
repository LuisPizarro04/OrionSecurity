from django.contrib import admin
from .models import Guardia


@admin.register(Guardia)
class GuardiaAdmin(admin.ModelAdmin):
    list_display = ('user', 'dni', 'fecha_contratacion', 'fecha_examen_medico')
    search_fields = ('user__username', 'dni')
    list_filter = ('fecha_contratacion', 'fecha_examen_medico')
