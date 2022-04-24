from django.contrib import admin
from apps.empresa.models import Business

# Register your models here.

class AdminNegocio(admin.ModelAdmin):
    list_display =('name','ruc','direction')

admin.site.register(Business, AdminNegocio)