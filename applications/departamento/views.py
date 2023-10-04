from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import FormView
from applications.empleados.models import Empleado
from .models import Departamento
from .forms import NewDepartmentForm
# Create your views here.

class DepartamentoListView(ListView):
    model = Departamento
    context_object_name = 'departamentos'
    template_name = "departamento/list.html"

class NewDepartmentView(FormView):
    template_name ="departamento/new_department.html"
    form_class = NewDepartmentForm
    success_url = reverse_lazy('empleados_app:empleados_admin')

    def form_valid(self, form):
        print('****************Estamos en el form valid************')
        department = Departamento(
            name=form.cleaned_data['department'],
            shor_name=form.cleaned_data['shorname']
        )
        department.save()
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        Empleado.objects.create(
            first_name=first_name,
            last_name=last_name,
            job='1',
            department=department
        )
        return super().form_valid(form)