from django import forms
from .models import Empresa


class EmpresaForm(forms.ModelForm):
    """Formulario para crear o editar una empresa.

    Sirve como una planilla donde se anota el nombre de la organización antes
    de guardarla en la base de datos.
    """

    class Meta:
        model = Empresa
        fields = ["name"]
