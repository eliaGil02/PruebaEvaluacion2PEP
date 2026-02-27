from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tarea(models.Model):
    """
    Modelo que representa una tarea creada por un usuario.
    Cada tarea tiene: título, descripcion, fecha automática y autor
    """

    ESTADO_CHOICES = [
        ("pendiente", "Pendiente"),
        ("proceso", "En proceso"),
        ("completada", "Completada"),
    ] #en los tres estados que se puede encontrar una tarea

    titulo = models.CharField(max_length=100) #el titulo de la tarea

    descripcion = models.TextField() #la descripcion de la tarea

    fecha_creacion = models.DateTimeField(auto_now_add=True) #fecha de crecion automatica

    estado = models.CharField(
        max_length=20, choices=ESTADO_CHOICES, default="pendiente"
    )

    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    imagen = models.ImageField(upload_to='imagenes_tareas/', null = True, blank = True) 
    #carpeta donde se guardaran(imagenes tares), null = en base de datos puede no existir y blank es no obligatorio
    def __str__(self):
        return self.titulo
