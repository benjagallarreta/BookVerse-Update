from django.db import models
from Usuario.models import Usuario
from Libro.models import Libro

class Reseña(models.Model):
    fecha = models.DateField()
    estrellas = models.CharField(max_length=5)
    comentario = models.TextField(max_length=500)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, default=None)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='reseñas')