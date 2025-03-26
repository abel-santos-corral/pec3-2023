import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
import os

# Definimos el rango de VarD
x = np.linspace(0, 2, 100)

# Definimos las funciones de membresía trapezoidales
L = fuzz.trapmf(x, [0, 0, 0, 1])
M = fuzz.trapmf(x, [0, 1, 1, 2])
H = fuzz.trapmf(x, [0, 1, 2, 2])

# Graficamos
plt.figure(figsize=(8, 5))
plt.plot(x, L, 'b', linewidth=2, label='L')
plt.plot(x, M, 'g', linewidth=2, label='M')
plt.plot(x, H, 'r', linewidth=2, label='H')

plt.title('Funciones de Membresía de VarD')
plt.xlabel('VarD')
plt.ylabel('Grado de pertenencia')
plt.legend()
plt.grid()

# Crear el directorio si no existe
output_dir = 'data/output/variables_linguisticas'
os.makedirs(output_dir, exist_ok=True)

# Guardar la imagen
output_path = os.path.join(output_dir, 'VarD.png')
plt.savefig(output_path)
plt.show()