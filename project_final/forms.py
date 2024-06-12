from django import forms
from .models import Apostador, CaracteristicaApostador, ActualizacionApostador

class FormRegistrarApostador(forms.ModelForm):
    class Meta:
        model = Apostador
        fields = ['nombre', 'edad', 'foto']

class FormCaracteristicaApostadores(forms.ModelForm):
    class Meta:
        model = CaracteristicaApostador
        fields = ['numero_juegos', 'ganadas_del_apostador']  # Corregido el nombre del campo

        
class FormActualizarApostador(forms.ModelForm):
    class Meta:
        model = ActualizacionApostador
        fields = []

