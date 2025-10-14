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