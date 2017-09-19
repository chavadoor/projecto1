from django.shortcuts import render
from rutinas.models import Instructor, Rutina, Sexo
from django.views.generic import ListView, DetailView
from django.template import loader
from django.http import HttpResponse


# Create your views here.


class InstructorListView(ListView):
    model = Instructor

class InstructorDetailView(DetailView):
    model = Instructor

class RutinaListView(ListView):
    model = Rutina

# Filtro de rutinas deacuerdo a la seleccion de instructor
    def get_queryset(self):
     return Rutina.objects.filter(instructor=self.kwargs['pk'])

class SexoListView(ListView):
    model = Sexo

