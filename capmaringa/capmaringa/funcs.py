from django.shortcuts import render


# Escreve um texto em um h2 dentro de um jumbotron
def mensagem_generica(request, mensagem):
    return render(request, 'mensagem.html', context={
        'mensagem': mensagem,
    })