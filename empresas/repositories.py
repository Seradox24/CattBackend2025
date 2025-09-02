from .models import Empresa


class EmpresaRepository:
    """Acceso a datos para ``Empresa``.

    Opera como un intermediario que consulta la base de datos, parecido a un
    archivista que recupera expedientes cuando se le solicita.
    """

    def all(self):
        # Devuelve todas las empresas, como listar todos los expedientes.
        return Empresa.objects.all()
