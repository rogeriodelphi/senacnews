from django.shortcuts import render, redirect
from apps.news.models import Noticia
from apps.news.forms import NoticiaForm

def index(request):
    template_name = 'index.html'
    publicacoes = Noticia.objects.all()
    pacote_de_dados = {
        'publicacoes': publicacoes
    }
    return render(request, template_name, pacote_de_dados)

def adicionar_noticia(request):
    template_name = 'adicionar_noticia.html'
    if request.method == "POST":
        form = NoticiaForm(request.POST)

        if form.is_valid():
            form.save()

        print(form.errors)
        return redirect('index')
    else:
        form = NoticiaForm()
        context = {'form': form}
        return render(request, template_name, context)


def remover_noticia(request, id):
    template_name = 'remover_noticia.html'
    form = Noticia.objects.get(id=id)
    context = {'form': form}
    if request.method == 'POST':
        form.delete()
        return redirect('index')
    return render(request, template_name, context)

