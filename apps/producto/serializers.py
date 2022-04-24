from rest_framework import serializers
from apps.producto.models import Producto


class ProductoSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    class Meta:
        model = Producto
        fields = '__all__'

    def get_category(self,producto):
        if producto.id:
            return producto.category.name
        
