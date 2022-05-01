from pip import List
from rest_framework.generics import ListAPIView
from apps.producto.serializers import  ProductoSerializer



class ProductoListAPIView(ListAPIView):
    serializer_class = ProductoSerializer

    def get_queryset(self):
        data = self.request.GET
        idEmpresa = data.get('idEmpresa')
        idCategoria = data.get('idCategoria')
        if idEmpresa and idEmpresa.strip()!="" and idCategoria and idCategoria.strip() != '':
            producto = self.get_serializer().Meta.model.objects.filter(status = True, business = idEmpresa, category = idCategoria)
        
        return producto

class ProductoDetalleListAPIView(ListAPIView):
    serializer_class = ProductoSerializer

    def get_queryset(self):
        data = self.request.GET
        idProducto = data.get('idProducto')
        print(idProducto)
        producto = self.get_serializer().Meta.model 
        return producto.objects.filter(status=True, id=idProducto)