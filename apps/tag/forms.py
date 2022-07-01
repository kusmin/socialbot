from apps.tag.models import Tag, Categoria
from django import forms


class CategoriaForm(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput(attrs={'class': 'required'}), label="nome")

    class Meta:
        model = Categoria
        fields = ['nome']


class TagForm(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput(attrs={'class': 'required'}), label="nome")

    class Meta:
        model = Tag
        fields = ['nome']
