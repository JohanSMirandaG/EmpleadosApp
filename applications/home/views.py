from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from .models import Prueba
from .forms import PruebaForm
# Create your views here.

class IndexView(TemplateView):
    template_name = 'home/home.html'
    # Aqui puede tener funciones de bases de datos

class PruebaListView(ListView):
    template_name = 'home/lista.html'
    queryset = ['A', 'B', 'C']
    context_object_name = 'lista_prueba'

class ResumenFoundationView(TemplateView):
    template_name = "home/resumen_foundation.html"

class ModeloPruebaListView(ListView):
    model = Prueba
    template_name = "home/pruebas.html"
    context_object_name = 'lista_prueba'


class PruebaCreateView(CreateView):
    template_name = "home/add.html"
    form_class = PruebaForm
    success_url = '/'