from django.contrib import admin
from django.urls import path
from .views import RegistrarUsuario

app_name = 'apps.usuarios'

urlpatterns = [
    path("registrar/", RegistrarUsuario.as_view(),name='registrar'),
]
