from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

from avisos.models import Aviso
from avisos.forms import AvisoForm

from capmaringa.funcs import mensagem_generica

# Create your views here.
def listar_avisos(request):
    avisos = Aviso.objects.all().order_by('-data')[:25]

    return render(request, 'avisos/lista_avisos.html', context={
        'avisos': avisos,
    })


def detalhes(request, aviso_id):
    aviso = get_object_or_404(Aviso, pk=aviso_id)

    return render(request, 'avisos/aviso_detalhes.html', context={
        'aviso': aviso,
    })


@login_required
def criar_avisos(request):
    if request.user.perfil.pode_postar:
        if request.method == 'POST':
            aviso_form = AvisoForm(data=request.POST)

            if aviso_form.is_valid():
                aviso = aviso_form.save(commit=False)
                aviso.autor = request.user
                aviso.save()
                return HttpResponseRedirect(reverse('avisos:listar_avisos'))

            else:
                # TODO colocar acentos
                return mensagem_generica(request, 'Formulario invalido')

        else:
            aviso_form = AvisoForm()

            return render(request, 'avisos/criar_aviso.html', context={
                'aviso_form': aviso_form,
            })

    else:
        # TODO colocar acentos
        return mensagem_generica(request, 'Voce nao pode postar')
