from django.views.generic import ListView
from .models import Empresa


class EmpresaListView(ListView):
    """Listado de empresas registradas.

    Muestra todas las fichas disponibles como si hojeáramos un catálogo.
    """

    model = Empresa
    context_object_name = "empresas"
