from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import *


app_name = 'apps.libros'

urlpatterns = [
    path("agregar_categoria/", AgregarCategoria.as_view(),name='agregar_categoria'),
    path("agregar_libro/", AgregarLibro.as_view(), name='agregar_libro'),
    path("modificar_libro/<int:pk>", ModificarLibro.as_view(), name= 'modificar_libro'),
    path("eliminar_libro/<int:pk>", EliminarLibro.as_view(), name= 'eliminar_libro'),
    path("listar_libros/", ListarLibros.as_view(), name='listar_libros'),
    path("listar_por_categoria/<str:categoria>", ListarLibrosPorCategoria, name='listar_por_categoria'),
    path("libro_detalle/<int:id>", libro_detalle, name='libro_detalle'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
