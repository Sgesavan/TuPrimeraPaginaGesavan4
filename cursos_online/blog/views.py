from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Curso, Instructor, Categoria
from .forms import CursoForm, InstructorForm, CategoriaForm
from django.db.models import Q

# Vista para ingresar un curso
def agregar_curso(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_cursos')
    else:
        form = CursoForm()
    return render(request, 'blog/agregar_curso.html', {'form': form})

# Vista para buscar cursos por nombre
def buscar_cursos(request):
    query = request.GET.get('q', '')
    resultados = Curso.objects.filter(Q(nombre__icontains=query) | Q(descripcion__icontains=query))
    return render(request, 'blog/buscar_cursos.html', {'resultados': resultados, 'query': query})