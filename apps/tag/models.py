from django.contrib.postgres.fields import ArrayField
from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=128, unique=True)
    data_criacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome


class Tag(models.Model):
    nome = models.CharField(max_length=128, unique=True)
    data_criacao = models.DateTimeField(auto_now=True)
    categoria = models.ManyToManyField(Categoria)

    def __str__(self):
        return self.nome

