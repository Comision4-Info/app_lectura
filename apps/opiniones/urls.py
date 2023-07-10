from django.urls import path
from .views import *

app_name = 'apps.opinion'

urlpatterns = [
    path('agregar_opinion/', AgregarOpinion, name= 'agregar_opinion'),
]