from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Consumidor
from .forms import ConsumidorForm, GRUForm, AtualizarConsumidorForm

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
        print("XXX = ",form)
        form.save()
        return redirect('principal')

    return render(request, 'cadastrar-gru.html', {'form': form})

@login_required
def atualizar_consumidor(request, cpf, credito):
    consumidor = Consumidor.objects.get(cpf=cpf)
    form = AtualizarConsumidorForm(request.POST or None, instance=consumidor)

    if (form.is_valid()):
        form.save()
        return redirect("principal")

    return render(request, "atualizar-consumidor.html", {'consumidor':consumidor, 'form':form})

@login_required
def realizar_venda(request):
    return render(request, 'realizar-venda.html')

@login_required
def info(request):
    consumidores = Consumidor.objects.all()
    return render(request, 'info.html', {'consumidores': consumidores})
