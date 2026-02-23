from .models import Tarea
from django.views.generic import ListView, DetailView

# Create your views here.


class ListaTareasView(ListView):
    # vista basada en clase que muestra todas las tareas
    model = Tarea  # modelo que se va a mostrar
    template_name = "tareas/lista_tareas.html"  # plantilla que se usa
    context_object_name = "tareas"  # nombre que usamos en el HTML


class DetalleTareaView(DetailView):
    model = Tarea  # modelo del q se obtendrá el objeto
    template_name = "tareas/detalle_tarea.html"  # plantilla que se usa
    context_object_name = "tarea"  # nombre que usamos en el HTML
    ordering = ["-fecha_creacion"]  # ordenar por fecha de creacion descendente
