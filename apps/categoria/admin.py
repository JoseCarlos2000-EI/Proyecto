from django.contrib import admin
from apps.categoria.models import Categoria
from apps.categoria.models import Anuncio
# Register your models here.
class AdminCategoria(admin.ModelAdmin):
    list_display = ('business','name', 'description','status')
class AdminAnuncios (admin.ModelAdmin):
    list_display = ('business','evento')
    
admin.site.register(Categoria, AdminCategoria)
admin.site.register(Anuncio, AdminAnuncios)