from django.shortcuts import render
from django.views.generic import TemplateView
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
        print(context)
        return context