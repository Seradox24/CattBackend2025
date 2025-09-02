from django.apps import AppConfig


class UsersConfig(AppConfig):
    """Configuración de la aplicación de usuarios."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "users"

    def ready(self):  # pragma: no cover - efectos secundarios
        """Conecta señales al iniciar la app,
        como enchufar cables antes de poner en marcha una máquina.
        """

        from . import signals  # noqa: F401
