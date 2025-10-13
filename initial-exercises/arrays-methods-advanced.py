# Ejercicio 10: Métodos avanzados de listas
# 1. Crea una lista llamada números con los valores [12, 45, 78, 23, 56, 89, 23, 56].
# 2. Cuenta cuántas veces aparece el número 23 en la lista. 
# 3. Encuentra el índice de la primera aparición del número 56.  
# 4. Elimina el último número de la lista. 
# 5. Usa el método extend() para agregar los valores [100, 200, 300] al final de la lista. 
# 6. Haz una copia de la lista en una nueva variable llamada numeros_copia. 
# 7. Limpia (vacía) la lista original.

# *author: Rafael Navarro Gómez | rafa140200@gmail.com

numeros = [12, 45, 78, 23, 56, 89, 23, 56]
print("Lista inicial: ", numeros)
print("Cantidad de veces que aparece el 23: ", numeros.count(23))
print("Índice de la primera aparición del 56: ", numeros.index(56))
numeros.pop()
print("Lista después de eliminar el último número: ", numeros)
numeros.extend([100, 200, 300])
print("Lista luego de usar extend(): ", numeros)
numeros_copia = numeros.copy()
print("Copia de la lista en numeros_copia: ", numeros_copia)
numeros.clear()
print("Lista original después de limpiarla: ", numeros)