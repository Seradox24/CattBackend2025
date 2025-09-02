"""
Configuración de URLs para el proyecto.

El listado `urlpatterns` funciona como un mapa de carreteras que indica qué
vista atiende cada dirección. Para más detalles visita:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Ejemplos:
Vistas basadas en funciones
    1. Importar:  from my_app import views
    2. Agregar la ruta a `urlpatterns`:  path('', views.home, name='home')
Vistas basadas en clases
    1. Importar:  from other_app.views import Home
    2. Agregar la ruta a `urlpatterns`:  path('', Home.as_view(), name='home')
Incluir otra configuración de URLs
    1. Importar la función include(): from django.urls import include, path
    2. Agregar la ruta a `urlpatterns`:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
    path("empresas/", include("empresas.urls")),
    path("practicas/", include("practicas.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
