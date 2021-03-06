from django.contrib import admin
from .models import Pessoa

class ListandoPessoas(admin.ModelAdmin):
    list_display = ('nome', 'email')
    list_display_links = ('nome',)
    search_fields = ('nome',)
    list_per_page = 10
    
admin.site.register(Pessoa, ListandoPessoas)