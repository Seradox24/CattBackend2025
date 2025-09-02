from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Perfil extendido con roles."""

    class Roles(models.TextChoices):
        STUDENT = "student", "Alumno"
        TEACHER = "teacher", "Docente"
        COMPANY = "company", "Empresa"
        ADMIN = "admin", "Admin"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=Roles.choices, default=Roles.STUDENT)

    def __str__(self) -> str:  # pragma: no cover - trivial
        return f"{self.user.username} ({self.get_role_display()})"
