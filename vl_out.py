import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
import os

# Definimos el rango de Out
x = np.linspace(0, 10, 101)

# Definimos las funciones de membresía trapezoidales
VL = fuzz.trapmf(x, [0, 0, 0, 1])
L = fuzz.trapmf(x, [0, 2, 2, 3])
M = fuzz.trapmf(x, [2, 4, 5, 6])
H = fuzz.trapmf(x, [5, 6, 6, 9])
VH = fuzz.trapmf(x, [7, 8, 10, 10])

# Graficamos
plt.figure(figsize=(8, 5))
plt.plot(x, VL, 'c', linewidth=2, label='VL')
plt.plot(x, L, 'b', linewidth=2, label='L')
plt.plot(x, M, 'g', linewidth=2, label='M')
plt.plot(x, H, 'r', linewidth=2, label='H')
plt.plot(x, VH, 'm', linewidth=2, label='VH')

plt.title('Funciones de Membresía de Out')
plt.xlabel('Out')
plt.ylabel('Grado de pertenencia')
plt.legend()
plt.grid()

# Crear el directorio si no existe
output_dir = 'data/output/variables_linguisticas'
os.makedirs(output_dir, exist_ok=True)

# Guardar la imagen
output_path = os.path.join(output_dir, 'Out.png')
plt.savefig(output_path)
plt.show()
