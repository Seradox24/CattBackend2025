"""
Configuración de Django para el proyecto.

Este archivo funciona como el panel de control de una nave: cada perilla y
interruptor define el rumbo y la altura de la aplicación.

Generado por 'django-admin startproject' usando Django 5.2.5.

Para más información sobre este archivo, consulta
https://docs.djangoproject.com/en/5.2/topics/settings/

Para ver la lista completa de configuraciones y sus valores, visita
https://docs.djangoproject.com/en/5.2/ref/settings/
"""

from pathlib import Path
import os

# Construye rutas dentro del proyecto como BASE_DIR / 'subdir',
# parecido a encajar piezas de LEGO para formar un camino.
BASE_DIR = Path(__file__).resolve().parent.parent

# Ajustes rápidos para desarrollo; no son aptos para producción,
# como andar con andamios temporales antes de levantar el edificio final.
# Consulta https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/
# para la lista de verificación previa al despliegue.

# ADVERTENCIA DE SEGURIDAD: mantén la clave secreta de producción fuera de
# la vista, al igual que la combinación de una caja fuerte.
SECRET_KEY = "django-insecure--e9v-yiddr#onfjwyl8u&00f3fjtqz=dn@yi0k4$_#9tpr9$yy"

# ADVERTENCIA DE SEGURIDAD: no ejecutes con DEBUG activado en producción;
# sería como dejar las puertas del servidor abiertas de par en par.
DEBUG = True

ALLOWED_HOSTS = []


# Definición de aplicaciones, el índice de módulos que conforman nuestro
# proyecto.

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # aplicaciones de terceros, plugins que se acoplan a nuestra maquinaria
    "tailwind",
    "django_browser_reload",
    "theme",
    # aplicaciones locales, componentes hechos a medida para el motor
    "core",
    "users",
    "empresas",
    "practicas",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "core.context_processors.site_settings",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Base de datos, la despensa donde guardamos la información.
# Más detalles en
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB", "catt_db"),
        "USER": os.environ.get("POSTGRES_USER", "postgres"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD", "postgres"),
        "HOST": os.environ.get("POSTGRES_HOST", "localhost"),
        "PORT": os.environ.get("POSTGRES_PORT", "5432"),
    }
}


# Validación de contraseñas, filtros que aseguran que las llaves sean
# robustas.
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internacionalización: permite hablar diferentes idiomas como un intérprete
# en una conferencia.
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Archivos estáticos (CSS, JavaScript, Imágenes), parecidos a carteles en una
# ciudad que permanecen igual en cada visita.
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

TAILWIND_APP_NAME = "theme"

INTERNAL_IPS = ["127.0.0.1"]

# Tipo de clave primaria por defecto.
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
