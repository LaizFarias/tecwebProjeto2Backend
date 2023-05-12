from django.db import models

# Create your models here.


class Filme (models.Model):

    nome = models.CharField(max_length=100)
    backdrop_path = models.CharField(max_length=255)
    def __str__(self):
        return self.nome
     
