from .models import Empresa


def create_empresa(name: str) -> Empresa:
    """Caso de uso para registrar una empresa.

    Se asemeja a dar de alta una nueva tarjeta en el directorio comercial.
    """

    return Empresa.objects.create(
        name=name
    )  # Persistimos el nombre como archivar un expediente nuevo.
