from django import forms
from .models import Oferta


class OfertaForm(forms.ModelForm):
    """Formulario para crear o editar una oferta de práctica.

    Equivale a completar un afiche antes de pegarlo en el tablón.
    """

    class Meta:
        model = Oferta
        fields = ["title", "empresa"]
