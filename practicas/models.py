from django.db import models
from empresas.models import Empresa


class Oferta(models.Model):
    """Oferta de práctica disponible para postulaciones."""

    title = models.CharField(max_length=255)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self) -> str:  # pragma: no cover - trivial
        return self.title
