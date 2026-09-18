from django import forms
from .models import Evento

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        # ¡OJO! Quitamos 'fotos_extra' y 'imagen_portada'
        fields = ['documento', 'video', 'audio', 'nota_extra', 'titulo', 'fecha', 'hora', 'ubicacion', 'descripcion', 'contenido', 'cobertura']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'hora': forms.TimeInput(attrs={'type': 'time'}), 
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Hacemos todos los campos no obligatorios
        for field_name in self.fields:
            self.fields[field_name].required = False