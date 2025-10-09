# Ejercicio Listas
# Crea un programa que:
# 1. Declare una lista llamada números que contenga los valores [3, 8, 1, 6, 0, 8, 4].
# 2. Agrega un nuevo número al final de la lista (elige cualquier número).
# 3. Elimina el primer elemento de la lista.
# 4. Ordena la lista de menor a mayor.
# 5. Imprime la lista y su longitud.

# *author: Rafael Navarro Gómez | rafa140200@gmail.com

numeros = [3, 8, 1, 6, 0, 8, 4]
print(numeros)
numeros.append(10)
print(numeros)
del numeros[0]
print(numeros)
numeros.sort()
print(numeros)
print("Lista: ",numeros,"Longitud: ",len(numeros))