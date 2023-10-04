from django.contrib import admin
from .models import Empleado, Habilidades

# Register your models here.

admin.site.register(Habilidades)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'full_name',
        'department',
        'job',
        'image',
        'display_abilities',    
    )
    search_fields = ('first_name',)
    list_filter = ('department','job','abilities',)
    # solo funciona con campos muchos a muchos
    filter_horizontal = ('abilities',)


    def full_name(self, obj):
        #
        return obj.first_name + ' ' +  obj.last_name
    
    def display_abilities(self, obj):
        return ", ".join([item.ability for item in obj.abilities.all()])
    display_abilities.short_description = 'abilities'

admin.site.register(Empleado, EmpleadoAdmin)