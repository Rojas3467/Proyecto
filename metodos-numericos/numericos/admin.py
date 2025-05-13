from django.contrib import admin
from .models import Ecuacion  

@admin.register(Ecuacion)
class EcuacionAdmin(admin.ModelAdmin):
    list_display = ('expresion', 'metodo', 'resultado')  
    search_fields = ('expresion', 'metodo')  

