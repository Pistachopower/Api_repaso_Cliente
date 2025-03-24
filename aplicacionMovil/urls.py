from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("listar/", views.AplicacionMovil_list, name="AplicacionMovil_list"),
    path(
        "aplicacion-eliminar/<int:aplicacion_id>/",
        views.aplicacion_eliminar,
        name="aplicacion_eliminar",
    ),
    path("listar-comentarios/", views.comentarios_list, name="comentarios_list"),
    path(
        "comentario-eliminar/<int:comentario_id>/",
        views.comentario_eliminar,
        name="comentario_eliminar",
    ),
    path("comentario/crear", views.comentario_crear, name="comentario_crear"),
    
    path("comentario/editar-nombre/<int:comentario_id>/", views.comentario_editar_patch, name="comentario_editar_patch"),
    
    
    
    
    # sesiones
    # path("usuario/crear", views.registrar_usuario, name="registrar_usuario"),
]
