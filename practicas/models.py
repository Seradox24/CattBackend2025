from django.db import models
from empresas.models import Empresa


class Oferta(models.Model):
    """Oferta de práctica disponible para postulaciones.

    Se comporta como un anuncio en una vitrina al que los estudiantes pueden
    apuntarse.
    """

    title = models.CharField(
        max_length=255
    )  # Título descriptivo, como el encabezado de un aviso.
    empresa = models.ForeignKey(
        Empresa,
        on_delete=models.CASCADE,
    )  # Empresa que publica la oferta, el emisor del anuncio.

    def __str__(self) -> str:  # pragma: no cover - representación simple
        return self.title
