from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Tarea(models.Model):
    """
    Modelo que representa una tarea creada por un usuario.
    Cada tarea tiene: título, descripcion, fecha automática y autor
    """

    titulo = models.CharField(max_length=100)

    descripcion = models.TextField()

    fecha_creacion = models.DateTimeField(auto_now_add=True)

    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
