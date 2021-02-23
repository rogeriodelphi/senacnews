from django.contrib import admin
from .models import User

@admin.register(User)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'telefone', 'eSupervisor')


