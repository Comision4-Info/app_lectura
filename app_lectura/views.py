from django.shortcuts import render


def inicio(request):
    template_name = 'inicio.html'
    return render(request,template_name)