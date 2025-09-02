from django.views.generic import ListView
from .models import Oferta


class OfertaListView(ListView):
    model = Oferta
    context_object_name = "ofertas"
