from django.contrib import admin
# Importar mis modelos desde .models
from .models import Artista, PerfilRedesSociales, SelloDiscografico, Album

# Registro mis modelos.
admin.site.register(Artista)
admin.site.register(PerfilRedesSociales)
admin.site.register(SelloDiscografico)
admin.site.register(Album)


