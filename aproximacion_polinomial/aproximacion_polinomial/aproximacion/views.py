from django.shortcuts import render
from .forms import InterpolacionForm, InterpolacionInversaForm
from .metodos import interpolacion_newton, interpolacion_inversa
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os
import uuid
def index(request):
    return render(request, 'aproximacion/index.html')


def interpolacion_view(request):
    resultado = None
    if request.method == 'POST':
        form = InterpolacionForm(request.POST)
        if form.is_valid():
            x = list(map(float, form.cleaned_data['puntos_x'].split(',')))
            y = list(map(float, form.cleaned_data['puntos_y'].split(',')))
            # Aquí capturamos los tres valores que devuelve la función
            pol, tabla_pasos, formulas_pasos = interpolacion_newton(x, y)

            niveles = [
                "Valores iniciales",
                "Primer nivel de diferencias divididas",
                "Segundo nivel de diferencias divididas",
                "Tercer nivel de diferencias divididas",
            ]

            pasos_detallados = []
            for i, nivel in enumerate(tabla_pasos):
                nombre_nivel = niveles[i] if i < len(niveles) else f"{i} nivel de diferencias divididas"
                pasos_detallados.append({
                    "nivel": nombre_nivel,
                    "valores": nivel,
                    "formulas": formulas_pasos[i] if i < len(formulas_pasos) else []
                })

            # Generar gráfica
            xp = np.linspace(min(x) - 1, max(x) + 1, 100)
            yp = [float(pol.evalf(subs={'x': xi})) for xi in xp]

            carpeta = os.path.join('aproximacion', 'static', 'aproximacion')
            os.makedirs(carpeta, exist_ok=True)
            nombre_grafica = f"graph_{uuid.uuid4().hex[:8]}.png"
            ruta_grafica = os.path.join(carpeta, nombre_grafica)

            plt.figure()
            plt.plot(xp, yp, label='Interpolación', color='blue')
            plt.scatter(x, y, color='red', label='Datos')
            plt.legend()
            plt.grid()
            plt.savefig(ruta_grafica, dpi=300)
            plt.close()

            resultado = {
                'valores_x': x,
                'valores_y': y,
                'polinomio': pol,
                'pasos': pasos_detallados,
                'grafica': nombre_grafica
            }
    else:
        form = InterpolacionForm()

    return render(request, 'aproximacion/resultado.html', {'form': form, 'resultado': resultado})




def interpolacion_inversa_view(request):
    resultado = None
    if request.method == 'POST':
        form = InterpolacionInversaForm(request.POST)
        if form.is_valid():
            y = list(map(float, form.cleaned_data['puntos_y'].split(',')))
            x = list(map(float, form.cleaned_data['puntos_x'].split(',')))
            pol_inv, tabla_pasos_inv = interpolacion_inversa(y, x)


            # Formatear cada nivel con explicaciones detalladas
            pasos_detallados_inv = [
                {"nivel": "Valores iniciales", "explicacion": "Estos son los valores originales de X.", "valores": tabla_pasos_inv[0]},
                {"nivel": "Primer nivel de diferencias divididas", "valores": tabla_pasos_inv[1]},
                {"nivel": "Segundo nivel de diferencias divididas", "valores": tabla_pasos_inv[2]},
            ]

            # Generación de la gráfica
            yp = np.linspace(min(y) - 1, max(y) + 1, 100)
            xp = [float(pol_inv.evalf(subs={'y': yi})) for yi in yp]

            plt.figure()
            plt.plot(xp, yp, label='Interpolación Inversa', color='green')
            plt.scatter(x, y, color='orange', label='Datos')
            plt.legend()
            plt.grid()

            carpeta = os.path.join('aproximacion', 'static', 'aproximacion')
            os.makedirs(carpeta, exist_ok=True)
            nombre_grafica_inv = f"graph_inv_{uuid.uuid4().hex[:8]}.png"
            ruta_grafica_inv = os.path.join(carpeta, nombre_grafica_inv)

            plt.savefig(ruta_grafica_inv, dpi=300)
            plt.close()

            resultado = {
                'valores_x': x,
                'valores_y': y,
                'polinomio_inverso': pol_inv,
                'pasos': pasos_detallados_inv,
                'grafica': nombre_grafica_inv
            }
    else:
        form = InterpolacionInversaForm()
    
    return render(request, 'aproximacion/resultado_inversa.html', {'form': form, 'resultado': resultado})


 
