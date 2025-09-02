from django.db import models


class Empresa(models.Model):
    """Datos básicos de la empresa.

    Funciona como una ficha en un directorio comercial que describe a cada
    organización con la que interactuaremos.
    """

    name = models.CharField(
        max_length=255
    )  # Nombre público, equivalente al rótulo en la fachada del edificio.

    def __str__(self) -> str:  # pragma: no cover - representación simple
        return self.name
