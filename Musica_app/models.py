from django.db import models
from django.core.exceptions import ValidationError
from datetime import date
import re

class SelloDiscografico(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Genero(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre


class Album(models.Model):
    titulo = models.CharField(max_length=100)
    fecha_lanzamiento = models.DateField()
    generos = models.ManyToManyField(Genero)  # Relación N-a-N con Genero
    artistas = models.ManyToManyField('Artista')  # Relación N-a-N con Artista

    def clean(self):
        if self.fecha_lanzamiento > date.today():
            raise ValidationError('La fecha de lanzamiento no puede estar en el futuro.')

    def __str__(self):
        return self.titulo


class PerfilRedesSociales(models.Model):
    instagram = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)

    def clean(self):
        if self.instagram and not re.match(r'^https://(www\.)?instagram\.com/.+', self.instagram):
            raise ValidationError('La URL de Instagram debe ser válida y comenzar con "https://instagram.com/".')
        if self.facebook and not re.match(r'^https://(www\.)?facebook\.com/.+', self.facebook):
            raise ValidationError('La URL de Facebook debe ser válida y comenzar con "https://facebook.com/".')
        if self.twitter and not re.match(r'^https://(www\.)?twitter\.com/.+', self.twitter):
            raise ValidationError('La URL de Twitter debe ser válida y comenzar con "https://twitter.com/".')

    def __str__(self):
        return f"Instagram: {self.instagram or 'N/A'}, Facebook: {self.facebook or 'N/A'}, Twitter: {self.twitter or 'N/A'}"


class Artista(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)
    genero_musical = models.ManyToManyField(Genero)
    sello_discografico = models.ForeignKey(SelloDiscografico, on_delete=models.CASCADE)
    albumes = models.ManyToManyField(Album)
    perfil_redes_sociales = models.OneToOneField(PerfilRedesSociales, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
