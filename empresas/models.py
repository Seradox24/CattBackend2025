from django.db import models


class Empresa(models.Model):
    """Datos básicos de la empresa."""

    name = models.CharField(max_length=255)

    def __str__(self) -> str:  # pragma: no cover - trivial
        return self.name
