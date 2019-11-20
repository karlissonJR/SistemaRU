from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Usuario(models.Model):
    class Meta:
        abstract = True
    cpf = models.CharField(primary_key=True, max_length=11)
    nome = models.CharField(max_length=50)
    senha = models.CharField(max_length=100)

class Funcionario(Usuario):
    funcao = models.CharField(max_length=50)

class Consumidor(Usuario):
    credito = models.DecimalField(decimal_places=2, max_digits=10)
    bolsista = models.BooleanField(default=False)

class GRU(models.Model):
    codigo_barras = models.CharField(primary_key=True, max_length=25)
    valor = models.DecimalField(decimal_places=2, max_digits=10)
    nome_computador = models.CharField(max_length=50)
    competencia = models.CharField(max_length=50)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)

class Transacao(models.Model):
    tipo = models.CharField(max_length=15)
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(decimal_places=2, max_digits=10)
    data_hora = models.DateTimeField('data da transação')
