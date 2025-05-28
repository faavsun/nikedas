from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

# Create your models here.

class Direccion(models.Model):
    calle = models.CharField(max_length=255, null=False)
    numero = models.IntegerField(null=False)
    detalle = models.CharField(max_length=255, null=True, verbose_name="Detalle o Departamento")
    comuna = models.CharField(max_length=255, null=False)
    region = models.CharField(max_length=255, null=False)

    def __str__(self):
        return f"{self.calle} {self.numero}, {self.detalle}, {self.comuna}, {self.region}"


class UsuarioManager(BaseUserManager):
    def create_user(self, correo, nombre, apellido, password=None, rut=None, **extra_fields):
        if not correo:
            raise ValueError('El correo electrónico es obligatorio')
        if not rut:
            raise ValueError('El RUT es obligatorio')
        correo = self.normalize_email(correo)
        user = self.model(correo=correo, nombre=nombre, apellido=apellido, rut=rut, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, correo, nombre, apellido, rut, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('telefono', '0000000000')
        extra_fields.setdefault('fnac', '1900-01-01')

        return self.create_user(correo, nombre, apellido, password, rut, **extra_fields)


class Usuario(AbstractBaseUser, PermissionsMixin):
    rut = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(unique=True)
    direcciones = models.ManyToManyField(Direccion)
    telefono = models.CharField(max_length=15, null=True, blank=True)
    fnac = models.DateField(verbose_name='Fecha de nacimiento')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['nombre', 'apellido', 'rut']

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.rut})"


class Marca(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre


class Zapatilla(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=50, null=False)
    precio = models.IntegerField(validators=[MinValueValidator(20000), MaxValueValidator(500000)],null=False)
    categoria = models.ManyToManyField(Categoria)
    descripcion = models.CharField(max_length=500, null=False)
    foto = models.ImageField(upload_to='zapatillas')

    def __str__(self):
        return f"{self.marca} -- {self.modelo}"
    
class StockZapatilla(models.Model):
    zapatilla = models.ForeignKey(Zapatilla, on_delete=models.CASCADE)
    talla = models.DecimalField(decimal_places=1, max_digits=3, null=False)
    cantidad = models.IntegerField(null=False, default=0)


class Carrito(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    zapatilla = models.ManyToManyField(Zapatilla, through='ItemCarrito')

    def __str__(self):
        return f"Carrito de {self.usuario}"


class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    zapatilla = models.ForeignKey(Zapatilla, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True, null=True)  # Hay que sacar el null

    def __str__(self):
        return f"{self.cantidad} - {self.zapatilla.modelo}"

    def precioTotal(self):
        return self.cantidad * self.zapatilla.precio


class Pedido(models.Model):
    cliente = models.ForeignKey('Usuario', on_delete=models.PROTECT)
    direccion = models.ForeignKey('Direccion', on_delete=models.PROTECT)

    # Definir opciones para el campo estado
    ESTADO_CHOICES = (
        ('P', 'Pendiente'),
        ('E', 'En proceso'),
        ('F', 'Finalizado'),
        ('C', 'Cancelado'),
    )
    estado = models.CharField(max_length=1, choices=ESTADO_CHOICES, default='P')

    fecha = models.DateTimeField(default=timezone.now)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Pedido {self.id} - {self.cliente}"


class PedidoZapatilla(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    zapatilla = models.ForeignKey(Zapatilla, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    talla = models.DecimalField(decimal_places=1, max_digits=3, default=1.0)

    def __str__(self):
        return f"Pedido {self.pedido.id} - {self.zapatilla.modelo} (Cantidad: {self.cantidad}, Talla: {self.talla})"


class Administrador(models.Model):
    rut = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    contrasenia = models.CharField(max_length=50, null=False)
    correo = models.EmailField(unique=True, max_length=254)

    def __str__(self):
        return f"{self.rut} -- {self.nombre} {self.apellido}"