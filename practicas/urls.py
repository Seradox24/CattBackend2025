from django.urls import path
from .views import OfertaListView

urlpatterns = [
    # Listado de ofertas de prácticas, una vitrina de oportunidades.
    path("", OfertaListView.as_view(), name="oferta-list"),
]
