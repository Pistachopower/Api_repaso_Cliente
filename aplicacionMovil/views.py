from django.shortcuts import render
import requests
from django.core import serializers
from django.shortcuts import render, redirect
from requests.exceptions import HTTPError
from aplicacionMovil import helper
from .forms import *
import json

# Create your views here.
def index(request):
    return render(request, 'index.html')


def AplicacionMovil_list(request):
    headers= {'Authorization': 'Bearer y1Z9EUZX1I2uNC5DeCKW7o2p2gyvCb'}
    response= requests.get('http://127.0.0.1:8080/api/v1/listas-aplicacion/', headers=headers)
    
    aplicacion= response.json()
    return render(request, 'aplicacionMovil/listar.html', {'aplicacion': aplicacion})


def aplicacion_eliminar(request, aplicacion_id):

    headers = {"Authorization": "Bearer y1Z9EUZX1I2uNC5DeCKW7o2p2gyvCb"}
    response = requests.delete(
        f"http://127.0.0.1:8080/api/v1/aplicacion-eliminar/{aplicacion_id}/",
        headers=headers,
    )
    
    print(response)
    if response.status_code == requests.codes.ok:
        return redirect("AplicacionMovil_list")
        
    return redirect("AplicacionMovil_list")


def comentarios_list(request):
    headers= {'Authorization': 'Bearer y1Z9EUZX1I2uNC5DeCKW7o2p2gyvCb'}
    response= requests.get('http://127.0.0.1:8080/api/v1/listas-comentarios/', headers=headers)
    comentarios= response.json()
    return render(request, 'comentarios/listar_comentarios.html', {'comentarios': comentarios})


def comentario_eliminar(request, comentario_id):

    headers = {"Authorization": "Bearer y1Z9EUZX1I2uNC5DeCKW7o2p2gyvCb"}
    response = requests.delete(
        f"http://127.0.0.1:8080/api/v1/comentario-eliminar/{comentario_id}/",
        headers=headers,
    )
    
    print(response)
    if response.status_code == requests.codes.ok:
        return redirect("comentarios_list")
        
    return redirect("comentarios_list")


def comentario_crear(request):
        
    if request.method == "POST":
        try:
            formulario = ComentarioForm(request.POST)
            
            headers = {
                "Authorization": "Bearer y1Z9EUZX1I2uNC5DeCKW7o2p2gyvCb",
                "Content-Type": "application/json",
            }
            print(request.POST)
            

            response = requests.post(
                "http://127.0.0.1:8080/api/v1/comentario/crear/",
                headers=headers,
                data=json.dumps(formulario.data),
            )
            if response.status_code == requests.codes.ok:
                return redirect("comentarios_list")
            else:
                response.raise_for_status()
        except HTTPError as http_err:
            if response.status_code == 400:
                errores = response.json()
                for error in errores:
                    formulario.add_error(error, errores[error])
                return render(
                    request, "comentarios/crear.html", {"formulario": formulario}
                )
            # else:
            #     return error_500(request)
        except Exception as err:
            print(f"Ocurrió un error: {err}")
            # return error_500(request)
    else:
        formulario = ComentarioForm(None)
    return render(request, "comentarios/crear.html", {"formulario": formulario})


def comentario_editar_patch(request, comentario_id):

    datosFormulario = None

    if request.method == "POST":
        # se obtienen los datos del formulario
        datosFormulario = request.POST

    comentario = helper.obtener_comentario_select(comentario_id)  # se hace la consulta a la bd
    formulario = ComentarioActualizarNombreForm(
        datosFormulario,
        #texto_comentario: viene del formulario y comentario viene del helper
        initial={
            "texto_comentario": comentario["texto_comentario"],
        },
    )
    if request.method == "POST":
        try:
            formulario = ComentarioActualizarNombreForm(request.POST)
            #datos = request.POST.copy()
            
            headers = {
                "Authorization": "Bearer y1Z9EUZX1I2uNC5DeCKW7o2p2gyvCb",
                "Content-Type": "application/json",
            }
            
            response = requests.patch(
                f"http://127.0.0.1:8080/api/v1/comentario-nombre-editar/{comentario_id}/",
                headers=headers,
                data=json.dumps(formulario.data),
            )

            if response.status_code == requests.codes.ok:
                return redirect("comentarios_list")
            else:
                print(response.status_code)
                response.raise_for_status()
        except HTTPError as http_err:
            print(f"Hubo un error en la petición: {http_err}")
            if response.status_code == 400:
                errores = response.json()
                for error in errores:
                    formulario.add_error(error, errores[error])
                return render(
                    request,
                    "comentarios/actualizarNombreComentario.html",
                    {"formulario": formulario, "comentario": comentario},
                )
            
            # elif response.status_code == 403:
            #     return error_403(request)
            # else:
            #     return error_500(request)
        except Exception as err:
            print(f"Ocurrió un error: {err}")
            # return error_500(request)

    return render(
                    request,
                    "comentarios/actualizarNombreComentario.html",
                    {"formulario": formulario, "comentario": comentario},
                )


    
    

#def registrar_usuario(request):
#    if request.method == "POST":
#        try:
#            formulario = RegistroForm(request.POST)
#            if formulario.is_valid():
#
#                # se prepara el formulario para enviarlo a la API
#                headers = {"Content-Type": "application/json"}
#                response = requests.post("http://127.0.0.1:8080/api/v1/registrar/usuario",
#                 
#                    headers=headers,
#                    data=json.dumps(formulario.cleaned_data),
#                )
#
#                if response.status_code == requests.codes.ok:
#                    usuario = response.json()
#                    token_acceso = helper.obtener_token_session(
#                        formulario.cleaned_data.get("username"),
#                        formulario.cleaned_data.get("password1"),
#                    )
#                    request.session["usuario"] = usuario
#                    request.session["token"] = token_acceso
#                    return redirect("index")
#                else:
#                    print(response.status_code)
#                    response.raise_for_status()
#                print(formulario.errors)
#        except HTTPError as http_err:
#            print(f"Hubo un error en la petición: {http_err}")
#            if response.status_code == 400:
#                errores = response.json()
#                for error in errores:
#                    formulario.add_error(error, errores[error])
#                return render(
#                    request, "registration/signup.html", {"formulario": formulario}
#                )
#            else:
#                return error_404(request)
#        except Exception as err:
#            print(f"Ocurrió un error: {err}")
#            return error_500(request)
#
#    else:
#        formulario = RegistroForm()
#    return render(request, "registration/signup.html", {"formulario": formulario})

