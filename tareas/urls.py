"""
URLS de la app tareas

Rutas específicas de esta app
"""

from django.urls import path

#importamos las clases creadas en taareas / view
from .views import (ListaTareasView, DetalleTareaView, CrearTareaView, RegistrarseView, EditarTareaView, EliminarTareaView,)


urlpatterns = [
    # ruta principal que muestra la lista de tareas
    path("", ListaTareasView.as_view(), name="lista_tareas"),

    # ruta que muestra el detalle de una tarea concreta
    path("tarea/<int:pk>/", DetalleTareaView.as_view(), name="detalle_tarea"),

    # Ruta para crear una nueva tarea
    path("crear/", CrearTareaView.as_view(), name="crear_tarea"),

    #ruta para editar la tarea
    path("editar/<int:pk>/", EditarTareaView.as_view(), name="editar_tarea"),

    #ruta para borrar la tarea
    path("eliminar/<int:pk>/", EliminarTareaView.as_view(), name="eliminar_tarea"),

    # ruta para registrarse
    path("signup/", RegistrarseView.as_view(), name="signup"),
]
