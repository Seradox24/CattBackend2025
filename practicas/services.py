from .models import Oferta
from empresas.models import Empresa


def publish_oferta(title: str, empresa: Empresa) -> Oferta:
    """Publicar una nueva oferta de práctica.

    Es como colgar un cartel en el tablón de anuncios de la empresa para que
    los estudiantes se enteren.
    """

    return Oferta.objects.create(
        title=title,
        empresa=empresa,
    )  # Guardamos la oferta como fijar el cartel en el tablón.
