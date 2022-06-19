from datetime import datetime

from django import forms

from instagram.models import Pagina


class PaginaForm(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput(attrs={'class': 'required'}), label="nome")
    username = forms.CharField(widget=forms.TextInput(), label='username')
    password = forms.CharField(widget=forms.TextInput(), label='password')

    class Meta:
        model = Pagina
        fields = ['nome', 'username', 'password']

    def dados(self):
        return {'form': self.cleaned_data, 'data': datetime.now()}
