# Generated by Django 5.1.1 on 2024-11-17 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Musica_app', '0002_genero_rename_perfil_artista_perfil_redes_sociales_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artista',
            name='genero_musical',
        ),
        migrations.AddField(
            model_name='artista',
            name='genero_musical',
            field=models.ManyToManyField(to='Musica_app.genero'),
        ),
    ]
