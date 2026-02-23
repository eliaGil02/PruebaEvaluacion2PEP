"""
URLS de la app tareas

Rutas específicas de esta app
"""

from django.urls import path
from .views import ListaTareasView, DetalleTareaView

urlpatterns = [
    # ruta principal que muestra la lista de tareas
    path("", ListaTareasView.as_view(), name="lista_tareas"),
    # ruta que muestra el detalle de una tarea concreta
    path("tarea/<int:pk>/", DetalleTareaView.as_view(), name="detalle_tarea"),
]
