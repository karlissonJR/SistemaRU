from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils import timezone

class Usuario(models.Model):
    class Meta:
        abstract = True
    cpf = models.CharField(primary_key=True, max_length=11)
    nome = models.CharField(max_length=50)
    senha = models.CharField(max_length=100)

class Funcionario(Usuario):
    funcao = models.CharField(max_length=50)

class Consumidor(Usuario):
    credito = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    bolsista = models.BooleanField()
    modalidade = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

class GRU(models.Model):
    #codigo_barras = models.CharField(primary_key=True, max_length=25)
    valor = models.DecimalField(decimal_places=2, max_digits=10)
    #competencia = models.CharField(max_length=50)
    consumidor = models.ForeignKey(Consumidor, on_delete=models.CASCADE)

    def __str__(self):
        return self.consumidor.nome

class Transacao(models.Model):
    #tipo = models.CharField(max_length=15)
    #descricao = models.CharField(max_length=100)
    consumidor = models.ForeignKey(Consumidor, on_delete=models.CASCADE)
    valor = models.DecimalField(decimal_places=2, max_digits=10)
    data_hora = models.DateTimeField('data da transação', default=timezone.now)
