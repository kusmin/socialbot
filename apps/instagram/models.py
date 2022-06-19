import datetime

from django.db import models
from django.utils import timezone


class Tag(models.Model):
    nome = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return self.nome


class Pagina(models.Model):
    qtd_seguidores = models.IntegerField(default=0)
    qtd_seguindo = models.IntegerField(default=0)
    qtd_publicacoes = models.IntegerField(default=0)
    ativo = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now=True)
    nome = models.CharField(max_length=128, null=True, blank=True)
    username = models.CharField(max_length=128, null=True, blank=True)
    password = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return self.nome

    def data_criacao(self):
        return self.data_criacao >= timezone.now() - datetime.timedelta(days=1)
