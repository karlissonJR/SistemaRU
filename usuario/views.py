from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.conf import settings
from usuario.forms import Cadastro_Form

def login(request):
    return render(request, 'index.html')

def cadastro(request):
    form = Cadastro_Form(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(settings.LOGIN_URL)

    return render(request, 'cadastro.html', {'form': form})

@login_required
def logout(request):
    auth_logout(request)
    return redirect(settings.LOGOUT_URL)