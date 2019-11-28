from django.urls import path
from .views import *

urlpatterns = [
    path('principal', principal, name='principal'),
    path('cadastrar-consumidor', cadastrar_consumidor, name='cadastrar_consumidor'),
    path('cadastrar-gru', cadastrar_gru, name='cadastrar_gru'),
    path('debitar-cpf', debitar_cpf, name='debitar_cpf'),
    path('info', info, name='info')
]