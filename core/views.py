from django.shortcuts import render, redirect
from .models import Consumidor
from .forms import ConsumidorForm

def principal(request):
    return render(request, 'principal.html')

def cadastrar_consumidor(request):
    form = ConsumidorForm(request.POST or None)

    print(form)
    if form.is_valid():
        form.save()
        return redirect('principal')

    return render(request, 'cadastrar-consumidor.html', {'form': form})

def info(request):
    consumidores = Consumidor.objects.all()
    return render(request, 'info.html', {'consumidores': consumidores})
