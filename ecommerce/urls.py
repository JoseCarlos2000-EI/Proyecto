from django.contrib import admin
from django.conf.urls import url, include
from django.conf import settings 
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^empresa/',include(('apps.empresa.urls','apps.empresa'),namespace='empresa')),
    url(r'^categoria/',include(('apps.categoria.urls','apps.categoria'),namespace='categoria')),
    url(r'^producto/',include(('apps.producto.urls','apps.producto'),namespace='producto')),
    url(r'^',include(('apps.empresa.urls','apps.empresa'),namespace='inicio'))
]+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
