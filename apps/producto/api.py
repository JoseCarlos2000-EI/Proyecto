from rest_framework.generics import ListAPIView
from apps.producto.serializers import  ProductoSerializer



class ProductoListAPIView(ListAPIView):
    serializer_class = ProductoSerializer

    def get_queryset(self):
        data = self.request.GET
        idEmpresa = data.get('idEmpresa')
        idCategoria=data.get('idCategoria')
        print(idEmpresa)
        print(idCategoria)
        producto = self.get_serializer().Meta.model
        return  producto.objects.filter(status = True, business = idEmpresa, category = idCategoria)        