from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class Categorias(TemplateView):
    template_name = "categories.html"
    
    def get_context_data(self,**kwargs):
        if  kwargs.get('id'):
            self.request.session['idEmpresa']=kwargs.get('id')
        idEmpresa=self.request.session['idEmpresa']
        context = super().get_context_data()
        context["idEmpresa"] = idEmpresa
        #print (context["id"])
        return context