from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.utils import translation

import datetime

from blog.forms import *

from capmaringa.funcs import mensagem_generica

# Create your views here.
@login_required
def criar_posts(request):
    if request.user.perfil.pode_postar:
        if request.method == 'POST':
            post_form = PostForm(data=request.POST)

            if post_form.is_valid():
                post = post_form.save(commit=False)
                post.autor = request.user
                post.data_publicacao = datetime.datetime.now()

                if 'imagem' in request.FILES:
                    post.imagem = request.FILES['imagem']

                post.save()

                return HttpResponseRedirect(reverse('index'))

            else:
                return mensagem_generica(request, 'Formulario invalido')

        else:
            post_form = PostForm()
            return render(request, 'blog/criar_post.html', context={
                'post_form': post_form,
                'editando': False,
            })

    else:
        return mensagem_generica(request, 'Voce nao pode postar')


def listar_posts(request):
    posts = Post.objects.all().order_by('-data_publicacao')[:25]

    return render(request, 'blog/posts.html', context={
        'posts': posts,
    })


@login_required
def post_detalhe(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if post.autor == request.user:
        return render(request, 'blog/post_detalhe.html', context={
            'post': post,
        })

    else:
        return mensagem_generica(request, 'Voce nao pode editar esse post')

@login_required
def editar_posts(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.user == post.autor:
        if request.method == 'POST':
            post_form = EditaPostForm(data=request.POST)

            if post_form.is_valid():
                update_post = post_form.save(commit=False)

                if 'imagem' in request.FILES:
                    update_post.imagem = request.FILES['imagem']
                    post.imagem = update_post.imagem

                if update_post.titulo != '':
                    post.titulo = update_post.titulo

                if update_post.descricao != '':
                    post.descricao = update_post.descricao
                
                post.save()

                return HttpResponseRedirect(reverse('index'))

            else:
                return mensagem_generica(request, 'Formulario invalido')

        else:
            post_form = EditaPostForm()
            return render(request, 'blog/criar_post.html', context={
                'post_form': post_form,
                'editando': True,
            })

    else:
        return mensagem_generica(request, 'Voce nao e o dono desse posts')
