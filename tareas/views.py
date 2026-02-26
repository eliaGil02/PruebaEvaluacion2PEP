from .models import Tarea

# vistas genericas
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
)

# reverse_lazy se usa para redirecciones después de enviar un formulario
from django.urls import (
    reverse_lazy,
)

# Mixin que obliga a estar autenticado
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# form de registro de users
from django.contrib.auth.forms import UserCreationForm

# framework de msj
from django.contrib import messages

# para redireccionar
from django.shortcuts import redirect

# importamos el form de registro que hemos hecho
from .forms import RegistroForm

# Create your views here.


class PermisoAutorAdmin(UserPassesTestMixin):
    # permite el acceso solo si el user es el autor o es un superusuario
    def test_func(self):
        objeto = self.get_object()

        if self.request.user == objeto.autor:
            return True

        if self.request.user.is_staff or self.request.user.is_superuser:
            return True

        return False

    def handle_no_permission(self):
        messages.error(self.request, "No tienes permiso para realizar esta acción.")
        return redirect("lista_tareas")


class ListaTareasView(LoginRequiredMixin, ListView):
    # vista basada en clase que muestra todas las tareas
    model = Tarea  # modelo que se va a mostrar
    template_name = "tareas/lista_tareas.html"  # plantilla que se usa
    context_object_name = "tareas"  # nombre que usamos en el HTML
    ordering = ["-fecha_creacion"]  # ordenar por fecha de creacion descendente

    # sobreescribimos el metodo q obtiene los datos, q permite modificar la lista de tareas antes de enviarla
    def get_queryset(self):
        # si es superusuario puede ver todas las tareas
        if self.request.user.is_staff or self.request.user.is_superuser:
            queryset = Tarea.objects.all()
        else:
            queryset = Tarea.objects.filter(
                autor=self.request.user
            )  # obtenemos todas las tareas de el usuario
        busqueda = self.request.GET.get(
            "tareaBuscar"
        )  # recogemos lo q el usuario escribe en el buscador
        if busqueda:
            # filtramos las tareas q tenga el titulo con el texto buscado
            queryset = queryset.filter(titulo__icontains=busqueda)

        return queryset  # devolvemos la lista final


class DetalleTareaView(LoginRequiredMixin, DetailView):
    # vista q muestra el detalle de una tarea concreta
    model = Tarea  # modelo del q se obtendrá el objeto
    template_name = "tareas/detalle_tarea.html"  # plantilla que se usa
    context_object_name = "tarea"  # nombre que usamos en el HTML

    # limitar queryset para evitar q un user pueda ver tareas q no le corresponden
    def get_queryset(self):
        if self.request.user.is_staff or self.request.user.is_superuser:
            return Tarea.objects.all()
        return Tarea.objects.filter(autor=self.request.user)


class CrearTareaView(
    LoginRequiredMixin, CreateView
):  # Vista basada en clase para crear nuevas tareas
    model = Tarea
    template_name = "tareas/crear_tarea.html"
    fields = ["titulo", "descripcion", "estado"]
    success_url = reverse_lazy("lista_tareas")  # Redirección tras guardar

    # Asignamos automáticamente el usuario logueado como autor
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class EliminarTareaView(
    LoginRequiredMixin,
    PermisoAutorAdmin,
    DeleteView,
):
    # vista para eliminar una tarea
    model = Tarea
    template_name = "tareas/eliminar_tarea.html"
    success_url = reverse_lazy("lista_tareas")


class RegistrarseView(CreateView):
    # vista para registrarse
    form_class = RegistroForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")


class EditarTareaView(LoginRequiredMixin, PermisoAutorAdmin, UpdateView):
    # vista para modificar una tarea ya hecha
    model = Tarea
    template_name = "tareas/editar_tarea.html"
    fields = ["titulo", "descripcion", "estado"]
    success_url = reverse_lazy("lista_tareas")  # Redirección tras guardar
