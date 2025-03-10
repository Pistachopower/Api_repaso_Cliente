from django.shortcuts import render
import requests
from django.core import serializers

# Create your views here.
def index(request):
    return render(request, 'principal.html')


def AplicacionMovil_list(request):
    headers= {'Authorization': 'Bearer yuKfBp5bo7O4E1DtviP1AGI0hIhTUr'}
    response= requests.get('http://127.0.0.1:8080/api/v1/listas-aplicacion/', headers=headers)
    
    aplicacion= response.json()
    return render(request, 'aplicacionMovil/listar.html', {'aplicacion': aplicacion})


