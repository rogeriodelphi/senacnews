from django.shortcuts import render
from apps.news.models import Noticia

def site(request):
    template_name = 'site.html'
    publicacoes = Noticia.objects.all()
    pacote_de_dados = {
        'publicacoes': publicacoes
    }
    return render(request, template_name, pacote_de_dados)