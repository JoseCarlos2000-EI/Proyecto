from dataclasses import field
from rest_framework import serializers
from django.urls import reverse
from apps.empresa.models import Business


class EmpresaSerializer (serializers.ModelSerializer):
    urlCategoria = serializers.SerializerMethodField()
    class Meta:
        model = Business
        fields ='__all__'


    def get_urlCategoria(self, empresa):
        if empresa.id:
            url = reverse('categoria:categorias', kwargs={'id': empresa.id})
            return url    