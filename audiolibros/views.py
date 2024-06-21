# audiolibros/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Audiolibro
from .forms import AudiolibroForm
from django.db.models import Q

# Vista para listar los audiolibros y aplicar filtros de búsqueda y tipo
def lista_audiolibros(request):
    query = request.GET.get('q')  # Obtener la consulta de búsqueda del parámetro 'q'
    tipo_filtro = request.GET.get('tipo')  # Obtener el filtro de tipo del parámetro 'tipo'
    
    audiolibros = Audiolibro.objects.all()  # Obtener todos los audiolibros
    
    # Filtrar por título o autor si hay una consulta de búsqueda
    if query:
        audiolibros = audiolibros.filter(Q(titulo__icontains=query) | Q(autor__icontains=query))
    
    # Filtrar por tipo si hay un filtro de tipo
    if tipo_filtro:
        audiolibros = audiolibros.filter(tipo=tipo_filtro)
    
    # Obtener los tipos únicos de audiolibros
    tipos = Audiolibro.objects.values_list('tipo', flat=True).distinct()
    
    # Renderizar la plantilla 'lista_audiolibros.html' con los audiolibros, la consulta de búsqueda, los tipos y el filtro de tipo
    return render(request, 'audiolibros/lista_audiolibros.html', {
        'audiolibros': audiolibros,
        'query': query or '',
        'tipos': tipos,
        'tipo_filtro': tipo_filtro
    })

# Vista para crear un nuevo audiolibro
def crear_audiolibro(request):
    if request.method == 'POST':  # Si se envía el formulario
        form = AudiolibroForm(request.POST, request.FILES)  # Crear un formulario con los datos enviados
        if form.is_valid():  # Si el formulario es válido
            form.save()  # Guardar el nuevo audiolibro
            return redirect('lista_audiolibros')  # Redirigir a la lista de audiolibros
    else:
        form = AudiolibroForm()  # Crear un formulario vacío
    return render(request, 'audiolibros/crear_audiolibro.html', {'form': form})  # Renderizar la plantilla 'crear_audiolibro.html' con el formulario

# Vista para editar un audiolibro existente
def editar_audiolibro(request, pk):
    audiolibro = get_object_or_404(Audiolibro, pk=pk)  # Obtener el audiolibro por su clave primaria o devolver un error 404 si no existe
    if request.method == 'POST':  # Si se envía el formulario
        form = AudiolibroForm(request.POST, request.FILES, instance=audiolibro)  # Crear un formulario con los datos enviados y el audiolibro existente
        if form.is_valid():  # Si el formulario es válido
            form.save()  # Guardar los cambios del audiolibro
            return redirect('lista_audiolibros')  # Redirigir a la lista de audiolibros
    else:
        form = AudiolibroForm(instance=audiolibro)  # Crear un formulario con los datos del audiolibro existente
    return render(request, 'audiolibros/editar_audiolibro.html', {'form': form, 'audiolibro': audiolibro})  # Renderizar la plantilla 'editar_audiolibro.html' con el formulario y el audiolibro

# Vista para eliminar un audiolibro
def eliminar_audiolibro(request, pk):
    audiolibro = get_object_or_404(Audiolibro, pk=pk)  # Obtener el audiolibro por su clave primaria o devolver un error 404 si no existe
    if request.method == 'POST':  # Si se envía el formulario de confirmación de eliminación
        audiolibro.delete()  # Eliminar el audiolibro
        return redirect('lista_audiolibros')  # Redirigir a la lista de audiolibros
    return render(request, 'audiolibros/eliminar_audiolibro.html', {'audiolibro': audiolibro})  # Renderizar la plantilla 'eliminar_audiolibro.html' con el audiolibro
