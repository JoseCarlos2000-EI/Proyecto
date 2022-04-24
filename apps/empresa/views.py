from django.shortcuts import render
from django.template import Template
from django.views.generic import TemplateView
# Create your views here.

class Home (TemplateView):
    template_name = "index.html"
