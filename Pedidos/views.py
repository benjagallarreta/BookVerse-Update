from decimal import Decimal
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Carrito.models import Cart
from Pedidos.models import Pedido, DetalleLibro
from Usuario.models import Usuario 
from Libro.models import Libro 

@login_required #Esto de aca debe de cambiar a clase
def realizar_compra(request):
    #funcion crear pedido
    detalles_carrito = Cart.objects.filter(usuario=request.user)    
    usuario = request.user
    correo = usuario.email
    monto_total = total = sum(detalle.precio for detalle in detalles_carrito)
    # creo el pedido
    pedido = Pedido.objects.create( 
        usuario=usuario,
        correo=correo,
        monto_total=monto_total
    )
    #funcion crear detalle de los libros
    for item in detalles_carrito:
        DetalleLibro.objects.create(
            libro=item.libro.titulo,
            precio=item.precio,
            cantidad=item.cantidad,
            pedido=pedido
        )
    Cart.objects.filter(usuario=request.user).delete()

    return redirect ('/')

@login_required
def mis_pedidos(request):
    usuario = request.user
    pedidos = Pedido.objects.filter(usuario=usuario)
    return render(request, 'mis_pedidos.html', {'pedidos': pedidos})

def detalle(request, numero_compra):
    pedido= numero_compra
    libros= DetalleLibro.objects.filter(pedido=pedido)
    return render(request, 'detalle.html', {'libros':libros} )




