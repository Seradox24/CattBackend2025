from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied


class RoleRequiredMixin(LoginRequiredMixin):
    """Mixin enforcing that the user has a given role."""

    required_role: str | None = None

    def dispatch(self, request, *args, **kwargs):
        role = getattr(request.user, "profile", None)
        if self.required_role and (not role or role.role != self.required_role):
            raise PermissionDenied("User lacks required role.")
        return super().dispatch(request, *args, **kwargs)
