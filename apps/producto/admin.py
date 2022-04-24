from django.contrib import admin
from apps.producto.models import Producto, Categoria

# Register your models here.
class AdminProducto(admin.ModelAdmin):
    list_display = ('business','category','name', 'description', 'price', 'stock','status')   
 
admin.site.register(Producto, AdminProducto)