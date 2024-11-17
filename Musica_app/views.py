from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages  # Para mensajes flash
from .models import Artista
from .forms import ArtistaForm


# Vista para listar artistas (Incluye datos relacionados: Álbumes, Perfiles, y Sellos)
def artista_index(request):
    artistas = Artista.objects.select_related(
        'perfil_redes_sociales', 'sello_discografico'
    ).prefetch_related('genero_musical', 'albumes').order_by('nombre')  # Ordena por nombre
    return render(request, 'musica_app/artista_index.html', {'artistas': artistas})


# Vista para crear un nuevo artista (Incluye relaciones con Álbumes, Perfiles, y Sellos)
def artista_create(request):
    if request.method == 'POST':
        form = ArtistaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Artista creado exitosamente.")
            return redirect('artista_index')  # Redirige a la lista de artistas
        else:
            messages.error(request, "Hubo un error al crear el artista.")
    else:
        form = ArtistaForm()
    return render(request, 'musica_app/artista_create.html', {'form': form})

# Vista para ver los detalles de un artista
def artista_detail(request, pk):
    artista = get_object_or_404(Artista, pk=pk)
    albumes = artista.albumes.all()  # Álbumes relacionados
    perfil = artista.perfil_redes_sociales  # Perfil de redes sociales
    sello = artista.sello_discografico  # Sello discográfico
    return render(request, 'musica_app/artista_detail.html', {
        'artista': artista,
        'albumes': albumes,
        'perfil': perfil,
        'sello': sello
    })


# Vista para actualizar un artista existente (Incluye relaciones)
def artista_update(request, pk):
    artista = get_object_or_404(Artista, pk=pk)
    if request.method == 'POST':
        form = ArtistaForm(request.POST, instance=artista)
        if form.is_valid():
            form.save()
            messages.success(request, 'Artista actualizado exitosamente.')  # Mensaje de éxito
            return redirect('artista_index')
        else:
            messages.error(request, "Hubo un problema al actualizar campos.")
    else:
        form = ArtistaForm(instance=artista)
    return render(request, 'musica_app/artista_update.html', {'form': form})


# Vista para eliminar un artista
def artista_delete(request, pk):
    artista = get_object_or_404(Artista, pk=pk)
    if request.method == 'POST':
        artista.delete()
        messages.success(request, 'Artista eliminado exitosamente.')  # Mensaje de éxito
        return redirect('artista_index')
    return render(request, 'musica_app/artista_delete.html', {'artista': artista})
