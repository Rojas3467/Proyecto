from django.contrib import admin
from .models import HistorialEcuacion

@admin.register(HistorialEcuacion)
class HistorialEcuacionAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'metodo', 'solucion')
    readonly_fields = ('fecha',)
    ordering = ('-fecha',)


