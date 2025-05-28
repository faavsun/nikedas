# forms.py
from django import forms
from django.forms import modelformset_factory
from .models import Usuario, Direccion, Zapatilla, StockZapatilla, Pedido, PedidoZapatilla
from django.contrib.auth.forms import AuthenticationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class SearchForm(forms.Form):
    query = forms.CharField(label='Buscar', max_length=100)


class DireccionForm(forms.ModelForm):
    class Meta:
        model = Direccion
        fields = ['calle', 'numero', 'detalle', 'comuna', 'region']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['detalle'].required = False


class AdminLoginForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.is_superuser:
            raise forms.ValidationError(
                "Solo los administradores pueden acceder a esta página.")


class UsuarioForm(forms.ModelForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput,
                                help_text='Debe tener al menos una mayuscula, una minuscula y un numero')
    password2 = forms.CharField(
        label='Confirmar contraseña', widget=forms.PasswordInput)
    fnac = forms.DateInput(format=(
        '%d-%m-%Y'), attrs={'class': 'form-control', 'placeholder': 'Select Date', 'type': 'date'})

    class Meta:
        model = Usuario
        fields = ['rut', 'nombre', 'apellido', 'correo', 'fnac', 'telefono']
        help_texts = {
            'rut': 'Sin puntos y con guión',
            'telefono': 'Debe partir con 9. Ej: 912345678',
            'fnac': 'DD/MM/AAAA'
        }

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_staff = False
        user.is_superuser = False
        if commit:
            user.save()
        return user


class UpdateUsuarioForm(forms.ModelForm):
    fnac = forms.DateInput(format=(
        '%d-%m-%Y'), attrs={'class': 'form-control', 'placeholder': 'Select Date', 'type': 'date'})

    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'correo', 'fnac', 'telefono']
        help_texts = {
            'telefono': 'Debe partir con 9. Ej: 912345678',
            'fnac': 'DD/MM/AAAA'
        }


# forms.py

class ZapatillaForm(forms.ModelForm):
    class Meta:
        model = Zapatilla
        fields = ['marca', 'modelo', 'precio',
                  'categoria', 'descripcion', 'foto']
        widgets = {
            'categoria': forms.CheckboxSelectMultiple(),
            'descripcion': forms.Textarea(attrs={'rows': 8, 'cols': 15}),
        }

    def __init__(self, *args, **kwargs):
        super(ZapatillaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Agregar Zapatilla'))

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio <= 0:
            raise forms.ValidationError(
                "El precio debe ser un número positivo y mayor a cero.")
        return precio

    def clean_modelo(self):
        modelo = self.cleaned_data.get('modelo')
        if len(modelo) < 2:
            raise forms.ValidationError(
                "El modelo debe tener al menos 2 caracteres.")
        return modelo


class StockZapatillaForm(forms.ModelForm):
    class Meta:
        model = StockZapatilla
        fields = ['talla', 'cantidad']

    def __init__(self, *args, **kwargs):
        super(StockZapatillaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Agregar Stock'))

    def clean_talla(self):
        talla = self.cleaned_data.get('talla')
        if talla <= 0:
            raise forms.ValidationError(
                "La talla debe ser un número positivo y mayor a cero.")
        return talla

    def clean_cantidad(self):
        cantidad = self.cleaned_data.get('cantidad')
        if cantidad <= 0:
            raise forms.ValidationError(
                "La cantidad debe ser un número positivo y mayor a cero.")
        return cantidad


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['estado']
        widgets = {
            'estado': forms.Select(choices=Pedido.ESTADO_CHOICES),
        }

    def __init__(self, *args, **kwargs):
        super(PedidoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Guardar Cambios'))


class PedidoZapatillaForm(forms.ModelForm):
    class Meta:
        model = PedidoZapatilla
        fields = ['zapatilla',  'cantidad']


class PedidoEstadoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['estado']
        widgets = {
            'estado': forms.Select(choices=Pedido.ESTADO_CHOICES, attrs={'class': 'form-control'}),
        }


PedidoZapatillaFormSet = modelformset_factory(
    PedidoZapatilla, form=PedidoZapatillaForm, extra=1
)
