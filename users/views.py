from django.views.generic import ListView
from .models import Profile


class ProfileListView(ListView):
    """Listado de perfiles de usuario.

    Sirve como revisar fichas de participantes en un archivo ordenado.
    """

    model = Profile
    context_object_name = "profiles"
