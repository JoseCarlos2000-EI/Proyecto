from django.conf.urls import url
from apps.producto.api import ProductoListAPIView
from apps.producto.views import tienda


urlpatterns = [
    url('productoAPI',ProductoListAPIView.as_view(), name='ListaProductos'),
    url(r'^tienda/(?P<id>\d+)$',tienda.as_view(), name='tienda')
]
