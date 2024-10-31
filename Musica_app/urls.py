from django.urls import path
from . import views

urlpatterns = [
    # URLs para Artista
    path('artistas/', views.artista_index, name='artista_index'),
    path('artistas/nuevo/', views.artista_create, name='artista_create'),
    path('artistas/<int:pk>/', views.artista_detail, name='artista_detail'),
    path('artistas/<int:pk>/editar/', views.artista_update, name='artista_update'),
    path('artistas/<int:pk>/eliminar/', views.artista_delete, name='artista_delete'),

    # URLs para Álbum
    path('albumes/', views.album_index, name='album_index'),
    path('albumes/nuevo/', views.album_create, name='album_create'),
    path('albumes/<int:pk>/', views.album_detail, name='album_detail'),
    path('albumes/<int:pk>/editar/', views.album_update, name='album_update'),
    path('albumes/<int:pk>/eliminar/', views.album_delete, name='album_delete'),

    # URLs para Perfil de Redes Sociales
    path('perfiles/', views.perfil_index, name='perfil_index'),
    path('perfiles/nuevo/', views.perfil_create, name='perfil_create'),
    path('perfiles/<int:pk>/', views.perfil_detail, name='perfil_detail'),
    path('perfiles/<int:pk>/editar/', views.perfil_update, name='perfil_update'),
    path('perfiles/<int:pk>/eliminar/', views.perfil_delete, name='perfil_delete'),

    # URLs para Sello Discográfico
    path('sellos/', views.sello_index, name='sello_index'),
    path('sellos/nuevo/', views.sello_create, name='sello_create'),
    path('sellos/<int:pk>/', views.sello_detail, name='sello_detail'),
    path('sellos/<int:pk>/editar/', views.sello_update, name='sello_update'),
    path('sellos/<int:pk>/eliminar/', views.sello_delete, name='sello_delete'),
]
