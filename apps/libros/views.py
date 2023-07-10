from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from apps.opiniones.models import Opinion
from apps.opiniones.forms import OpinionForm

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

    def form_valid(self, form):
        form.instance.colaborador = self.request.user
        return super().form_valid(form)


class ListarLibros(ListView):
    model = Libros
    template_name = 'libros/listar_libros.html'
    context_object_name = "libros"

    def get_context_data(self):
        context = super().get_context_data()
        categorias = Categorias.objects.all()
        context['categorias'] = categorias
        return context
    
    def get_queryset(self) -> QuerySet[Any]:
        query = self.request.GET.get('buscador')
        queryset = super().get_queryset()

        if query:
            queryset = queryset.filter(titulo__icontains=query)
        return queryset.order_by('titulo')


def ListarLibrosPorCategoria(request,categoria):
    categorias2 = Categorias.objects.filter(nombre = categoria)
    libros = Libros.objects.filter(categoria = categorias2[0].id).order_by('fecha_agregado')
    categorias = Categorias.objects.all()
    template_name='libros/listar_libros.html'
    contexto = {
        'libros': libros,
        'categorias': categorias
    }
    return render(request,template_name,contexto)


# class LibroDetalle(DetailView):
#     model = Libros
#     template_name = 'libros/libro.html'
#     context_object_name = 'libro'

def libro_detalle(request,id):
    libros = Libros.objects.get(id=id)
    opiniones = Opinion.objects.filter(libro=id)
    form = OpinionForm(request.POST)

    if form.is_valid():
        if request.user.is_authenticated:
            aux = form.save(commit=False)
            aux.libro = libros
            aux.usuario = request.user
            aux.save()
            form = OpinionForm()
        else:
            return redirect('apps.usuarios:iniciar_sesion')
        
    contexto ={
        'libro' : libros,
        'form' : form,
        'opiniones': opiniones,
    }
    template_name = 'libros/libro.html'
    return render(request,template_name,contexto)