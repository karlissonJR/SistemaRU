from django.urls import path
from .views import *

urlpatterns = [
    path('', principal, name='principal'),
    path('cadastrar-consumidor', cadastrar_consumidor, name='cadastrar_consumidor'),
    path('info', info, name='info')
]