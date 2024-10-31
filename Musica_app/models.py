from django.db import models
from django.core.exceptions import ValidationError  # para manejar errores
import re  # librería para usar expresiones regulares

# Modelo Sello Discografico:
class SelloDiscografico(models.Model):
    nombre = models.CharField(max_length=100)
    
    # Validación de longitud mínima/evitar caracteres especiales
    def clean(self):
        if len(self.nombre) < 3:
            raise ValidationError('El nombre debe tener al menos 3 caracteres.')
        if not re.match(r'^[a-zA-Z\s]+$', self.nombre):
            raise ValidationError('El nombre solo puede contener letras y espacios.')
    
    def __str__(self):
        return self.nombre

# Modelo Perfil RedesSociales:
class PerfilRedesSociales(models.Model):
    instagram = models.URLField()
    facebook = models.URLField()
    twitter = models.URLField()
    
    # Validación URL comienza con "http" o "https"/prefijo en las URLs/longitud de URL
    def clean(self):
        url_pattern = re.compile(r'^https?://')
        if not (url_pattern.match(self.instagram) and url_pattern.match(self.facebook) and url_pattern.match(self.twitter)):
            raise ValidationError('Las URLs deben comenzar con "http" o "https".')
        max_length = 200
        if len(self.instagram) > max_length or len(self.facebook) > max_length or len(self.twitter) > max_length:
            raise ValidationError(f'Las URLs no deben exceder {max_length} caracteres.')
    
    def __str__(self):
        return f"Instagram: {self.instagram}"

# Modelo Artista:
class Artista(models.Model):
    nombre = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=50)
    genero_musical = models.CharField(max_length=50)
    
    # Validación de longitud mínima nombre/números en nombre y nacionalidad/
    def clean(self):
        if len(self.nombre) < 3:
            raise ValidationError('El nombre debe tener al menos 3 caracteres.')
        if any(char.isdigit() for char in self.nombre):
            raise ValidationError('El nombre no debe contener números.')
        if any(char.isdigit() for char in self.nacionalidad):
            raise ValidationError('La nacionalidad no debe contener números.')
        
    def __str__(self):
        return self.nombre

# Modelo Album:
class Album(models.Model):
    # opciones de géneros como constantes
    ROCK = 'Rock'
    POP = 'Pop'
    JAZZ = 'Jazz'
    HIPHOP = 'Hip-Hop'
    CLASICA = 'Clásica'
    ELECTRONICA = 'Electronica'

    # conjunto de opciones usando una lista de tuplas
    GENERO_CHOICES = [
        (ROCK, 'Rock'),
        (POP, 'Pop'),
        (JAZZ, 'Jazz'),
        (HIPHOP, 'Hip-Hop'),
        (CLASICA, 'Clásica'),
        (ELECTRONICA, 'Electronica'),
    ]

    titulo = models.CharField(max_length=100)
    fecha_lanzamiento = models.DateField()
    genero = models.CharField(max_length=50, choices=GENERO_CHOICES)

    def __str__(self):
        return self.titulo


