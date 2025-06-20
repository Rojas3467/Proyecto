import numpy as np
from sympy import symbols, expand

def interpolacion_newton(x, y):
    if len(x) != len(y):
        raise ValueError("Las listas de puntos x e y deben tener la misma longitud.")
    n = len(x)
    coeficientes = np.copy(y)
    tabla = [coeficientes.tolist()]
    formulas = [["{:.2f}".format(val) for val in coeficientes.tolist()]]

    for j in range(1, n):
        nivel_formula = []
        for i in range(n - 1, j - 1, -1):
            numerador = coeficientes[i] - coeficientes[i - 1]
            denominador = x[i] - x[i - j]
            resultado = numerador / denominador
            formula = f"({coeficientes[i]:.2f} - {coeficientes[i-1]:.2f}) / ({x[i]:.2f} - {x[i-j]:.2f}) = {resultado:.2f}"
            coeficientes[i] = resultado
            nivel_formula.append(formula)
        tabla.append(coeficientes.tolist())
        formulas.append(nivel_formula)

    X = symbols('x')
    polinomio = coeficientes[0]
    acumulador = 1
    for i in range(1, n):
        acumulador *= (X - x[i - 1])
        polinomio += coeficientes[i] * acumulador

    return expand(polinomio), tabla, formulas


def interpolacion_inversa(y, x):
    """
    Realiza interpolación inversa, buscando el valor de x dado un y.
    Se invierten los valores para aplicar el método de Newton sobre y.
    """
    if len(y) != len(x):
        raise ValueError("Las listas de puntos y e x deben tener la misma longitud.")
    
    n = len(y)
    coeficientes = np.copy(x)  # Ahora los coeficientes se calculan en función de x
    tabla = [coeficientes.tolist()]
    
    #Cálculo de diferencias divididas respecto a y
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coeficientes[i] = (coeficientes[i] - coeficientes[i - 1]) / (y[i] - y[i - j])
        tabla.append(coeficientes.tolist())

    # Construcción del polinomio interpolante 
    Y = symbols('y')
    polinomio = coeficientes[0] #Esta línea inicia el polinomio con el primer coeficiente
    acumulador = 1
    #Se construye los términos restantes
    for i in range(1, n):
        acumulador *= (Y - y[i - 1])
        polinomio += coeficientes[i] * acumulador

    return expand(polinomio), tabla
