from django.contrib import admin
from .models import Autor, Artigo


admin.site.register(Autor)

class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'publicado_em', 'atualizado_em')
    list_filter = ('publicado_em', 'autor')
    search_fields = ('titulo', 'texto')

admin.site.register(Artigo, ArtigoAdmin)

