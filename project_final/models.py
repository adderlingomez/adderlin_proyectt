from django.db import models
from django.utils import timezone


# Create your models here.

#modelo principal de la base de datos que incluye una foto
class apostadores(models.Model):
    nombre_apostador = models.CharField(max_length=100)
    edad = models.IntegerField(null= True)
    fecha_inscripcion = models.DateField(default=timezone.now)
    foto = models.ImageField(null = True, blank=True)

    def __str__(self):
      return self.nombre_apostador



class Caracteristica_apostadores(models.Model):
    numero_juegos = models.IntegerField(default=0) #especifica el valor por defecto si se intenta ingresar un valor vacio
    veces_perdi = models.IntegerField()
    apostador = models.OneToOneField(apostadores, on_delete=models.CASCADE)
  
    def __str__(self):
        return self.numero_juegos

