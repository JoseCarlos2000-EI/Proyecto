from rest_framework import serializers
from apps.producto.models import Producto
from django.urls import reverse

class ProductoSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    urlDetalle = serializers.SerializerMethodField()
    class Meta:
        model = Producto
        fields = '__all__'

    def get_category(self,producto):
        if producto.id:
            return producto.category.name

    def get_urlDetalle(self, producto):
        if producto.id:
            url = reverse('producto:detalleProducto', kwargs={'id': producto.id})
            return url              
        
