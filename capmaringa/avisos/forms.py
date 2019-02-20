from django import forms

from avisos.models import Aviso


class AvisoForm(forms.ModelForm):

    data = forms.DateField(widget=forms.SelectDateWidget())
    horario = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))

    class Meta:
        model = Aviso
        exclude = ('autor',)