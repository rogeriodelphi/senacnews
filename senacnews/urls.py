from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# from django.conf.urls import url
# from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('noticias/', include('apps.news.urls', namespace='news')),
    # url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.AdminSite.site_header = 'SENAC NEWS Login'
admin.AdminSite.site_title = 'Administração - sistema SENAC NEWS'
admin.AdminSite.index_title = "Administração - SENAC NEWS"
