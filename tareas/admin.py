from django.contrib import admin
from .models import Tarea

# Register your models here.

#registramos el modelo Tarea en el panel de administracion
admin.site.register(Tarea)