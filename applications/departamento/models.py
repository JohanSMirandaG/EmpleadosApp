from django.db import models

# Create your models here.
class Departamento(models.Model):
    name = models.CharField('name', max_length=50, unique=True)
    shor_name = models.CharField('shor_name', max_length=20, blank=True)
    active = models.BooleanField('active', default=True)
    
    class Meta:
        verbose_name = 'Mi Departamento'
        verbose_name_plural = 'Areas de la empresa'
        ordering = ['name']
        unique_together = ('name', 'shor_name')

    def __str__(self):
        return self.name
    