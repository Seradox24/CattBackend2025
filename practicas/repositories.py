from .models import Oferta


class OfertaRepository:
    """Consultas relacionadas con ``Oferta``.

    Funciona como un buscador que recopila avisos según los filtros pedidos.
    """

    def all(self):
        # Lista todas las ofertas, como mostrar todos los anuncios disponibles.
        return Oferta.objects.all()
