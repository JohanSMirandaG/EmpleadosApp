from django.urls import path
from . import views
urlpatterns = [
    path(
        'home/', 
        views.IndexView.as_view()
    ),  
    path(
        'vista/', 
        views.PruebaListView.as_view()
    ),  
    path(
        'prueba/', 
        views.ModeloPruebaListView.as_view()
    ),  
    path(
        'add/', 
        views.PruebaCreateView.as_view(), 
        name = 'prueba_add'
    ),  
    path(
        'resumen/', 
        views.ResumenFoundationView.as_view(), 
        name = 'resumen'
    ),
]
