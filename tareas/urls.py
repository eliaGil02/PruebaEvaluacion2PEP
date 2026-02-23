"""
URLS de la app tareas

Rutas específicas de esta app
"""

from django.urls import path
from .views import TareaListView

urlpatterns = [
    # ruta principal que muestra la lista de tareas
    path("", TareaListView.as_view(), name="lista_tareas"),
]
