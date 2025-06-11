from django.shortcuts import render
from sympy import Symbol
from sympy.parsing.sympy_parser import parse_expr
import numpy as np
from .metodos import gauss_elimination, gauss_jordan
from .models import HistorialEcuacion

def resolver_sistema(request):
    historial = HistorialEcuacion.objects.order_by('-fecha')[:10]
    resultado = ""
    grafico = None  
    pasos = ""
    if request.method == "POST":
        sistema = request.POST.get("sistema", "")
        metodo = request.POST.get("metodo", "")
        try:
            ecuaciones = sistema.strip().split("\n")

            # Lista de variables permitidas y detectadas en las ecuaciones
            posibles_vars = ['x', 'y', 'z', 'w', 't', 'u', 'v']
            variables = [var for var in posibles_vars if any(var in eq for eq in ecuaciones)]

            # Crear símbolos para sympy
            contexto = {var: Symbol(var) for var in variables}

            A = []
            b = []

            for eq in ecuaciones:
                izquierda, derecha = eq.strip().split("=")
                izquierda_expr = parse_expr(izquierda.strip(), local_dict=contexto)
                derecha_expr = parse_expr(derecha.strip(), local_dict=contexto)
                coefs = [float(izquierda_expr.coeff(contexto[v])) for v in variables]
                A.append(coefs)
                b.append(float(derecha_expr))

            A = np.array(A, dtype=float)
            b = np.array(b, dtype=float)

            if metodo == 'gauss':
                solucion, pasos, grafico = gauss_elimination(A, b)
            elif metodo == 'gauss_jordan':
                solucion, pasos, grafico = gauss_jordan(A, b)
            else:
                raise ValueError("Método no válido.")

            # Formatear resultado con variables y valores
            resultado = ", ".join(f"{var} = {val:.4f}" for var, val in zip(variables, solucion))

        except Exception as e:
            resultado = f"Error al procesar el sistema: {e}"

    contexto = {
        "resultado": resultado,
        "pasos": pasos,
        "grafico": grafico,
        "historial": historial,
    }
    return render(request, "ecuaciones/index.html", contexto)
