from django.contrib import admin
from django.urls import path
from Home.views import HomeView, LibrosPorGeneroView
from Usuario.views import LoginView, CustomLogoutView, RegistroView, UsuarioDetailView, UsuarioUpdateView
from Pedidos.views import mis_pedidos, realizar_compra, detalle
from Carrito.views import CarritoView,AgregarLibroView,EliminarLibroView,RestarLibroView,LimpiarCarritoView,CheckOutView,PaymentView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),   
    path('libros/<str:genero>/', LibrosPorGeneroView.as_view(), name='libros_por_genero'),
    
    path('perfil/', UsuarioDetailView.as_view(), name='perfil_usuario'),
    path('editar-perfil/', UsuarioUpdateView.as_view(), name='editar_usuario'),
    path('registro/', RegistroView.as_view(), name='registro'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),

    path('mis_pedidos/', mis_pedidos, name='mis_pedidos'),
    path('generar_pedido/',realizar_compra,name='generar_pedido'),
    path('detalle/<uuid:numero_compra>/', detalle, name='detalle'),

    path('carrito/', CarritoView.as_view(), name='carrito'),
    path('agregar/<str:isbn>/', AgregarLibroView.as_view(), name='agregar_libro'),
    path('eliminar/<str:isbn>/', EliminarLibroView.as_view(), name='eliminar_libro'),
    path('restar/<str:isbn>/', RestarLibroView.as_view(), name='restar_libro'),
    path('limpiar/', LimpiarCarritoView.as_view(), name='limpiar_carrito'),
    path('checkout/', CheckOutView.as_view(), name='checkout'),
    path('pago/', PaymentView.as_view(), name='pago'),
]
