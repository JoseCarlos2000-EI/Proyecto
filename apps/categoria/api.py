from rest_framework.generics import ListAPIView

from apps.categoria.serializers import CategoriaSerializer,AnunciosSerializer
from apps.empresa.models import Business
from apps.producto.models import Producto


class CategoriaListAPIView(ListAPIView):
    
    serializer_class = CategoriaSerializer
   
    def get_queryset(self):
        data = self.request.GET
        idEmpresa = data.get('id')
        #print(idEmpresa)
        categoria = self.get_serializer().Meta.model.objects.filter(status=True)
        if idEmpresa and idEmpresa.strip() != '':
            categoria = categoria.filter(business=idEmpresa)
        
        return categoria

class AnunciosAPIView(ListAPIView):
    serializer_class = AnunciosSerializer

    def get_queryset(self):
        data = self.request.GET
        idEmpresa = data.get('idEmpresa')
        print(idEmpresa)
        return self.get_serializer().Meta.model.objects.filter(business=idEmpresa)
      
