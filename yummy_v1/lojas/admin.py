from django.contrib import admin
from .models import Loja

class ListandoLojas(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(Loja, ListandoLojas)
