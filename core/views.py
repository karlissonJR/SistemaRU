from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Consumidor, GRU, Transacao
from .forms import ConsumidorForm, GRUForm, TransacaoForm

@login_required
def principal(request):
    return render(request, 'principal.html')

@login_required
def cadastrar_consumidor(request):
    form = ConsumidorForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('principal')

    return render(request, 'cadastrar-consumidor.html', {'form': form})

@login_required
def cadastrar_gru(request):
    form = GRUForm(request.POST or None)

    if form.is_valid():
        form.save()

        gru = GRU.objects.last()
        cpf = gru.consumidor.cpf
        filtroConsumidor = Consumidor.objects.filter(cpf=cpf)
        consumidor = Consumidor.objects.get(cpf=cpf)
        credito = gru.valor + consumidor.credito
        filtroConsumidor.update(credito=credito)

        return redirect('principal')

    return render(request, 'cadastrar-gru.html', {'form': form})

@login_required
def realizar_venda(request):
    form = TransacaoForm(request.POST or None)

    if form.is_valid():
        form.save()

        transacao = Transacao.objects.last()
        cpf = transacao.consumidor.cpf
        filtroConsumidor = Consumidor.objects.filter(cpf=cpf)
        consumidor = Consumidor.objects.get(cpf=cpf)
        credito = consumidor.credito - transacao.valor
        filtroConsumidor.update(credito=credito)

        return redirect('principal')

    return render(request, 'realizar-venda.html', {'form': form})

@login_required
def realizar_venda2(request):
    form = TransacaoForm(request.POST or None)

    if form.is_valid():
        form.save()

        transacao = Transacao.objects.last()
        cpf = transacao.consumidor.cpf
        filtroConsumidor = Consumidor.objects.filter(cpf=cpf)
        consumidor = Consumidor.objects.get(cpf=cpf)
        credito = consumidor.credito - transacao.valor
        filtroConsumidor.update(credito=credito)

        return redirect('principal')

    return render(request, 'realizar-venda2.html', {'form': form})

@login_required
def info(request):
    consumidores = Consumidor.objects.all()
    return render(request, 'info.html', {'consumidores': consumidores})
