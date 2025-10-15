# 11. Combina dos listas de números utilizando el operador +.
# 12. Crea una lista de cadenas y concatena todos los elementos en una sola cadena.
# 13. Crea una lista de números e imprime la longitud de la lista usando len().
# 14. Crea una lista de letras y usa index() para obtener el índice de una letra específica.
# 15. Usa extend() para añadir múltiples elementos de una lista a otra lista.
# 16. Accede a los últimos 3 elementos de una lista de números usando slicing.
# 17. Usa copy() para crear una copia de una lista de colores.
# 18. Crea una lista de listas (listas anidadas) y accede a un elemento de una lista interna.
# 19. Usa clear() para eliminar todos los elementos de una lista.
# 20. Multiplica una lista de 3 elementos por 4 y muestra el resultado.

# Ejercicio 11

array1 = [1, 2, 3]
array2 = [4, 5, 6]
array3 = array1 + array2
print("Lista combinada:", array3)

# Ejercicio 12

strings = ["¡","Hola", " ", "Mundo", "!"]
single_string = ""
for char in strings:
    single_string+=char
print("Cadena concatenada:", single_string)

# Ejercicio 13

numbers = [1, 2, 3, 4, 5, 6]
print("Longitud de la lista de números:", len(numbers))

# Ejercicio 14

chars = ['a', 'b', 'c', 'd', 'e']
print("Índice de e:", chars.index('e'))

# Ejercicio 15

list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
list1.extend(list2)
print("Lista después de usar extend():", list1)

# Ejercicio 16

print("Últimos 3 elementos de la lista:", chars[-3:])

# Ejercicio 17

colors = ["rojo", "verde", "azul"]
colors_copy = colors.copy()
print("Copia de la lista de colores:", colors_copy)

# Ejercicio 18

father_list = [colors, numbers, chars]
for list in father_list:
    print("Elemento de una lista interna:", list[0])
    break

# Ejercicio 19

print("Array 3 antes de la limpieza:", array3)
array3.clear()
print("Array 3 después de la limpieza:", array3)

# Ejercicio 20

elements = [1, 2, 3]
multiplied_list = lambda x: [i * 4 for i in x]
print("Lista multiplicada por 4:", multiplied_list(elements))
