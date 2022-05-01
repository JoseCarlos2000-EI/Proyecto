from django.conf.urls import url
from apps.producto.api import ProductoDetalleListAPIView, ProductoListAPIView
from apps.producto.views import carrito, checkout, tienda,detalleProducto


urlpatterns = [
    url(r'^productoAPI$',ProductoListAPIView.as_view(), name='ListaProductos'),
    url(r'^detalle-productoAPI$',ProductoDetalleListAPIView.as_view(), name='detalleProductoAPI'),
    url(r'^tienda/(?P<id>\d+)$',tienda.as_view(), name='tienda'),
    url(r'^producto-detalle/(?P<id>\d+)$',detalleProducto.as_view(), name='detalleProducto'),
    url(r'^checkout/$',checkout.as_view(), name='checkout'),
    url(r'^carrito/$',carrito.as_view(), name='carrito'),
    
]
