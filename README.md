# Proyecto Django: Cursos Online

Este es un proyecto de ejemplo para crear una página web con Django utilizando el patrón MVT. La aplicación permite agregar y buscar cursos online.

## Funcionalidades
1. **Agregar Cursos**: Permite ingresar cursos con nombre, descripción y fecha de publicación.
2. **Buscar Cursos**: Permite buscar cursos por nombre o descripción.

## Cómo probar
1. Clona el repositorio.
2. Instala las dependencias con `pip install -r requirements.txt`.
3. Realiza las migraciones con `python manage.py migrate`.
4. Crea un superusuario con `python manage.py createsuperuser`.
5. Ejecuta el servidor con `python manage.py runserver`.
6. Accede a `http://127.0.0.1:8000/blog/agregar-curso/` para agregar cursos y a `http://127.0.0.1:8000/blog/buscar-cursos/` para realizar búsquedas.

## Estructura
- **Modelo**: Curso, Instructor, Categoria.
- **Vistas**: Para agregar y buscar cursos.
- **Plantillas**: Herencia de plantillas HTML.
