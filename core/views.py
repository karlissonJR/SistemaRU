from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Consumidor
from .forms import ConsumidorForm

@login_required
def principal(request):
    return render(request, 'principal.html')

@login_required
def cadastrar_consumidor(request):
    form = ConsumidorForm(request.POST or None)

    print(form)
    if form.is_valid():
        form.save()
        return redirect('principal')

    return render(request, 'cadastrar-consumidor.html', {'form': form})

@login_required
def cadastrar_gru(request):
    return render(request, 'cadastrar-gru.html')

@login_required
def debitar_cpf(request):
    return render(request, 'debitar-cpf.html')

@login_required
def info(request):
    consumidores = Consumidor.objects.all()
    return render(request, 'info.html', {'consumidores': consumidores})
