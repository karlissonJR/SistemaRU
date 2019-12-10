from django.urls import path
from .views import *

urlpatterns = [
    path('principal', principal, name='principal'),
    path('cadastrar-consumidor', cadastrar_consumidor, name='cadastrar_consumidor'),
    path('atualizar-consumidor/<cpf>/<credito>', atualizar_consumidor, name='atualizar_consumidor'),
    path('cadastrar-gru', cadastrar_gru, name='cadastrar_gru'),
    path('realizar-venda', realizar_venda, name='realizar_venda'),
    path('info', info, name='info')
]