from django.urls import path
from . import views

app_name = 'apps/news'
urlpatterns = [
    path('', views.index, name='index'),
    path('adicionar_noticia/', views.adicionar_noticia, name='adicionar_noticia'),
    path('remover_noticia/<int:id>/', views.remover_noticia, name='remover_noticia'),
    path('listar_noticias', views.listar_noticias, name='listar_noticias'),
]
