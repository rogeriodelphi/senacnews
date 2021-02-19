from django.shortcuts import render
from apps.news.models import Noticia

def index(request):
    template_name = 'index.html'
    publicacoes = Noticia.objects.all()
    pacote_de_dados = {
        'publicacoes': publicacoes
    }
    return render(request, template_name, pacote_de_dados)