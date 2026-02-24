"""
URLS de la app tareas

Rutas específicas de esta app
"""

from django.urls import path
from .views import ListaTareasView, DetalleTareaView
from .views import CrearTareaView #+importamos la clase desde tarea/view.py

urlpatterns = [
    # ruta principal que muestra la lista de tareas
    path("", ListaTareasView.as_view(), name="lista_tareas"),
    # ruta que muestra el detalle de una tarea concreta
    path("tarea/<int:pk>/", DetalleTareaView.as_view(), name="detalle_tarea"),
    # Ruta para crear una nueva tarea
    path("crear/", CrearTareaView.as_view(), name="crear_tarea"),
]
