from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied


class RoleRequiredMixin(LoginRequiredMixin):
    """Mixin que valida que el usuario tenga un rol específico.

    Funciona como un guardia de seguridad que revisa si el visitante lleva la
    acreditación correcta antes de abrirle la puerta.
    """

    required_role: str | None = None

    def dispatch(self, request, *args, **kwargs):
        # Busca el perfil del usuario; es como sacar la credencial de la billetera.
        role = getattr(request.user, "profile", None)
        if self.required_role and (not role or role.role != self.required_role):
            # Si la credencial no coincide, se levanta una barrera de acceso.
            raise PermissionDenied("El usuario no posee el rol requerido.")
        return super().dispatch(request, *args, **kwargs)
