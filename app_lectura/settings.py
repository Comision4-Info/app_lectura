from pathlib import Path
from django.urls import reverse_lazy



#-----------------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
#-----------------------------------------------------------------------------------
SECRET_KEY = "django-insecure-5u#n@z7$!s8z412e_s#ja9i3g-cl_y$+f)!x=m_@7jl$jefk6h"
#-----------------------------------------------------------------------------------
AUTH_USER_MODEL = 'usuarios.Usuarios'
#-----------------------------------------------------------------------------------
LOGIN_URL          = reverse_lazy('apps.usuarios:iniciar_sesion')
LOGIN_REDIRECT_URL = reverse_lazy('inicio')
LOGOUT_REDIRECT_URL= reverse_lazy('inicio')
#-----------------------------------------------------------------------------------
DEBUG = True
#-----------------------------------------------------------------------------------
ALLOWED_HOSTS = []
#-----------------------------------------------------------------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    #Paquetes

    #Apps
    'apps.usuarios',
]
#-----------------------------------------------------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
#-----------------------------------------------------------------------------------
ROOT_URLCONF = "app_lectura.urls"
#-----------------------------------------------------------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
#-----------------------------------------------------------------------------------
WSGI_APPLICATION = "app_lectura.wsgi.application"
#-----------------------------------------------------------------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": 'app_lectura',
        "USER": 'root',
        "PASSWORD": 'root',
        "PORT": '3306'
    }
}
#-----------------------------------------------------------------------------------
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
#-----------------------------------------------------------------------------------
LANGUAGE_CODE = "es-ar"

TIME_ZONE = "America/Argentina/Buenos_Aires"

USE_I18N = True

USE_TZ = True
#-----------------------------------------------------------------------------------
STATIC_URL = "static/"
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
STATIC_ROOT      = BASE_DIR / "staticfiles"
#-----------------------------------------------------------------------------------
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
#-----------------------------------------------------------------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
#-----------------------------------------------------------------------------------