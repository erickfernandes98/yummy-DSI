from django.contrib import admin
from . models import Sobremesa

class ListandoSobremesas(admin.ModelAdmin):
    list_display = ('id', 'nome_sobremesa', 'publicada')
    list_display_links = ('id', 'nome_sobremesa')
    search_fields = ('nome_sobremesa',)
    list_filter = ('categoria',)
    list_editable = ('publicada',)
    list_per_page = 10

admin.site.register(Sobremesa, ListandoSobremesas)