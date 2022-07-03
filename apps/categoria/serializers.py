from rest_framework import serializers
from apps.categoria.models import Categoria
from apps.categoria.models import Anuncio
from apps.producto.models import Producto
from django.urls import reverse


class CategoriaSerializer(serializers.ModelSerializer):
    minPrice = serializers.SerializerMethodField()
    urlTienda = serializers.SerializerMethodField()
    class Meta:
        model = Categoria
        fields = '__all__'

    def get_minPrice(self,categoria):
        if categoria.id:
            minPrice = Producto.objects.filter(category=categoria.id , business=categoria.business ).order_by('price')[0]
            print(minPrice)
            return minPrice.price

    def get_urlTienda(self, categoria):
        if categoria.id:
            url = reverse('producto:tienda', kwargs={'id': categoria.id})
            return url       


class AnunciosSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Anuncio
        fields = '__all__'


            

            