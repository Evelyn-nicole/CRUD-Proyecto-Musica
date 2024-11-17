from django import forms
from .models import Artista, Album, PerfilRedesSociales, SelloDiscografico, Genero


class ArtistaForm(forms.ModelForm):
    genero_musical = forms.ModelMultipleChoiceField(
        queryset=Genero.objects.all(),
        widget=forms.CheckboxSelectMultiple(),  # Usa casillas de verificación
        required=True  # Campo obligatorio
    )
    albumes = forms.ModelMultipleChoiceField(
        queryset=Album.objects.all(),
        widget=forms.CheckboxSelectMultiple(),  # Usa casillas de verificación
        required=False  # Campo opcional
    )

    class Meta:
        model = Artista
        fields = ['nombre', 'nacionalidad', 'genero_musical', 'perfil_redes_sociales', 'sello_discografico', 'albumes']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del artista'}),
            'nacionalidad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nacionalidad'}),
            'genero_musical': forms.CheckboxSelectMultiple(),  # Correcto para ManyToMany
            'perfil_redes_sociales': forms.Select(attrs={'class': 'form-control'}),
            'sello_discografico': forms.Select(attrs={'class': 'form-control'}),
            'albumes': forms.CheckboxSelectMultiple(),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.full_clean()  # Ejecuta las validaciones del modelo
        if commit:
            instance.save()
            self.save_m2m()  # Guarda las relaciones ManyToMany
        return instance



class AlbumForm(forms.ModelForm):
    artistas = forms.ModelMultipleChoiceField(
        queryset=Artista.objects.all(),
        widget=forms.CheckboxSelectMultiple(),  # Casillas de verificación para artistas
        required=True  # Obligatorio
    )
    generos = forms.ModelMultipleChoiceField(
        queryset=Genero.objects.all(),
        widget=forms.CheckboxSelectMultiple(),  # Casillas de verificación para géneros
        required=True  # Obligatorio
    )

    class Meta:
        model = Album
        fields = ['titulo', 'fecha_lanzamiento', 'generos', 'artistas']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título del álbum'}),
            'fecha_lanzamiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        

class PerfilRedesSocialesForm(forms.ModelForm):
    class Meta:
        model = PerfilRedesSociales
        fields = ['instagram', 'facebook', 'twitter']
        widgets = {
            'instagram': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://instagram.com/...'}),
            'facebook': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://facebook.com/...'}),
            'twitter': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://twitter.com/...'}),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.full_clean()
        if commit:
            instance.save()
        return instance


class SelloDiscograficoForm(forms.ModelForm):
    class Meta:
        model = SelloDiscografico
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del sello discográfico'}),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.full_clean()
        if commit:
            instance.save()
        return instance


class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del género'}),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.full_clean()
        if commit:
            instance.save()
        return instance
