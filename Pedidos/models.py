# models.py en la aplicación pedidos
import uuid
from django.db import models

from Libro.models import Libro
from Usuario.models import Usuario

class EstadoPedido(models.TextChoices): #los diferentes estados que puede tomar un pedido
    PENDIENTE = 'P', 'Pendiente'
    ENVIADO = 'N', 'Enviado'
    ENTREGADO = 'D', 'Entregado'
    CANCELADO = 'C', 'Cancelado'

class Pedido(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE) #clave foranea al usuario
    correo = models.EmailField()
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField(auto_now_add=True)
    estado = models.CharField( #estado del pedido, por default  es pendiente, puede cambiar a enviado o entregado
        max_length=2,
        choices=EstadoPedido.choices,
        default=EstadoPedido.PENDIENTE,
    )
    numero_compra = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)

class DetalleLibro(models.Model):
    libro = models.CharField(max_length=255) #titulo, no planeo cambiarlo 
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()
    pedido = models.ForeignKey(Pedido, related_name='detalle_libros', on_delete=models.CASCADE) # clave foranea al pedido