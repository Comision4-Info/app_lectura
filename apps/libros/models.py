from django.db import models
from django.utils import timezone
from apps.usuarios.models import Usuarios


# Create your models here.
class Categorias(models.Model):
    nombre = models.CharField(max_length=20, null=False)

    def __str__(self) -> str:
        return self.nombre


class Libros(models.Model):
    titulo = models.CharField(max_length=50, null=False)
    autor = models.CharField(max_length=20, null=False)
    descripcion = models.TextField()
    fecha_agregado = models.DateTimeField(auto_now_add=True)
    colaborador = models.ForeignKey(
        Usuarios, on_delete=models.SET_NULL, null=True, default=1)
    published = models.DateTimeField(default=timezone.now)
    imagen = models.ImageField(
        null=True, blank=True, upload_to='libros', default='libros/libro_default.png')
    categoria = models.ForeignKey(
        Categorias, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ('-published',)
