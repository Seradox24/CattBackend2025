from .models import Oferta
from empresas.models import Empresa


def publish_oferta(title: str, empresa: Empresa) -> Oferta:
    """Publicar una nueva oferta de práctica."""
    return Oferta.objects.create(title=title, empresa=empresa)
