from django.contrib.auth import get_user_model
from .models import Profile


def register_user(username: str, password: str, role: str) -> Profile:
    """Crea un usuario y su perfil asociado.

    Es parecido a registrar a alguien en la recepción y entregarle un carnet con
    el rol que desempeñará.
    """

    User = get_user_model()  # Obtiene la clase de usuario configurada.
    user = User.objects.create_user(username=username, password=password)
    return Profile.objects.create(user=user, role=role)
