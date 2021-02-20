from django.contrib import admin
from django.urls import path
from apps.news import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # http://127.0.0.1:8000/admin/
    path('admin/', admin.site.urls),

    # http://127.0.0.1:8000/
    path('', views.index, name = 'index'),

    # http://127.0.0.1:8000/adicionar_noticia
    path('adicionar_noticia/', views.adicionar_noticia, name = 'adicionar_noticia'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.AdminSite.site_header = 'SENAC NEWS Login'
admin.AdminSite.site_title = 'Administração - sistema SENAC NEWS'
admin.AdminSite.index_title = "Administração - SENAC NEWS"
