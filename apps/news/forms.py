from django import forms
from apps.news.models import Noticia

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'texto', 'data_publicacao', 'categoria', 'assunto', 'autor', 'foto_publicacao']