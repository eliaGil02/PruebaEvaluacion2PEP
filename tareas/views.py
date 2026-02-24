from .models import Tarea
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView
from django.urls import reverse_lazy # reverse_lazy se usa para redirecciones después de enviar un formulario
from django.contrib.auth.mixins import LoginRequiredMixin # Mixin que obliga a estar autenticado

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

class CrearTareaView(LoginRequiredMixin, CreateView):# Vista basada en clase para crear nuevas tareas   
    model = Tarea
    template_name = "tareas/crear_tarea.html"
    fields = ["titulo", "descripcion", "estado"]
    success_url = reverse_lazy("lista_tareas")# Redirección tras guardar

    # Asignamos automáticamente el usuario logueado como autor
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
