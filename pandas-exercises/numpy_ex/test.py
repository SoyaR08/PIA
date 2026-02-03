import numpy as np

# Rafael Navarro Gómez

# Tarea - Ejercicios NumPy

# 13. Indicar los índices (posición) de los valores mínimos y máximos del array

three_dim_array = np.random.randint(0, 100, size=27).reshape(3, 3, 3)

mix_element, max_element = three_dim_array.min(), three_dim_array.max()

print(f"Elemento mínimo: {mix_element}. Elemento máximo: {max_element}")
