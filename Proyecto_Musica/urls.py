from django.contrib import admin
from django.urls import path, include
from Musica_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.artista_index, name='home'),  # Redirige la raíz a la lista de artistas
    path('Musica/', include('Musica_app.urls')),  # Incluye las URLs de musica_app
]

