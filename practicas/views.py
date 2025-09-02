from django.views.generic import ListView
from .models import Oferta


class OfertaListView(ListView):
    """Muestra el listado de ofertas disponibles.

    Es como presentar todos los anuncios de prácticas en una cartelera digital.
    """

    model = Oferta
    context_object_name = "ofertas"
