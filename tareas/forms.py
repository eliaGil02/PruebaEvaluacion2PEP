# importamos sistema de form de django
from django import forms

# importamos modelo User que trae django por defecto
from django.contrib.auth.models import User

# importamos form base de creacion de user
from django.contrib.auth.forms import UserCreationForm


# form heredado de usercreation, con campos obligatorios
class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Correo electrónico")
    first_name = forms.CharField(required=True, label="Nombre")
    last_name = forms.CharField(required=True, label="Apellidos")

    # clase meta, indicando q modelo usamos y q campos mostramos
    class Meta:
        model = User  # modelo user
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        ]

    # sobreescribimos el metodo save()
    def save(self, commit=True):
        # creamos user
        user = super().save(commit=False)
        # asignamos los campos adicionales
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        # obligamos que no sea staff desde el registro publico
        user.is_staff = False
        # si el commit es true lo guardamos en bs, si no devolvermos el user creado
        if commit:
            user.save()

        return user
