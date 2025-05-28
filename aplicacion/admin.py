from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


class CustomUserAdmin(UserAdmin):
    model = Usuario
    list_display = ('correo', 'nombre', 'apellido', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('correo', 'nombre', 'apellido', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('correo', 'nombre', 'apellido', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('correo',)
    ordering = ('correo',)


admin.site.register(Usuario, CustomUserAdmin)


class AdmUsuario(admin.ModelAdmin):
    list_display = ['rut', 'nombre', 'apellido',
                    'contrasenia', 'correo', 'fnac']
    list_editable = ['nombre', 'apellido', 'fnac', 'contrasenia', 'correo']


class AdmZapatilla(admin.ModelAdmin):
    list_display = ['id', 'marca', 'modelo', 'precio', 'descripcion']
    list_editable = ['marca', 'modelo', 'precio', 'descripcion']


class AdmDireccion(admin.ModelAdmin):
    list_display = ['id', 'calle', 'numero', 'comuna']
    list_editable = ['calle', 'numero', 'comuna']


class AdmMarca(admin.ModelAdmin):
    list_display = ['id', 'nombre']
    list_editable = ['nombre']


class AdmPedido(admin.ModelAdmin):
    list_display = ['id', 'fecha', 'cliente', 'direccion', 'estado', 'total']


class AdmCategoria(admin.ModelAdmin):
    list_display = ['id', 'nombre']
    list_editable = ['nombre']


class AdmPedidoZapatilla(admin.ModelAdmin):
    list_display = ['id', 'pedido', 'zapatilla', 'cantidad']


class AdmAdministrador(admin.ModelAdmin):
    list_display = ['rut', 'nombre', 'apellido', 'contrasenia', 'correo']
    list_editable = ['nombre', 'apellido', 'contrasenia', 'correo']


class AdmStockZapatillas(admin.ModelAdmin):
    list_display = ['id', 'zapatilla', 'talla', 'cantidad']
    list_editable = ['zapatilla', 'talla', 'cantidad']
    list_display_links = ['id']


# Register your models here.
admin.site.register(Zapatilla, AdmZapatilla)
admin.site.register(Direccion, AdmDireccion)
admin.site.register(Marca, AdmMarca)
admin.site.register(Pedido, AdmPedido)
admin.site.register(Categoria, AdmCategoria)
admin.site.register(PedidoZapatilla, AdmPedidoZapatilla)
admin.site.register(Administrador, AdmAdministrador)
admin.site.register(StockZapatilla, AdmStockZapatillas)
