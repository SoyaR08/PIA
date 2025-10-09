# Ejercicio 6: Tuplas
# 1. Crea una tupla llamada puntos que contenga los siguientes valores: (5, 10, 15, 20, 25).
# 2. Imprime el valor en la tercera posición de la tupla.
# 3. Convierte la tupla en una lista.
# 4. Agrega el valor 30 al final de la nueva lista.
# 5. Convierte la lista nuevamente en tupla y imprímela.


# *author: Rafael Navarro Gómez | rafa140200@gmail.com

puntos = tuple((5, 10, 15, 20, 25))
print("Tupla:",puntos)
print("Valor 3º posición:",puntos[2])
tuple_list = list(puntos)
print("Tupla convertida en lista:",tuple_list)
tuple_list.append(30)
print("Tupla con el valor 30 añadido:",tuple_list)
puntos = tuple(tuple_list.copy())
print("Tupla reconvertida:",puntos)