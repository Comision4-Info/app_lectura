from django.contrib import admin
from django.urls import path, include
from .views import inicio


urlpatterns = [
    path("admin/", admin.site.urls),
    path("inicio/", inicio , name='inicio'),
    path("usuarios/", include('apps.usuarios.urls')),
]
