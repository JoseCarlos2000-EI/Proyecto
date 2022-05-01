from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse
# Create your views here.
class tienda (TemplateView):
    template_name ='products.html'
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data()
        if kwargs.get('id'):
            self.request.session['idCategoria']=kwargs.get('id')
        categoria = self.request.session['idCategoria']
        context["idEmpresa"] = self.request.session['idEmpresa']    
        context["idCategoria"] = categoria
        #print(context)
        return context
    

class detalleProducto(TemplateView):
    template_name='product-detail.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data()
        #Obtiene id de Producto
        if kwargs.get('id'):
            self.request.session['idProducto']=kwargs.get('id')
        
        context["idProducto"]=self.request.session['idProducto']
        ##Obtener Url de Categorias
        idEmpresa = self.request.session["idEmpresa"]
        url = reverse('categoria:categorias', kwargs={'id': idEmpresa})
        context["urlCategoria"]=url

        ##Obtener Url de Tienda
        idCategoria = self.request.session["idCategoria"]
        urlTienda = reverse('producto:tienda', kwargs={'id':idCategoria})
        context["urlTienda"]=urlTienda
        ##print(context["idProducto"])
        return context

class checkout(TemplateView):
    template_name='checkout.html'
    def get_context_data(self,**kwargs):
        context = super().get_context_data()
        idEmpresa = self.request.session["idEmpresa"]
        url = reverse('categoria:categorias', kwargs={'id': idEmpresa})
        context["urlCategoria"]=url
        print(url)
        return context


class carrito(TemplateView):
    template_name='carrito.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data()
        if 'idEmpresa' in self.request.session:
            idEmpresa = self.request.session["idEmpresa"]
        else:
            idEmpresa = 1    
        url = reverse('categoria:categorias', kwargs={'id': idEmpresa})
        context["urlCategoria"]=url
        print(url)
        return context
    

