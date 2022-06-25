import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


class Categoria(models.Model):
    nome = models.CharField(max_length=128, unique=True)
    tags = ArrayField(ArrayField(models.CharField(max_length=255)))

    def __str__(self):
        return self.nome


class Pagina(models.Model):
    ativo = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now=True)
    nome = models.CharField(max_length=128)
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('nome' , 'user')

    def __str__(self):
        return self.nome

    def data_criacao(self):
        return self.data_criacao >= timezone.now() - datetime.timedelta(days=1)

class ProcessarBot(models.Model):
    nome = models.CharField(max_length=128, null=True, blank=True)
    pagina = models.ForeignKey(Pagina, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    status = models.CharField(max_length=128, null=True, blank=True)
