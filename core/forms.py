from django import forms
from .models import Consumidor, GRU, Transacao

class ConsumidorForm(forms.ModelForm):
    class Meta:
        model = Consumidor
        fields = ['nome', 'modalidade', 'cpf', 'bolsista']

class GRUForm(forms.ModelForm):
    class Meta:
        model = GRU
        fields = ['consumidor', 'valor']

class TransacaoForm(forms.ModelForm):
    class Meta:
        model = Transacao
        fields = ['consumidor', 'valor']