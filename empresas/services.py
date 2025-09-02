from .models import Empresa


def create_empresa(name: str) -> Empresa:
    """Caso de uso para registrar una empresa."""
    return Empresa.objects.create(name=name)
