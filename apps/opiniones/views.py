from django.shortcuts import render
from .forms import OpinionForm

# Create your views here.
def AgregarOpinion(request):
    form = OpinionForm(request.POST or None)
    if form.is_valid():
        form.save()

    contexto ={
        'form' : form,
    }
    template_name= 'opiniones/agregar_opinion.html'
    return render(request,template_name,contexto)

