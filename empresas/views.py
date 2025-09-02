from django.views.generic import ListView
from .models import Empresa


class EmpresaListView(ListView):
    model = Empresa
    context_object_name = "empresas"
