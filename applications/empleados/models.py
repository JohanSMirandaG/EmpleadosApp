from django.db import models
#
from ckeditor.fields import RichTextField
from applications.departamento.models import Departamento
# Create your models here.

class Habilidades(models.Model):
    ability = models.CharField('ability', max_length=60, default='DEFAULT VALUE')

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades Empleados'

    def __str__(self):
        return self.ability
    

class Empleado(models.Model):
    """Modelo para tabla empleado"""
    JOB_CHOICES = (
        ('0', 'CONTADOR'),
        ('1', 'ADMINISTRADOR'),
        ('2', 'ECONOMISTA'),
        ('3', 'DESARROLLADOR WEB DJANGO'),        
        ('4', 'OTRO'),
    )
    first_name = models.CharField('Nombre', max_length=60)
    last_name = models.CharField('Apellido', max_length=60)
    full_name = models.CharField(
        'Nombre completo',
        max_length=120,
        blank=True
    )
    job = models.CharField('Cargo', max_length=1, choices=JOB_CHOICES)
    department = models.ForeignKey(Departamento, on_delete=models.CASCADE,verbose_name="Departamento")
    image = models.ImageField(upload_to='empleado', blank=True, null=True,verbose_name="Avatar")
    abilities = models.ManyToManyField(Habilidades, blank=True, null=True, verbose_name="Habilidades")
    cv = RichTextField('Hoja de vida', blank=True, null=True)

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['last_name']
        unique_together = ('first_name', 'last_name')

    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name
    