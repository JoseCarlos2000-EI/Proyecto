from django.conf.urls import url
from apps.empresa.api import EmpresaListAPIView
from apps.empresa.views import Home


urlpatterns = [
    url('empresaAPI', EmpresaListAPIView.as_view(), name='empresaAPI'),
    url(r'^$', Home.as_view(), name='inicio'),
    
]
