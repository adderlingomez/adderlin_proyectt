from django import forms
from .models import apostadores, Caracteristica_apostadores



class FormRegistrarApostador(forms.ModelForm):
    class Meta:
        model = apostadores

        fields = ['nombre_apostador', 'edad', 'foto']

class FormCaracteristicaApostadores(forms.ModelForm):
    class Meta:
        model = Caracteristica_apostadores

        fields = ['numero_juegos', 'veces_perdi']