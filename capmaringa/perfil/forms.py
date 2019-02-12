from django import forms
from django.contrib.auth.models import User

from perfil.models import Perfil


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'password',
        )


class PerfilForm(forms.ModelForm):

    class Meta:
        model = Perfil
        exclude = (
            'user',
            'conta_autorizada',
            'pode_postar',
        )