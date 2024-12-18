# Generated by Django 5.1.1 on 2024-11-16 23:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Musica_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.RenameField(
            model_name='artista',
            old_name='perfil',
            new_name='perfil_redes_sociales',
        ),
        migrations.RenameField(
            model_name='artista',
            old_name='sello',
            new_name='sello_discografico',
        ),
        migrations.RemoveField(
            model_name='album',
            name='genero',
        ),
        migrations.AddField(
            model_name='artista',
            name='albumes',
            field=models.ManyToManyField(to='Musica_app.album'),
        ),
        migrations.AlterField(
            model_name='artista',
            name='nacionalidad',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='artista',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='perfilredessociales',
            name='facebook',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='perfilredessociales',
            name='instagram',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='perfilredessociales',
            name='twitter',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='album',
            name='generos',
            field=models.ManyToManyField(to='Musica_app.genero'),
        ),
        migrations.AlterField(
            model_name='artista',
            name='genero_musical',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Musica_app.genero'),
        ),
    ]
