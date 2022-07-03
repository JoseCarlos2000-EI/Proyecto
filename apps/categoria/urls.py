from django.conf.urls import url
from apps.categoria.api import CategoriaListAPIView,AnunciosAPIView
from apps.categoria.views import Categorias

    
urlpatterns = [
    url('categoriaAPI',CategoriaListAPIView.as_view(), name='ListaCategorias'),
    url(r'(?P<id>\d+)$',Categorias.as_view(), name='categorias'),
    url('AnunciosAPI', AnunciosAPIView.as_view(), name='anuncios')
]
    
    