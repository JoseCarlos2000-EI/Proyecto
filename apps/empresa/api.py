from rest_framework.generics import ListAPIView
from apps.empresa.serializers import EmpresaSerializer

class EmpresaListAPIView (ListAPIView):
    serializer_class = EmpresaSerializer

    def get_queryset(self):
        empresa = self.get_serializer().Meta.model
        return empresa.objects.filter(status=True)