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

# 12. Encontrar los valores mínimos y máximos del anterior array

mix_element, max_element = three_dim_array.min(), three_dim_array.max()

print(f"Elemento mínimo: {mix_element}. Elemento máximo: {max_element}")

# 13. Indicar los índices (posición) de los valores mínimos y máximos del array

min_index = np.unravel_index(three_dim_array.argmin(), three_dim_array.shape) #argmin convierte el array en unidimensional y devuelve ese índice, para que unravel_index lo traduzca a las dimensiones originales
max_index = np.unravel_index(three_dim_array.argmax(), three_dim_array.shape)


print(f"Índice del elemento mínimo: {min_index}. Índice del elemento máximo: {max_index}")

# 14. Generar una matriz de tamaño 10x10 en la que los bordes sean 1 y el interior ceros (0). (Utilizar rangos de índices)

stylish_m = np.ones((10, 10))

stylish_m[1:-1, 1:-1] = 0

print(stylish_m)

# 15. Crear array de tamaño 5x5 con los siguientes valores; [0,1,2,3,4]

m5x5 = np.random.randint(0, 5, size=(5, 5))

print(m5x5)

# 16. Crear dos arrays aleatorios del mismo tamaño (3x3 o 5x5) y verificar si son iguales. Comprobar si algún elemento coincide, generando matriz booleana.

random_m1 = np.random.randint(1, 10, size=(3, 3))
random_m2 = np.random.randint(1, 10, size=(3, 3))

print(random_m1 == random_m2)

# 17. Generar array de dimensión 5x5 en el que los elementos sean de tipo numérico entero aleatorio comprendido entre el 1 y 100.

random_5x5_arr = np.random.randint(1, 101, size=(5, 5))

print(random_5x5_arr)


# 18. Dado el array anterior, obtener la suma total de la matriz 5x5.

total_sum = np.sum(random_5x5_arr)

print(total_sum)

# 19. Dado el array anterior, obtener un nuevo array que contenga la suma de cada una de las columnas.

columns_sum = np.sum(random_5x5_arr, axis=0)

print(columns_sum)

# 20. Dado el array anterior, extraer fila inicial, fila intermedia (fila 3) y la última fila.

rows = random_5x5_arr.shape[0]

first_row = random_5x5_arr[0]
middle_row = random_5x5_arr[rows // 2]
last_row = random_5x5_arr[-1]

print(first_row)
print(middle_row)
print(last_row)