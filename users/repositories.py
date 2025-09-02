from .models import Profile


class ProfileRepository:
    """Data access helpers for Profile."""

    def get_by_role(self, role: str):
        return Profile.objects.filter(role=role)
