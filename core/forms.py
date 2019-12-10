from django import forms
from .models import Consumidor, GRU

class ConsumidorForm(forms.ModelForm):
    class Meta:
        model = Consumidor
        fields = ['nome', 'modalidade', 'cpf']

class AtualizarConsumidorForm(forms.ModelForm):
    class Meta:
        model = Consumidor
        fields = []

class GRUForm(forms.ModelForm):
    class Meta:
        model = GRU
        fields = ['consumidor', 'valor']