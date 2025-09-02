from django.urls import path
from .views import ProfileListView

urlpatterns = [
    # Ruta que lista perfiles; funciona como un índice de personas registradas.
    path("profiles/", ProfileListView.as_view(), name="profile-list"),
]
