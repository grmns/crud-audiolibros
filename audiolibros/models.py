# audiolibros/models.py

from django.db import models

class Audiolibro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    descripcion = models.TextField()
    audio = models.FileField(upload_to='audiolibros/')
    tipo = models.CharField(max_length=100)
    fecha_publicacion = models.DateField()

    def __str__(self):
        return self.titulo
