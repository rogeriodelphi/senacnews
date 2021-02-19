from django.contrib import admin

from apps.news.models import Autor, Noticia


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sexo', 'cidade', 'curriculo')


@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'data_publicacao', 'categoria', 'assunto', 'autor')