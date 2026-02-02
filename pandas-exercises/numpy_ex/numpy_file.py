import numpy as np

# Rafael Navarro Gómez

# Tarea - Ejercicios NumPy

# 1. Crear un vector con valores dentro del rango 10-49

vector_test = np.arange(10, 50, 1)

print(vector_test)

# 2. Invertir vector

print(vector_test[::-1])

# 3. Crear un array de 10 ceros.

zeros_v = np.zeros(10)

print(zeros_v)

# 4. Crear un array de 10 unos.

ones_v = np.ones(10)

print(ones_v)

# 5. Crear matriz 3x3 con valores del 0 a 8.

m = np.arange(0, 9).reshape(3, 3)

print(m)