from django.db import models
from django.db.models.query_utils import subclasses

# Create your models here.

class prueba(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    
    def __str__(self):
        return self.titulo + ' ' + self.subtitulo
    
