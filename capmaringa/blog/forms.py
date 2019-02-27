from django import forms

from blog.models import *


class PostForm(forms.ModelForm):
    imagem = forms.ImageField(required=False)

    class Meta:
        model = Post
        exclude = (
            'autor',
            'data_publicacao',
        )


class EditaPostForm(forms.ModelForm):
    titulo = forms.CharField(required=False)
    descricao = forms.CharField(widget=forms.Textarea, required=False)
    imagem = forms.ImageField(required=False)

    class Meta:
        model = Post
        exclude = (
            'autor',
            'data_publicacao',
        )