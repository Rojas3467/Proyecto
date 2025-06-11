from django.db import models

class HistorialEcuacion(models.Model):
    ecuaciones = models.TextField()
    metodo = models.CharField(max_length=50)
    solucion = models.CharField(max_length=200)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.metodo} - {self.fecha}"


