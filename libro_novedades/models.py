from django.db import models
from django.utils.translation import gettext_lazy as _


class NovedadDiaria(models.Model):
    fecha = models.DateField(auto_now_add=True, verbose_name="Fecha")
    descripcion = models.TextField(verbose_name="Descripción de la novedad")
    reportado_por = models.CharField(max_length=100, verbose_name="Reportado por")
    imagen = models.ImageField(upload_to='novedades/', blank=True, null=True, verbose_name="Imagen adjunta")

    def __str__(self):
        return f"Novedad - {self.fecha}: {self.descripcion[:50]}"

    class Meta:
        verbose_name = "Novedad Diaria"
        verbose_name_plural = "Novedades Diarias"
        ordering = ['-fecha']


class ReporteIncidente(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En progreso'),
        ('resuelto', 'Resuelto'),
    ]

    fecha_reporte = models.DateTimeField(auto_now_add=True, verbose_name="Fecha del reporte")
    descripcion = models.TextField(verbose_name="Descripción del incidente")
    reportado_por = models.CharField(max_length=100, verbose_name="Reportado por")
    estado = models.CharField(max_length=15, choices=ESTADO_CHOICES, default='pendiente',
                              verbose_name="Estado del incidente")
    evidencia = models.FileField(upload_to='incidentes/', blank=True, null=True,
                                 verbose_name="Evidencia (imagen/documento)")
    comentarios = models.TextField(blank=True, null=True, verbose_name="Comentarios adicionales")

    def __str__(self):
        return f"Incidente ({self.get_estado_display()}) - {self.fecha_reporte}: {self.descripcion[:50]}"

    class Meta:
        verbose_name = "Reporte de Incidente"
        verbose_name_plural = "Reportes de Incidentes"
        ordering = ['-fecha_reporte']


class ReporteGeneral(models.Model):
    fecha = models.DateField(auto_now_add=True, verbose_name="Fecha del reporte")
    resumen = models.TextField(verbose_name="Resumen del día")
    elaborado_por = models.CharField(max_length=100, verbose_name="Elaborado por")
    archivo_adjunto = models.FileField(upload_to='reportes_generales/', blank=True, null=True,
                                       verbose_name="Archivo adjunto")

    def __str__(self):
        return f"Reporte General - {self.fecha}"

    class Meta:
        verbose_name = "Reporte General"
        verbose_name_plural = "Reportes Generales"
        ordering = ['-fecha']
