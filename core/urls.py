from django.urls import path
from .views import *

urlpatterns = [
    path('principal', principal, name='principal'),
    path('cadastrar-consumidor', cadastrar_consumidor, name='cadastrar_consumidor'),
    path('cadastrar-gru', cadastrar_gru, name='cadastrar_gru'),
    path('realizar-venda', realizar_venda, name='realizar_venda'),
    path('realizar-venda2', realizar_venda2, name='realizar_venda2'),
    path('info', info, name='info')
]