from typing import Any, Dict
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    TemplateView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
#models
from .models import Empleado, Departamento
#Forms
from .forms import EmpleadoForm

class InicioView(TemplateView):
    """ Pagina de inicio """
    template_name = 'inicio.html'

# 1- Listar todos los empleados de la empresa
class ListAllEmpleados(ListView):
    template_name = 'empleados/list_all.html'
    paginate_by = 3
    
    def get_queryset(self):
        kword = self.request.GET.get("kword" ,)
        if not kword :
            kword = ""
        lista = Empleado.objects.filter(
            Q(first_name__icontains=kword) |  # Busca en el campo first_name
            Q(last_name__icontains=kword) |   # Busca en el campo last_name
            Q(full_name__icontains=kword)
        ).order_by('id')
        return lista

# 2- Listar todos los empleados que pertenecen a un Area 
class ListByAreaEmpleado(ListView):
    """ lista empleados de un area """
    template_name = 'empleados/list_by_area.html'
    context_object_name='empleados'
    paginate_by = 3
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Obtén el ID del área del self.kwargs
        area_id = self.kwargs['id']
        # Obten el objeto de Área relacionado o devuelva 404 si no existe
        departamento = get_object_or_404(Departamento, id=area_id)
        # Agrega el nombre del área al contexto
        context['departamento'] = departamento.name  # Supongo que el campo se llama 'nombre', cambia si es diferente
        return context
    
    def get_queryset(self):
        id = self.kwargs['id']
        lista = Empleado.objects.filter(
            department__id = id
        )
        return lista

# 3- Listar todos los empleados que pertenecen a un Trabajo 
class ListByJobEmpleado(ListView):
    """ lista empleados de cargo """

    template_name = 'empleados/list_by_job.html'
    def get_queryset(self):
        job_id = self.kwargs['id']
        lista = Empleado.objects.filter(
            job = job_id
        )
        return lista
   
# 4- Listar por palabra clave
class ListEmpleadosByKword(ListView):
    """ list empleado por palabra clave """
    template_name = 'empleados/by_kword.html'
    context_object_name = 'empleados'
    def get_queryset(self):
        kword = self.request.GET.get("kword" ,)
        lista = Empleado.objects.filter(
            first_name = kword
        )
        return lista

# 5- Listar habilidades de un empleado
class SelectEmpleadoView(TemplateView):
    template_name = 'empleados/select_empleado.html'
    context_object_name = 'empleados'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['empleados'] = Empleado.objects.all()
        return context

class ListAbilitiesEmpleadoView(ListView):
    template_name = 'empleados/abilities.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        empleado_id = self.request.GET.get('empleado')
        empleado = Empleado.objects.get(id=empleado_id)
        return empleado.abilities.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        empleado_id = self.request.GET.get('empleado')
        empleado = Empleado.objects.get(id=empleado_id)
        context['empleado'] = empleado
        return context

# 
class empleadoDetailView(DetailView):
    model = Empleado
    template_name = "empleados/detail_empleado.html"
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes.'
        return context
    

class SuccessView(TemplateView):
    template_name = "empleados/success.html"

class EmpleadoCreateView(CreateView):
    template_name = "empleados/add.html"
    model = Empleado
    form_class = EmpleadoForm
    success_url = reverse_lazy('empleados_app:empleados_admin')
    def form_valid(self, form):
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + " " + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)

class EmpleadoUpdateView(UpdateView):
    template_name = "empleados/update.html"
    model = Empleado
    form_class = EmpleadoForm
    success_url = reverse_lazy('empleados_app:empleados_admin')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print("****************POST********************")
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        print("****************FORM********************")
        return super(EmpleadoUpdateView, self).form_valid(form)
    

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "empleados/delete.html"
    success_url = reverse_lazy('empleados_app:empleados_admin')

# 1- Listar todos los empleados de la empresa
class ListEmpleadosAdmin(ListView):
    template_name = 'empleados/list_empleados.html'
    paginate_by = 10
    orderin = 'first_name'
    context_object_name = 'empleados'
    model = Empleado