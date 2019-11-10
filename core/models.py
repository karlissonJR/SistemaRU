from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Usuario(models.Model):
    class Meta :
        abstract = True
    cpf = models.CharField(primary_key=True, max_length=11)
    nome = models.CharField(max_length=50)
    senha = models.CharField(max_length=100)

class Funcionario(Usuario):
    funcao = models.CharField(max_length=50)

class Consumidor(Usuario):
    credito = models.DecimalField(decimal_places=2, max_digits=10)
    bolsista = models.BooleanField(default=False)

