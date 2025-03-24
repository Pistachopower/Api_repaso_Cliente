import requests

# import environ
import os
from pathlib import Path


def obtener_aplicacion_movil_select():
    headers = {'Authorization': 'Bearer y1Z9EUZX1I2uNC5DeCKW7o2p2gyvCb'}
    response = requests.get(
        "http://127.0.0.1:8080/api/v1/listas-aplicacion/", headers=headers
    )
    aplicaciones = response.json()

    lista_aplicaciones = [("", "Ninguna")]
    for app in aplicaciones:
        lista_aplicaciones.append((app["id"], app["nombre"]))
    return lista_aplicaciones


def obtener_usuarios_select():
    headers = {'Authorization': 'Bearer y1Z9EUZX1I2uNC5DeCKW7o2p2gyvCb'}
    response = requests.get(
        "http://127.0.0.1:8080/api/v1/listar-usuarios/", headers=headers
    )
    usuarios = response.json()

    lista_usuarios = [("", "Ninguna")]
    for user in usuarios:
        lista_usuarios.append((user["id"], user["username"]))
    return lista_usuarios


def obtener_comentario_select(comentario_id):
    headers = {'Authorization': 'Bearer y1Z9EUZX1I2uNC5DeCKW7o2p2gyvCb'}
    response = requests.get(
        "http://127.0.0.1:8080/api/v1/texto-comentario/" + str(comentario_id) + "/", headers=headers
    )
    comentario = response.json()

    return comentario


# BASE_DIR = Path(__file__).resolve().parent.parent
# environ.Env.read_env(
#    os.path.join(BASE_DIR, ".env"), True
# )  # configura todo lo referente a las variables de entorno
# env = environ.Env()
#
#
# class helper:
#    def obtener_aplicacion_select(aplicacion_id):
#        headers = {"Authorization": "Bearer " + env("OAUTH2_ACCESS_TOKEN")}
#        response = requests.get(
#            "http://127.0.0.1:8080/api/v1/listas-aplicacion/" + str(aplicacion_id),
#            headers=headers,
#        )
#        aplicacion = response.json()
#        return aplicacion
