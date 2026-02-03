import numpy as np

# Rafael Navarro Gómez

# Tarea - Ejercicios NumPy

# 16. Crear dos arrays aleatorios del mismo tamaño (3x3 o 5x5) y verificar si son iguales. Comprobar si algún elemento coincide, generando matriz booleana.

random_m1 = np.random.randint(1, 10, size=(3, 3))
random_m2 = np.random.randint(1, 10, size=(3, 3))

print(random_m1 == random_m2)

