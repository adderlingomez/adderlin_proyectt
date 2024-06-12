from django.contrib import admin
from .models import Apostador, CaracteristicaApostador, ActualizacionApostador

# Register your models here.
admin.site.register(Apostador)
admin.site.register(CaracteristicaApostador)
admin.site.register(ActualizacionApostador)

