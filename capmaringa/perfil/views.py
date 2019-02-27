from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from perfil.forms import *

# Create your views here.
def cadastro(request):

    cadastrado = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        perfil_form = PerfilForm(data=request.POST)

        if user_form.is_valid() and perfil_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()

            perfil = perfil_form.save(commit=False)
            perfil.user = user
            perfil.save()

            cadastrado = True

            logout(request)
            return render(request, 'mensagem.html', context={
                'mensagem': 'Aguarde a autorização de um administrador para poder logar',
            })

        else:
            print(user_form.errors, perfil_form.errors)

    else:
        user_form = UserForm()
        perfil_form = PerfilForm()

        return render(request, 'perfil/cadastro.html', context={
            'user_form': user_form,
            'perfil_form': perfil_form,
            'cadastrado': cadastrado,
        })


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.perfil.conta_autorizada:
                login(request, user)
                return HttpResponseRedirect(reverse('blog:lista_posts'))

            else:
                return render(request, 'mensagem.html', context={
                'mensagem': 'Conta não autorizada',
            })

        else:
            return render(request, 'mensagem.html', context={
                'mensagem': 'Login invalido',
            })

    else:
        return render(request, 'perfil/login.html', context={})


@login_required
def logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('blog:lista_posts'))