# Generated by Django 4.2.1 on 2023-05-09 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Filmes', '0002_remove_filme_descricao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filme',
            name='nome_original',
        ),
    ]