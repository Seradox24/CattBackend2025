from .models import Empresa


class EmpresaRepository:
    """Acceso a datos para Empresa."""

    def all(self):
        return Empresa.objects.all()
