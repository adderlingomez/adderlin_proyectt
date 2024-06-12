from django.db import models
from django.utils import timezone

class Apostador(models.Model):
    """
    Modelo principal de la base de datos que incluye una foto.
    """
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    foto = models.ImageField(upload_to='apostadores/', blank=True)

    def __str__(self):
        return self.nombre

class CaracteristicaApostador(models.Model):
    """
    Modelo para almacenar las características de un apostador.
    """
    apostador = models.OneToOneField(Apostador, on_delete=models.CASCADE, related_name='caracteristica')
    numero_juegos = models.IntegerField(default=0)
    ganadas_del_apostador = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.numero_juegos} juegos, {self.apostador.ganadas_del_apostador} ganadas"

class ActualizacionApostador(models.Model):
    """
    Modelo para registrar actualizaciones de un apostador.
    """
    apostador = models.ForeignKey(Apostador, on_delete=models.CASCADE, related_name='actualizaciones')
    ganadas = models.IntegerField(default=0)
    perdidas = models.IntegerField(default=0)
    fecha_actualización = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Ganadas: {self.ganadas}, Perdidas: {self.perdidas}"
