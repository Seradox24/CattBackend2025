from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class RegistrationForm(UserCreationForm):
    """Formulario de registro que permite seleccionar el rol.

    Se asemeja a una ficha de inscripción donde se elige el cargo que se
    desempeñará dentro del sistema.
    """

    role = forms.ChoiceField(choices=Profile.Roles.choices)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "role")
