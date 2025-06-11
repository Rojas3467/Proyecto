import matplotlib.pyplot as plt
import io
import base64
import numpy as np

def gauss_elimination(A, b):
    n = len(b)
    Ab = np.hstack([A, b.reshape(-1, 1)]) #Combina A y b en una matriz aumentada
    pasos = "Matriz aumentada inicial:\n" + str(Ab) + "\n\n"

    # Eliminación hacia adelante
    for i in range(n):
        max_row = np.argmax(np.abs(Ab[i:, i])) + i
        Ab[[i, max_row]] = Ab[[max_row, i]]
        pasos += f"Pivoteo: intercambiar fila {i} con fila {max_row}\n{Ab}\n\n"
        for j in range(i+1, n):
            factor = Ab[j][i] / Ab[i][i]
            Ab[j] = Ab[j] - factor * Ab[i]
            pasos += f"Eliminar fila {j} usando fila {i} (factor: {factor:.4f})\n{Ab}\n\n"

    # Sustitución regresiva segura
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        suma = sum(Ab[i, j] * x[j] for j in range(i+1, n))
        x[i] = (Ab[i, -1] - suma) / Ab[i, i]
        
    pasos += f"Resultado final (sustitución regresiva):\n x = {x}\n"
    
    fig, ax = plt.subplots(figsize=(5, 4))
    ax.imshow(Ab, cmap='Blues', aspect='auto')
    ax.set_title('Matriz aumentada final (Eliminación de Gauss)')
    ax.axis('off')
    
    rows, cols = Ab.shape
    for i in range(rows):
        for j in range(cols):
            valor = f"{Ab[i, j]:.2f}"
            ax.text(j, i, valor, ha='center', va='center', color='black', fontsize=10)
            
    plt.tight_layout()
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    grafico = base64.b64encode(buf.getvalue()).decode('utf-8')
    buf.close()

    return x, pasos, grafico
    
def gauss_jordan(A, b):
    n = len(b)
    Ab = np.hstack([A, b.reshape(-1, 1)]).astype(float) # lleva la matriz aumentada a la forma reducida por filas
    pasos = "Matriz aumentada inicial:\n" + str(Ab) + "\n\n"

    for i in range(n):
        max_row = np.argmax(np.abs(Ab[i:, i])) + i
        Ab[[i, max_row]] = Ab[[max_row, i]]
        pasos += f"Pivoteo: intercambiar fila {i} con fila {max_row}\n"
        pasos += str(Ab) + "\n\n"
        #Normalizacion del pivote
        Ab[i] = Ab[i] / Ab[i, i]
        pasos += f"Normalizar fila {i} para que pivote sea 1\n"
        pasos += str(Ab) + "\n\n"

        for j in range(n):
            if i != j:
                Ab[j] = Ab[j] - Ab[j, i] * Ab[i] #Elimina todos los valores en la columna i excepto el pivote
                pasos += f"Eliminar elemento en fila {j}, columna {i}\n"
                pasos += str(Ab) + "\n\n"

    x = Ab[:, -1]
    fig, ax = plt.subplots()
    ax.matshow(Ab, cmap='viridis')  # Mostrar la matriz final como imagen

    for (i, j), val in np.ndenumerate(Ab):
        ax.text(j, i, f"{val:.2f}", va='center', ha='center', color='white')

    plt.title("Matriz aumentada final (Gauss-Jordan)")

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)
    image_png = buf.getvalue()
    grafico = base64.b64encode(image_png).decode('utf-8')
    buf.close()

    return x, pasos, grafico

