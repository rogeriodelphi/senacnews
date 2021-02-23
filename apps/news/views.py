from django.shortcuts import render, redirect, get_object_or_404
from apps.news.models import Noticia
from apps.news.forms import NoticiaForm

def index(request):
    template_name = 'index.html'
    publicacoes = Noticia.objects.all()
    pacote_de_dados = {
        'publicacoes': publicacoes
    }
    return render(request, template_name, pacote_de_dados)

def listar_noticias(request):
    # template_name = 'listar_noticias.html'
    # noticias = Noticia.objects.all()
    # context = {'noticias': noticias}
    # return render(request, template_name, context)
    context = {'noticias': Noticia.objects.all()}
    return render(request, 'listar_noticias.html', context)


def adicionar_noticia(request):
    template_name = 'adicionar_noticia.html'
    if request.method == "POST":
        form = NoticiaForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

        print(form.errors)
        return redirect('news:listar_noticias')
    else:
        form = NoticiaForm()
        context = {'form': form}
        return render(request, template_name, context)


def editar_noticia(request, id):
    template_name = 'adicionar_noticia.html'
    noticia = get_object_or_404(Noticia, pk=id)
    form = NoticiaForm(request.POST or None, request.FILES or None, instance=noticia)
    context = {'form': form}
    if form.is_valid():
        form.save()
        return redirect('news:listar_noticias')
    return render(request, template_name, context)


def remover_noticia(request, id):
    template_name = 'remover_noticia.html'
    form = Noticia.objects.get(id=id)
    context = {'form': form}
    if request.method == 'POST':
        form.delete()
        return redirect('news:listar_noticias')
    return render(request, template_name, context)

