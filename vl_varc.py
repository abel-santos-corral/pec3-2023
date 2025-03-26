import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
import os

# Definimos el rango de VarC
x = np.linspace(0, 2, 100)

# Definimos las funciones de membresía trapezoidales
VL = fuzz.trapmf(x, [0, 0, 0.2, 0.6])
L = fuzz.trapmf(x, [0, 0.4, 0.6, 1.4])
M = fuzz.trapmf(x, [0.8, 1.0, 1.0, 1.2])
H = fuzz.trapmf(x, [0.6, 1.4, 1.6, 2.0])
VH = fuzz.trapmf(x, [1.4, 1.8, 2.0, 2.0])

# Graficamos
plt.figure(figsize=(8, 5))
plt.plot(x, VL, 'c', linewidth=2, label='VL')
plt.plot(x, L, 'b', linewidth=2, label='L')
plt.plot(x, M, 'g', linewidth=2, label='M')
plt.plot(x, H, 'r', linewidth=2, label='H')
plt.plot(x, VH, 'm', linewidth=2, label='VH')

plt.title('Funciones de Membresía de VarC')
plt.xlabel('VarC')
plt.ylabel('Grado de pertenencia')
plt.legend()
plt.grid()

# Crear el directorio si no existe
output_dir = 'data/output/variables_linguisticas'
os.makedirs(output_dir, exist_ok=True)

# Guardar la imagen
output_path = os.path.join(output_dir, 'VarC.png')
plt.savefig(output_path)
plt.show()
