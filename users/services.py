from django.contrib.auth import get_user_model
from .models import Profile


def register_user(username: str, password: str, role: str) -> Profile:
    """Create a user and associated profile."""
    User = get_user_model()
    user = User.objects.create_user(username=username, password=password)
    return Profile.objects.create(user=user, role=role)
