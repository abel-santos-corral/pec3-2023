import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
import os

# Definimos el rango de VarB
x = np.linspace(0, 9, 100)

# Definimos las funciones de membresía trapezoidales
L = fuzz.trapmf(x, [0, 0, 0, 4])
M = fuzz.trapmf(x, [2, 3, 7, 8])
H = fuzz.trapmf(x, [4, 8, 8, 9])

# Graficamos
plt.figure(figsize=(8, 5))
plt.plot(x, L, 'b', linewidth=2, label='L')
plt.plot(x, M, 'g', linewidth=2, label='M')
plt.plot(x, H, 'r', linewidth=2, label='H')

plt.title('Funciones de Membresía de VarB')
plt.xlabel('VarB')
plt.ylabel('Grado de pertenencia')
plt.legend()
plt.grid()

# Crear el directorio si no existe
output_dir = 'data/output/variables_linguisticas'
os.makedirs(output_dir, exist_ok=True)

# Guardar la imagen
output_path = os.path.join(output_dir, 'VarB.png')
plt.savefig(output_path)
plt.show()
