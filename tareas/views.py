from .models import Tarea
from django.views.generic import ListView, DetailView

# Create your views here.


class ListaTareasView(ListView):
    # vista basada en clase que muestra todas las tareas
    model = Tarea  # modelo que se va a mostrar
    template_name = "tareas/lista_tareas.html"  # plantilla que se usa
    context_object_name = "tareas"  # nombre que usamos en el HTML
    ordering = ["-fecha_creacion"]  # ordenar por fecha de creacion descendente

    # sobreescribimos el metodo q obtiene los datos, q permite modificar la lista de tareas antes de enviarla
    def get_queryset(self):
        queryset = super().get_queryset()  # obtenemos todas las tareas
        busqueda = self.request.GET.get(
            "tareaBuscar"
        )  # recogemos lo q el usuario escribe en el buscador
        if busqueda:
            # filtramos las tareas q tenga el titulo con el texto buscado
            queryset = queryset.filter(titulo__icontains=busqueda)

        return queryset  # devolvemos la lista final


class DetalleTareaView(DetailView):
    model = Tarea  # modelo del q se obtendrá el objeto
    template_name = "tareas/detalle_tarea.html"  # plantilla que se usa
    context_object_name = "tarea"  # nombre que usamos en el HTML
