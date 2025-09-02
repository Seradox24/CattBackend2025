from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Perfil extendido con roles.

    Actúa como una tarjeta de presentación digital que indica qué sombrero usa
    cada usuario dentro del sistema.
    """

    class Roles(models.TextChoices):
        # Cada opción es como una etiqueta pegada en la mochila del usuario.
        STUDENT = "student", "Alumno"
        TEACHER = "teacher", "Docente"
        COMPANY = "company", "Empresa"
        ADMIN = "admin", "Admin"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(
        max_length=20,
        choices=Roles.choices,
        default=Roles.STUDENT,
    )  # Guarda el rol elegido, similar a ajustar un selector en una consola.

    def __str__(self) -> str:  # pragma: no cover - representación simple
        return f"{self.user.username} ({self.get_role_display()})"
