from django import forms
from django.forms import DateInput

from apps.news.models import Noticia


class NoticiaForm(forms.ModelForm):
    texto = forms.CharField(required=False, widget=forms.Textarea(
        attrs={'placeholder': 'Digite o texto da notícia ...', 'rows': '4'}))
    class Meta:
        model = Noticia
        fields = ['titulo', 'texto', 'categoria', 'assunto', 'autor', 'foto_publicacao']
        widget = {
            'data_publicacao': DateInput(attrs={'placeholder': 'Data da publicação'}),
        }