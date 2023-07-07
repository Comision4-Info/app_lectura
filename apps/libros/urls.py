from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import *


app_name = 'apps.libros'

urlpatterns = [
    path("agregar_categoria/", AgregarCategoria.as_view(),name='agregar_categoria'),
    path("agregar_libro/", AgregarLibro.as_view(), name='agregar_libro'),
    path("listar_libros/", ListarLibros.as_view(), name='listar_libros'),
    path("libro_detalle/<int:pk>", LibroDetalle.as_view(), name='libro_detalle'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
