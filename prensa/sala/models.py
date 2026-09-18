from django.db import models

class Evento(models.Model):
    titulo = models.CharField(max_length=500, blank=True, null=True, verbose_name="Título del Evento")
    fecha = models.DateField(blank=True, null=True, verbose_name="Fecha")
    hora = models.TimeField(blank=True, null=True, verbose_name="Hora")
    ubicacion = models.CharField(max_length=200, blank=True, null=True, verbose_name="Ubicación")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción Corta")
    contenido = models.TextField(blank=True, null=True, verbose_name="Cuerpo Completo de la Noticia")
    cobertura = models.CharField(max_length=200, blank=True, null=True, verbose_name="Cobertura")
    
    # --- MULTIMEDIA (La portada sigue aquí para que el Word la llene, pero no la pediremos manual) ---
    imagen_portada = models.ImageField(upload_to='agenda_fotos/portadas/', blank=True, null=True, verbose_name="Foto de Portada")
    documento = models.FileField(upload_to='agenda_documentos/', blank=True, null=True, verbose_name="Documento Word (.docx)")
    
    # --- NUEVOS CAMPOS MULTIMEDIA ---
    video = models.FileField(upload_to='agenda_videos/', blank=True, null=True, verbose_name="Video del Evento")
    audio = models.FileField(upload_to='agenda_audios/', blank=True, null=True, verbose_name="Audio / Entrevista")
    nota_extra = models.FileField(upload_to='agenda_notas/', blank=True, null=True, verbose_name="Nota / PDF Adicional")

    class Meta:
        verbose_name = "Evento de Agenda"
        verbose_name_plural = "Eventos de Agenda"
        ordering = ['-fecha', 'hora']

    def __str__(self):
        return f"{self.fecha} - {self.titulo}"

# NUEVA TABLA PARA MÚLTIPLES FOTOS
class ImagenEvento(models.Model):
    evento = models.ForeignKey(Evento, related_name='galeria', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='agenda_fotos/galeria/')