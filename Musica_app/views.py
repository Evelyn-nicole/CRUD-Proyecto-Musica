from django.shortcuts import render, get_object_or_404, redirect
from .models import Artista, Album, PerfilRedesSociales, SelloDiscografico
from .forms import ArtistaForm, AlbumForm, PerfilRedesSocialesForm, SelloDiscograficoForm

# CRUD ARTISTAS
# Vista para listar artistas
def artista_index(request):
    artistas = Artista.objects.all()
    return render(request, 'musica_app/artista_index.html', {'artistas': artistas})

# Vista para crear un nuevo artista
def artista_create(request):
    if request.method == 'POST':
        form = ArtistaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('artista_index')
    else:
        form = ArtistaForm()
    return render(request, 'musica_app/artista_create.html', {'form': form})

# Vista para ver los detalles de un artista
def artista_detail(request, pk):
    artista = get_object_or_404(Artista, pk=pk)
    return render(request, 'musica_app/artista_detail.html', {'artista': artista})

# Vista para actualizar un artista existente
def artista_update(request, pk):
    artista = get_object_or_404(Artista, pk=pk)
    if request.method == 'POST':
        form = ArtistaForm(request.POST, instance=artista)
        if form.is_valid():
            form.save()
            return redirect('artista_index')
    else:
        form = ArtistaForm(instance=artista)
    return render(request, 'musica_app/artista_update.html', {'form': form})

# Vista para eliminar un artista
def artista_delete(request, pk):
    artista = get_object_or_404(Artista, pk=pk)
    if request.method == 'POST':
        artista.delete()
        return redirect('artista_index')
    return render(request, 'musica_app/artista_delete.html', {'artista': artista})


# CRUD ALBUMES
# Vista para listar álbumes
def album_index(request):
    albumes = Album.objects.all()
    return render(request, 'musica_app/album_index.html', {'albumes': albumes})

# Vista para crear un nuevo álbum
def album_create(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('album_index')
    else:
        form = AlbumForm()
    return render(request, 'musica_app/album_create.html', {'form': form})

# Vista para ver los detalles de un álbum
def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'musica_app/album_detail.html', {'album': album})

# Vista para actualizar un álbum existente
def album_update(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('album_index')
    else:
        form = AlbumForm(instance=album)
    return render(request, 'musica_app/album_update.html', {'form': form})

# Vista para eliminar un álbum
def album_delete(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        album.delete()
        return redirect('album_index')
    return render(request, 'musica_app/album_delete.html', {'album': album})


# CRUD PERFILES RRSS
# Vista para listar perfiles
def perfil_index(request):
    perfiles = PerfilRedesSociales.objects.all()
    return render(request, 'musica_app/perfil_index.html', {'perfiles': perfiles})

# Vista para crear un nuevo perfil
def perfil_create(request):
    if request.method == 'POST':
        form = PerfilRedesSocialesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('perfil_index')
    else:
        form = PerfilRedesSocialesForm()
    return render(request, 'musica_app/perfil_create.html', {'form': form})

# Vista para ver los detalles de un perfil
def perfil_detail(request, pk):
    perfil = get_object_or_404(PerfilRedesSociales, pk=pk)
    return render(request, 'musica_app/perfil_detail.html', {'perfil': perfil})

# Vista para actualizar un perfil existente
def perfil_update(request, pk):
    perfil = get_object_or_404(PerfilRedesSociales, pk=pk)
    if request.method == 'POST':
        form = PerfilRedesSocialesForm(request.POST, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('perfil_index')
    else:
        form = PerfilRedesSocialesForm(instance=perfil)
    return render(request, 'musica_app/perfil_update.html', {'form': form})

# Vista para eliminar un perfil
def perfil_delete(request, pk):
    perfil = get_object_or_404(PerfilRedesSociales, pk=pk)
    if request.method == 'POST':
        perfil.delete()
        return redirect('perfil_index')
    return render(request, 'musica_app/perfil_delete.html', {'perfil': perfil})


# CRUD SELLOS
# Vista para listar sellos
def sello_index(request):
    sellos = SelloDiscografico.objects.all()
    return render(request, 'musica_app/sello_index.html', {'sellos': sellos})

# Vista para crear un nuevo sello
def sello_create(request):
    if request.method == 'POST':
        form = SelloDiscograficoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sello_index')
    else:
        form = SelloDiscograficoForm()
    return render(request, 'musica_app/sello_create.html', {'form': form})

# Vista para ver los detalles de un sello
def sello_detail(request, pk):
    sello = get_object_or_404(SelloDiscografico, pk=pk)
    return render(request, 'musica_app/sello_detail.html', {'sello': sello})

# Vista para actualizar un sello existente
def sello_update(request, pk):
    sello = get_object_or_404(SelloDiscografico, pk=pk)
    if request.method == 'POST':
        form = SelloDiscograficoForm(request.POST, instance=sello)
        if form.is_valid():
            form.save()
            return redirect('sello_index')
    else:
        form = SelloDiscograficoForm(instance=sello)
    return render(request, 'musica_app/sello_update.html', {'form': form})

# Vista para eliminar un sello
def sello_delete(request, pk):
    sello = get_object_or_404(SelloDiscografico, pk=pk)
    if request.method == 'POST':
        sello.delete()
        return redirect('sello_index')
    return render(request, 'musica_app/sello_delete.html', {'sello': sello})
