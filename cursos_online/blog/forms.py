from django import forms
from .models import Curso, Instructor, Categoria

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'descripcion', 'fecha_publicacion']

class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ['nombre', 'correo']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']