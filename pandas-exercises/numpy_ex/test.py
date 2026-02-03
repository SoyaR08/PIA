import numpy as np

# Rafael Navarro Gómez

# Tarea - Ejercicios NumPy

# 11. Crear un array con valores al azar de forma 3x3x3 (3 dimensiones)

three_dim_array = np.random.randint(0, 100, size=27).reshape(3, 3, 3)

print(three_dim_array)