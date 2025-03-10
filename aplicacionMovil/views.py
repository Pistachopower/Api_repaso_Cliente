from django.shortcuts import render
import requests
from django.core import serializers

# Create your views here.
def index(request):
    return render(request, 'index.html')


def AplicacionMovil_list(request):
    response= requests.get('http://127.0.0.1:8080/api/v1/listas-aplicacion/')
    
    aplicacion= response.json()
    return render(request, 'listar.html', {'aplicacion': aplicacion})


