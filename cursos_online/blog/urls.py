from django.urls import path
from . import views

urlpatterns = [
    path('agregar-curso/', views.agregar_curso, name='agregar_curso'),
    path('buscar-cursos/', views.buscar_cursos, name='buscar_cursos'),
]