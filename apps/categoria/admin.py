from django.contrib import admin
from apps.categoria.models import Categoria

# Register your models here.
class AdminCategoria(admin.ModelAdmin):
    list_display = ('business','name', 'description','status')

admin.site.register(Categoria, AdminCategoria)