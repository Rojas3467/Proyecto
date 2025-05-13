from rest_framework.views import APIView
from rest_framework.response import Response
import sympy as sp
from django.shortcuts import render
from .utils import metodo_secante, graficar_secante

class ResolverEcuacion(APIView):
    """
    API para resolver ecuaciones con el método de la secante.
    Se validan los datos de entrada para evitar errores de ejecución.
    """
    def post(self, request):
        expresion = request.data.get("expresion")

        # Validación de los valores iniciales
        try:
            x0 = float(request.data.get("x0"))
            x1 = float(request.data.get("x1"))
            if x0 == x1:
                return Response({"error": "Los valores iniciales deben ser diferentes"}, status=400)
        except ValueError:
            return Response({"error": "Valores numéricos inválidos"}, status=400)

        # Validación de la expresión matemática
        x = sp.symbols('x')
        try:
            f = sp.sympify(expresion)
        except:
            return Response({"error": "Expresión inválida"}, status=400)

        # Aplicar el método de la secante
        resultado = metodo_secante(f, x0, x1)

        # Generar la gráfica si hay iteraciones
        if "iteraciones" in resultado and resultado["iteraciones"]:
            resultado["grafico"] = graficar_secante(resultado["iteraciones"], f)

        return Response(resultado)

def index(request):
    """
    Vista para cargar la página principal de la aplicación.
    """
    return render(request, "numericos/index.html")
