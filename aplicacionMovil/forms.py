from django.contrib.auth.models import User  # se usa para las sesiones
from django.contrib.auth.forms import UserCreationForm  # se usa para las sesiones
from django import forms

from aplicacionMovil import helper


class RegistroForm(UserCreationForm):
    roles = (
        (2, "empleado"),
        (3, "cliente"),
    )
    rol = forms.ChoiceField(choices=roles)

    nombre = forms.CharField(max_length=100)
    telefono = forms.CharField(max_length=15)
    correo = forms.EmailField(max_length=254)

    class Meta:
        # propiedades del user
        model = User
        fields = ("last_name", "password1", "password2", "username", "rol")



class ComentarioForm(forms.Form):
    texto_comentario = forms.CharField(widget=forms.Textarea)

    puntuacion = forms.IntegerField(
        label="puntuacion", required=True, help_text="puntuacion del 1 al 5"
    )

    # fecha_comentario
    fecha_comentario = forms.DateField(label="Fecha comentario")

    def __init__(self, *args, **kwargs):

        super(ComentarioForm, self).__init__(*args, **kwargs)

        appDisponibles = helper.obtener_aplicacion_movil_select()
        self.fields["aplicacion_movil"] = forms.ChoiceField(
            choices=appDisponibles,
            widget=forms.Select,
            required=True,
            help_text="Despliega y selecciona un elemento",
        )

        UsuarioDisponibles = helper.obtener_usuarios_select()
        self.fields["usuario"] = forms.ChoiceField(
            choices=UsuarioDisponibles,
            widget=forms.Select,
            required=True,
            help_text="Despliega y selecciona un elemento",
        )
        
        
class ComentarioActualizarNombreForm(forms.Form):
    texto_comentario = forms.CharField(
        label="Nombre del comentario",
        required=True,
        max_length=200,
        help_text="200 caracteres como máximo",
    )
