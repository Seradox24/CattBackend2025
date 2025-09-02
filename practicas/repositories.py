from .models import Oferta


class OfertaRepository:
    """Consultas relacionadas con ofertas."""

    def all(self):
        return Oferta.objects.all()
