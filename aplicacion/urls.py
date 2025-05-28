from django.urls import path, include
from .views import (index, producto, administrador, detalleproducto, loginAdmin,
                    adminpedido, anadir, categoria, direcciones, editar, editarusuarios, pedidos,
                    perfil, recuperar, registro, totalusuarios, usuarios, carrito, marca,
                    agregarCarrito, eliminarCarrito, confirmarCompra, agregarUsuario, eliminarUsuario,
                    direccionesusuario, eliminardireccion, editardirecciones, agregardireccion, listaPedidos,
                    crearPedido, editarPedido, eliminarPedido, detallePedido,
                    agregardireccionusuario, editardireccionusuario, eliminardireccionusuario,
                    search_results, eliminarProducto
                    )
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index, name='index'),
    path('buscar/', search_results, name='search_results'),
    path('producto/<int:id>/', producto, name='producto'),
    path('administrador/', administrador, name='administrador'),
    path('detalleproducto/<int:id>', detalleproducto, name='detalleproducto'),
    path('adminpedido/', adminpedido, name='adminpedido'),
    path('anadir/', anadir, name='anadir'),
    path('categoria/<int:id>/', categoria, name='categoria'),
    path('marca/<int:id>/', marca, name='marca'),
    path('direcciones/<str:rut>', direcciones, name='direcciones'),
    path('agregardireccionusuario/<str:rut>',agregardireccionusuario, name="agregardireccionusuario"),
    path('editardireccionusuario/<int:id>',editardireccionusuario, name="editardireccionusuario"),
    path('eliminardireccionusuario/<int:id>',eliminardireccionusuario, name="eliminardireccionusuario"),
    path('editar/<int:id>', editar, name='editar'),
    path('usuarios/<str:rut>', usuarios, name='usuarios'),
    path('editarusuarios/<str:rut>', editarusuarios, name='editarusuarios'),
    path('agregarusuario/', agregarUsuario, name="agregarUsuario"),
    path('eliminarusuario/<str:rut>', eliminarUsuario, name="eliminarUsuario"),
    path('direccionesusuario/<str:rut>', direccionesusuario, name="direccionesusuario"),
    path('agregardireccion/<str:rut>', agregardireccion, name="agregardireccion"),
    path('eliminardireccion/<int:id>',eliminardireccion, name="eliminardireccion"),
    path('editardirecciones/<int:id>', editardirecciones, name="editardirecciones"),
    path('loginAdmin/', loginAdmin, name='loginAdmin'),
    path('pedidos/<str:rut>', pedidos, name='pedidos'),
    path('perfil/<str:rut>', perfil, name='perfil'),
    path('recuperar/', recuperar, name='recuperar'),
    path('registro/', registro, name='registro'),
    path('totalusuarios/', totalusuarios, name='totalusuarios'),
    path('carrito/', carrito, name='carrito'),
    path('carrito/<int:id_zapatilla>/', agregarCarrito, name='agregarCarrito'),
    path('carrito/<int:id_item>', eliminarCarrito, name='eliminarCarrito'),
    path('compraconfirmada/', confirmarCompra, name="confirmarCompra"),
    path('listaPedidos/', listaPedidos, name='listaPedidos'),
    path('crearPedido/', crearPedido, name='crearPedido'),
    path('editarPedido/<int:pk>/', editarPedido, name='editarPedido'),
    path('eliminarPedido/<int:pk>/', eliminarPedido, name='eliminarPedido'),
    path('detallePedido/<int:pk>/', detallePedido, name='detallePedido'),
    path('eliminarProducto/<int:id>/', eliminarProducto, name='eliminarProducto'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
