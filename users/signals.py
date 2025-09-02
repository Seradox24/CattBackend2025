from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile

User = get_user_model()  # Obtiene el modelo de usuario configurado.


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """Crea un perfil automáticamente al registrar un usuario.

    Es como imprimir un carnet estudiantil justo después de matricularse.
    """

    if created:
        Profile.objects.create(user=instance)  # Asigna el carnet recién impreso.
