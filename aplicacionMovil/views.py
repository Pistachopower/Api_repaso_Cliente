from django.shortcuts import render
import requests
from django.core import serializers

# Create your views here.
def index(request):
    return render(request, 'index.html')


def AplicacionMovil_list(request):
    response= requests.get('http://127.0.0.1:8000/api/v1/lista')
    
    aplicacion= response.json()
    return render(request, 'index.html', {'aplicacion': aplicacion})


