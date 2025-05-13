import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
import base64

def metodo_secante(f, x0, x1, tol=1e-6, max_iter=100):
    """
    Implementación del Método de la Secante para encontrar la raíz de una función.
    """
    x = sp.symbols('x')
    f_lambda = sp.lambdify(x, f)

    iteraciones = []
    for i in range(max_iter):
        fx0, fx1 = f_lambda(x0), f_lambda(x1)

        if abs(fx1) < tol:
            return {"raiz": x1, "iteraciones": iteraciones}
        
        if fx1 - fx0 == 0:
            return {"error": "División por cero en iteración."}
        
        x_new = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        
        iteraciones.append({
            "iteracion": i,
            "x0": x0,
            "x1": x1,
            "nuevo_x": x_new,
            "f(x0)": fx0,
            "f(x1)": fx1,
            "f(nuevo_x)": f_lambda(x_new)
        })
        
        x0, x1 = x1, x_new
    
    return {"raiz": x1, "iteraciones": iteraciones}

def graficar_secante(iteraciones, f):
    """
    Genera una gráfica que muestra la convergencia del Método de la Secante.
    """
    x = sp.symbols('x')
    
    # Extraer valores de aproximación
    xs = [iteracion["nuevo_x"] for iteracion in iteraciones]

    plt.figure()
    plt.plot(range(len(xs)), xs, marker='o', linestyle='--', color="red")
    plt.xlabel("Iteración")
    plt.ylabel("Aproximación de la raíz")
    plt.title("Convergencia del método de la Secante")
    plt.grid(True)

    # Convertir imagen a base64
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    return base64.b64encode(buffer.getvalue()).decode()
