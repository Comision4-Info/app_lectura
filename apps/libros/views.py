from typing import Any, Dict
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *

# Create your views here.


class AgregarCategoria(CreateView, LoginRequiredMixin):
    model = Categorias
    fields = ['nombre']
    template_name = 'libros/agregar_categoria.html'
    success_url = reverse_lazy('inicio')


class AgregarLibro(CreateView, LoginRequiredMixin):
    model = Libros
    fields = ['titulo', 'autor', 'descripcion', 'imagen', 'categoria']
    template_name = 'libros/agregar_libro.html'
    success_url = reverse_lazy('inicio')


class ListarLibros(ListView):
    model = Libros
    template_name = 'libros/listar_libros.html'
    context_object_name = "libros"

    def get_context_data(self):
        context = super().get_context_data()
        categorias = Categorias.objects.all()
        context['categorias'] = categorias
        return context


class LibroDetalle(DetailView):
    model = Libros
    template_name = 'libros/libro.html'
    context_object_name = 'libro'
