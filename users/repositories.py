from .models import Profile


class ProfileRepository:
    """Auxiliares de acceso a datos para ``Profile``.

    Funciona como un bibliotecario que sabe en qué estante buscar perfiles
    según el rol que se necesite.
    """

    def get_by_role(self, role: str):
        # Filtra por rol, como separar libros por género.
        return Profile.objects.filter(role=role)
