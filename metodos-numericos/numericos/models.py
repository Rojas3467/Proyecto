from django.db import models

class Ecuacion(models.Model):
    expresion = models.CharField(max_length=255)
    metodo = models.CharField(max_length=50, default="secante")
    resultado = models.TextField(blank=True, null=True)
