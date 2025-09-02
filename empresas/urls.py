from django.urls import path
from .views import EmpresaListView

urlpatterns = [
    # Muestra todas las empresas; similar a una guía telefónica.
    path("", EmpresaListView.as_view(), name="empresa-list"),
]
