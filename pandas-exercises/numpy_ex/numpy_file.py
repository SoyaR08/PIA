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

# 6. Crear un array de 10 cincos.

array_of_five = np.full(10, 5)

print(array_of_five)

# 7. Transformar el array anterior a dimensión [2,5] y [5,2]

arf_2x5 = array_of_five.reshape(2, 5)
arf_5x2 = array_of_five.reshape(5, 2)

print(arf_2x5)
print(arf_5x2)

# 8. Encontrar los índices (no el valor) que no son cero dentro del siguiente array: [1,2,4,2,4,0,1,0,0,0,12,4,5,6,7,0]

array = np.array([1,2,4,2,4,0,1,0,0,0,12,4,5,6,7,0])

print(np.where(array != 0)[0])

# 9. Crear una matriz identidad 6x6

six_identity = np.identity(6)
print(six_identity)

# 10. Crear vector con 100 valores aleatorios de formato entero.

hundred_of_randoms = np.random.randint(0, 100, size=100)

print(hundred_of_randoms)

# 11. Crear un array con valores al azar de forma 3x3x3 (3 dimensiones)

three_dim_array = np.random.randint(0, 100, size=27).reshape(3, 3, 3)

print(three_dim_array)